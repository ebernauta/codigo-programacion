import time, pymysql

def main():
    
    conexion= pymysql.Connection(host="localhost",user="root",db="datos_usuarios")
    cursor = conexion.cursor()
    flag = True
    while flag == True:
        tabla = print('''
        +----------MENU-------------+
        | 1. Lista de usuarios      |
        | 2. Agregar usuario        |
        | 3. Modificar usuario      |
        | 4. Eliminar usuario       |
        | 5. Buscar usuario         |
        | 0. Fin                    |
        +---------------------------+
                    ''')
            
        def listaDeUsuarios():
            consulta = "SELECT * FROM usuarios"
            cursor.execute(consulta)
            usuarios = cursor.fetchall()
            for fila in usuarios:
                usuarios.append(fila[0])
                print(usuarios)        
                
            print(f'''
        +--------------Lista de usuarios-----------+
        |                                          |
        |                                          |
        |                                          |
        |                                          |
        |                                          |
        |                                          |                                         
        |                                          | 
        +------------------------------------------+
                    ''')
            time.sleep(5)
        
        def agregarUsuario():
            try:
                rut = str(input("Ingrese el rut:\n"))
                email = str(input("Ingrese el email:\n"))
                nombre = str(input("Ingrese el nombre:\n"))
                contraseña = int(input("Ingrese la contraseña:\n"))
                fechaIngreso = str(input("Ingrese la fecha de ingreso:\n"))
                sql = "INSERT INTO usuarios (RUT, EMAIL, NOMBRE, CONTRASEÑA, FECHA_INGRESO) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(rut,email,nombre,contraseña,fechaIngreso)
                cursor.execute(sql)
                conexion.commit()
                print("Usuario agregado correctamente")
                time.sleep(3)
                return main()
            except:
                print("ALGO SALIO MAL !")
                time.sleep(2)
                return agregarUsuario()
        
        def modificarUsuario():
            return
        
        def eliminarUsuario():
            rut = str(input("Ingrese el rut que desea eliminar:\n"))
            sql = "DELETE FROM usuarios WHERE usuarios.RUT = "+rut+"; "
            cursor.execute(sql)
            conexion.commit()
            print("Usuario eliminado correctamente")

        def buscarUsuario():
            rut = str(input("Ingrese el rut que desea buscar:\n"))
            sql = "SELECT RUT, EMAIL, NOMBRE, CONTRASEÑA, FECHA_INGRESO FROM usuarios WHERE usuarios.rut = "+rut+";"
            cursor.execute(sql)
            conexion.commit()
            
                
        eleccion = int(input("Ingrese una eleccion:\n"))
        #Dentro de la opcion de agregar usuario se hará una tabla donde cada vez 
        #Que se rellena un dato de un usuario se vaya mostrando 
        #en la consola para ser mas interactiva 
        if eleccion == 1:
            return listaDeUsuarios()
        elif eleccion == 2:
            return agregarUsuario()
        elif eleccion == 3:
            print("Estas dentro de la eleccion 3")
        elif eleccion == 4:
            return eliminarUsuario()
        elif eleccion == 5:
            print("Estas dentro de la eleccion 5")
        elif eleccion == 0:
            print("Fin del codigo...")
            time.sleep(2)
            break
        else:
            print("Eleccion de menú fuera de rango")
            time.sleep(2)
            return main()   
        
main()