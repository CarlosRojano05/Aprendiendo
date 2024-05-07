import mysql.connector

class conexionMysql:
    def __init__(self):
     self.mibasededatos = mysql.connector.connect(
         host = "localhost",
         port = "3306",
         user = "root",
         password = "",
         database = "prueba"    
     )
     
     self.conexion = self.mibasededatos
     self.cursor = self.conexion.cursor()
     
     #el condigo a continuación NO es obligación, este contigo solo es para
     #confirmar la coneccion con la base de datos. 
     
     if self.mibasededatos.is_connected():
        db_Info = self.mibasededatos.get_server_info()
        print("connected to MySQL server version: ", db_Info)
        
     #codigo de cierre de conexion
     
     def cerrar_conexion(self):
         self.cursor.close()
         self.conexion.close()
         
           