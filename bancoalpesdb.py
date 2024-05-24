import mysql.connector
from mysql.connector import errorcode

try:
    dataBase = mysql.connector.connect(
        host="localhost",                   # Reemplaza con tu host si es diferente
        user="root",                  # Reemplaza con tu nombre de usuario
        password="password123",           # Reemplaza con tu contraseña
        auth_plugin='mysql_native_password' # Asegúrate de incluir este parámetro
    )
    print("Conexión exitosa")
    
    # Preparar cursor object
    cursorObject = dataBase.cursor()
    
    # Verificar si la base de datos existe
    cursorObject.execute("SHOW DATABASES LIKE 'bancoalpes'")
    result = cursorObject.fetchone()
    
    if result:
        print("La base de datos 'bancoalpes' ya existe.")
    else:
        # Crear base de datos
        cursorObject.execute("CREATE DATABASE bancoalpes")
        print("Base de datos 'bancoalpes' creada con éxito")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está mal con el nombre de usuario o la contraseña")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print(err)

finally:
    if 'dataBase' in locals() and dataBase.is_connected():
        dataBase.close()
        print("Conexión cerrada")
    print("All done!")
