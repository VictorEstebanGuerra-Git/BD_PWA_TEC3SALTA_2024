import mysql.connector
import json

# Configuración de la conexión a la base de datos
mydb = mysql.connector.connect(
  host="#",
  user="#",
  password="#",
  database="#",
  port = 1
)

# Función para leer el contenido de un archivo JSON
def leer_json(ruta_json):
    with open(ruta_json, 'r') as file:
        contenido = file.read()
        return contenido

# Rutas de los archivos JSON que deseas cargar
rutas_json = {
    'trimestre1': r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\JSON\Trimestre1.json",
    'trimestre2': r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\JSON\Trimestre2.json",
    'trimestre3': r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\JSON\Trimestre3.json",
    'recuperacion': r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\JSON\Recuperacion.json"
}

# Leer y preparar los contenidos de los archivos JSON
contenidos_json = {}
for key, ruta_json in rutas_json.items():
    contenidos_json[key] = leer_json(ruta_json)

# Consultas SQL para actualizar cada atributo JSON
sql_trimestre1 = "UPDATE notas SET trimestre1notas = %s"
sql_trimestre2 = "UPDATE notas SET trimestre2notas = %s"
sql_trimestre3 = "UPDATE notas SET trimestre3notas = %s"
sql_recuperacion = "UPDATE notas SET notasrecuperacion = %s"

# Ejecutar cada consulta con el contenido del JSON
cursor = mydb.cursor()
cursor.execute(sql_trimestre1, (contenidos_json['trimestre1'],))
cursor.execute(sql_trimestre2, (contenidos_json['trimestre2'],))
cursor.execute(sql_trimestre3, (contenidos_json['trimestre3'],))
cursor.execute(sql_recuperacion, (contenidos_json['recuperacion'],))
mydb.commit()

print("Archivos JSON subidos correctamente")

# Cerrar la conexión
mydb.close()
