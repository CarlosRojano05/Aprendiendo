import mysql.connector

class ConexionMysql:
    def __init__(self):
        self.mibasededatos = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="bd_usuarios"    
        )
        
        self.conexion = self.mibasededatos
        self.cursor = self.conexion.cursor()
        
        if self.mibasededatos.is_connected():
            db_info = self.mibasededatos.get_server_info()
            print("Conectado a MySQL Server versión:", db_info)
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()