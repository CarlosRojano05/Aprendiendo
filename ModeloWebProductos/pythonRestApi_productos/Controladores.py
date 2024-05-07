from Modelproductos import Modelproductos

#linea de codigo Importar libreria
from flask import Flask, jsonify, request
from flask_cors import CORS

#codigo ejecucion de la API
app = Flask(__name__)
CORS(app)

productos = Modelproductos()

@app.route('/productos', methods = ['GET'])
def listarproductos():
    return jsonify(productos.obtener_productos())


@app.route('/producto/<int:id>', methods=['GET'])
def producto(id): 
    
        producto = productos.obtener_producto(id)
        return jsonify(producto)
    
        
@app.route('/nuevo_producto', methods = ['POST'])
def crear_producto():
    nombre = request.json['nombre']
    precio = request.json['precio']
    productos.insertar_producto(nombre, precio)
    return jsonify({"mensaje": "producto creado exitosamente"})

@app.route('/actualizar_producto/<int:id>', methods = ['PUT'])
def actualizar_producto(id):
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('precio')
    
    if nombre is None and precio is None:
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400
    
    else:
        productos.actualizar_producto(id, nombre, precio)
        return jsonify({"mensaje": "Producto actualizado correctamente"})
    
    
@app.route('/eliminar_producto/<int:id>', methods = ['DELETE'])
def eliminar_producto(id):
    if productos.obtener_producto(id):
       productos.eliminar_producto(id)
       return jsonify({"mensaje": "producto eliminado correctamente"})
    else:
       return jsonify({"mensaje": "el producto no existe"}), 404
   
if __name__ == '__main__' :
    app.run(debug = True)