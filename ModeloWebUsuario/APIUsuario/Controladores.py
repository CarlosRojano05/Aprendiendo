from ModelUsuarios import ModelUsuarios
from flask import Flask, jsonify, request
from flask_cors import CORS
import hashlib  # Para hashing de contraseñas

app = Flask(__name__)
CORS(app)

usuarios = ModelUsuarios()

# Crear un hash para una contraseña para asegurarla
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# CRUD para usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios.obtener_usuarios())

@app.route('/usuario/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = usuarios.obtener_usuario(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

@app.route('/nuevo_usuario', methods=['POST'])
def crear_usuario():
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')
    
    if not nombre or not email or not password:
        return jsonify({"mensaje": "Faltan datos para crear el usuario"}), 400
    
    hashed_password = hash_password(password)  # Hash the password
    usuarios.insertar_usuario(nombre, email, hashed_password)
    
    return jsonify({"mensaje": "Usuario creado exitosamente"})

@app.route('/actualizar_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    
    if not nombre and not email:
        return jsonify({"mensaje": "No se proporcionaron datos para actualizar"}), 400
    
    usuarios.actualizar_usuario(id, nombre, email)
    
    return jsonify({"mensaje": "Usuario actualizado correctamente"})

@app.route('/eliminar_usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    if usuarios.obtener_usuario(id):
        usuarios.eliminar_usuario(id)
        return jsonify({"mensaje": "Usuario eliminado correctamente"})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

# Ruta para autenticación
@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.json.get("email")
    password = request.json.get("password")
    
    if not email or not password:
        return jsonify({"mensaje": "Email y contraseña son obligatorios"}), 400
    
    usuario = usuarios.obtener_usuarios()
    for user in usuario:
        if user[2] == email:  # Suponiendo que la posición del correo es la tercera columna
            hashed_password = hash_password(password)
            if user[3] == hashed_password:  # Comparando hash con el almacenado
                return jsonify({"mensaje": "Autenticación exitosa"})
    
    return jsonify({"mensaje": "Correo o contraseña incorrectos"}), 401

if __name__ == '__main__':
    app.run(debug=True)
