from ConexionBasededatos import conexionMysql

class Modelproductos:
    def __init__(self):
     self.mibasededatos = conexionMysql() 
     self.conexion = self.mibasededatos.conexion
     self.cursor = self.mibasededatos.cursor
     
    def obtener_conexion(self):
        return self.mibasededatos
    
    def obtener_producto(self, id):
        self.cursor.execute("SELECT * FROM productos WHERE id = %s",(id,))
        return self.cursor.fetchone()
    
    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()
    
    def insertar_producto(self, nombre, precio):
        val = (nombre, precio)
        sql = "INSERT INTO productos (nombre, precio) VALUES (%s, %s)"
        self.cursor.execute(sql, val)
        self.conexion.commit()
        
    def actualizar_producto(self, id, nombre, precio):
        val = (nombre, precio, id)
        sql = "UPDATE productos SET nombre = %s, precio = %s WHERE id = %s"
        self.cursor.execute(sql, val)
        self.conexion.commit()   
        
    def eliminar_producto(self, id):
        val = (id,) 
        sql = "DELETE FROM productos WHERE id = %s"
        self.cursor.execute(sql, val)
        self.conexion.commit()
