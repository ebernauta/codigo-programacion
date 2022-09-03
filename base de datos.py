import pymysql, time

def EjecutarConexion():
    conexion = pymysql.Connection(host="localhost",user="root",password="",db="mysql")
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS datos_usuarios")
    conexion.close()
    conexion= pymysql.Connection(host="localhost",user="root",db="datos_usuarios")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios (RUT INT(11) PRIMARY KEY,  EMAIL VARCHAR(40), NOMBRE VARCHAR(30), CONTRASEÑA INT(8), FECHA_INGRESO datetime )")
    conexion.commit()
    conexion.close()
    
    print("""
          +-----------------------------------+
          |                                   |
          |                                   |
          | D A T A  B A S E  C O N E C T E D |
          |                                   |
          |                                   |
          +-----------------------------------+
          
          """)
    
    time.sleep(3)

EjecutarConexion()