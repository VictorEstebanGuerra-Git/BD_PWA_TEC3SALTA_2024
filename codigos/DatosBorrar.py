#esta parte sirve para eliminar los datos de las entidades de la bd, por cualquier cosa
import mysql.connector

conexion = mysql.connector.connect(
    host='#',
    database='#',
    port = 1,
    user = '#',
    password = '#'
)

cursor = conexion.cursor()

consulta = "DELETE FROM `materias`"
 
cursor.execute(consulta)
    
conexion.commit()

cursor.close()
conexion.close()

print("datos falsos borrados")