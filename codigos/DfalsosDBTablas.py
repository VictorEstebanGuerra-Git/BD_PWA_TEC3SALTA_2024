'''
Autor: Ramiro Sebastian Gaspar
Fecha: 30/05/2024
Proyecto: PWA ETT 3139 GRAL Martin Miguel de Guemes
Institucion: E.E.T 3139 Gral. M.M de Guemes, Salta Capital
    
Proposito: Este codigo se realizo con la idea de rellenar 8 tablas de la base de datos y pasarsela al equipo de testing para
que la saturen con la cantidad de datos que quieran y realizar sus pruebas. Ademas que a futuro se va a utilizar para
hacer pruebas con una PWA basica y tener datos falsos primeramente para despues pasar a datos reales, pero eso ya seria
a futuro. Este programa llena la base de datos casi en su totalidad pero algunos datos especificos como puede ser la
firma digital no los realiza. 

Notas: Solo se llenan 8 tablas debido a que hay 2 tablas que contienen atributos que contienen archivos excel y se decidio
que se le va hacer un codigo aparte para llenarlo con datos falsos.

Para utilizar este codigo se necesita la instalacion de mysql connector, que se descarga mediante comando pip en
Windows:
    pip install mysql-connector-python
Y las otras librerias:
    pip install faker

Este codigo no se probo en otros sistemas operativos.

Los cambios que se tienen que realizar para la prueba son en la parte de conexion con la bd, donde se pone el servidor local
que tengan asignado en su entorno y despues ponen los otros datos como el nombre del usuario, contraseña, nombre de la db y
el puerto. Es importante que controlen que la bd que se les paso tiene todo los nombres de las tablas y atributos iguales
que en este codigo, debido a que se estuvo actualizando constantemente la bd y puede haber diferencias en los nombres

'''

#antes de usar este codigo se tiene que instalar la librerias de mysql y de faker
#esto se hace en la terminal poniendo pip y el nombre de la libreria

import mysql.connector
import random
import pandas as pd
import datetime
from faker import Faker

fake = Faker()

# Variables que guardan datos especificos para algunas entidades
rol_dyp = ["Directivo", "Preceptor"]
palabras_de_dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
palabras_de_turno = ["mañana', 'tarde', 'nocturno"]
numeros_de_cursos = [1,2,3,4]
numeros_de_division = [1,2,3,4]
palabras_de_ciclo = ["ciclo superior", "ciclo basico"]
estado_de_asistencias = ["presente", "ausente", "tarde"]
palabras_de_notas = ["trabajo practico","tarea", "evaluacion","recuperacion"]


# Este es un random choice que se va a utilizar en la tabla de curso
curso = random.choice(numeros_de_cursos)
division = random.choice(numeros_de_division)
ciclo = random.choice(palabras_de_ciclo)

# Conexion con la BD
conexion = mysql.connector.connect(
    host='#',
    database='#',
    port=1,
    user='#',
    password='#'
)

cursor = conexion.cursor()


# Cada atributo de las tablas se va a rellenar con 50 datos en cada atributo
for _ in range(50):

# Entidad docentes
    dni_docentes = fake.random_number(digits=8)
    nombre_docentes = fake.first_name()
    apellido_docentes = fake.last_name()
    correo_docentes = fake.email()
    telefono1_docentes = fake.phone_number()
    contraseña_docentes = fake.password()
    firma_docentes = None

    consulta = "INSERT INTO `docentes` (dni, nombre, apellido, correo, telefono, contraseña, firma) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (dni_docentes, nombre_docentes, apellido_docentes, correo_docentes, telefono1_docentes, contraseña_docentes, firma_docentes)

    cursor.execute(consulta, valores)

# Entidad materias
    ID_materias = fake.random_number(digits=3)
    nombre_materias = fake.word()

    consulta2 = "INSERT INTO `materias` (id, nombre, docentes_dni) VALUES (%s, %s, %s)"
    valores2 = (ID_materias, nombre_materias, dni_docentes)

    cursor.execute(consulta2, valores2)
    
# Entidad directivos_preceptores
    dni_directivos_p = fake.random_number(digits=8)
    nombre_directivos_p = fake.first_name()
    apellido_directivos_p = fake.last_name()
    correo_directivos_p = fake.email()
    telefono1_directivos_p = fake.phone_number()
    contraseña_directivos_p = fake.password()
    firma_directivos_p = None
    rol_directivos_p = random.choice(rol_dyp)
    
    consulta3 ="INSERT INTO 'directivos_preceptores' (dni, nombre, apellido, correo, telefono, contraseña, firma, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores3 = (dni_directivos_p, nombre_directivos_p, apellido_directivos_p, correo_directivos_p, telefono1_directivos_p, contraseña_directivos_p, firma_directivos_p, rol_directivos_p)

    cursor.execute(consulta3,valores3)
    
# Entidad padres_tutores
    dni_padres_tutores = fake.random_number(digits=8)
    nombre_padres_tutores = fake.first_name()
    apellido_padres_tutores = fake.last_name()
    correo_padres_tutores = fake.email()
    telefono1_padres_tutores = fake.phone_number()
    telefono2_padres_tutores = fake.phone_number()
    contraseña_padres_tutores = fake.password()
    firma_padres_tutores = None
    
    consulta4 = "INSERT INTO 'padres_tutores' (dni, nombre, apellido, correo, telefono1, telefono2, contraseña, firma) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores4 = (dni_padres_tutores, nombre_padres_tutores, apellido_padres_tutores, correo_padres_tutores, telefono1_padres_tutores, telefono2_padres_tutores, contraseña_padres_tutores, firma_padres_tutores)
    
    cursor.execute(consulta4, valores4)
 
# Entidad alumnos
    dni_alumnos = fake.random_number(digits=8)
    nombre_alumnos = fake.first_name()
    apellido_alumnos = fake.last_name()
    correo_alumnos = fake.email()
    telefono1_alumnos = fake.phone_number()
    contraseña_alumnos = fake.password()
    
    consulta5 = "INSERT INTO 'alumnos' (dni, nombre, apellido, correo, telefono, contraseña, padres_tutores_dni) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores5 = (dni_alumnos, nombre_alumnos, apellido_alumnos, correo_alumnos, telefono1_alumnos, contraseña_alumnos, dni_padres_tutores)
    
    cursor.execute(consulta5, valores5)
    
# Entidad horarios
    ID_horarios = fake.random_number(digits=4)
    dia = random.choice(palabras_de_dias)
    hora_modulo = fake.time()
    turno = random.choice(palabras_de_turno)
    
    consulta6 = "INSERT INTO 'horarios' (id, dia, hora_modulo, turno, materias_id, materias_docentes_dni) VALUES (%s, %s, %s, %s, %s, %s)"
    valores6 = (ID_horarios, dia, hora_modulo, turno, ID_materias, dni_docentes)
    
    cursor.execute(consulta6, valores6)
    
# Entidad curso
    datos_curso = f"{curso} {division} {ciclo}"
    turno = random.choice(palabras_de_turno)
    comunicados = fake.paragraph()
    
    consulta7 = "INSERT INTO 'curso' (ncurso_ndivision_ciclo, turno, comunicados, alumnos_dni, alumnos_padres_tutores_dni, horarios_id, horarios_materias_id, horarios_materias_docentes_dni, directivos_preceptores_dni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores7 = (datos_curso, turno, comunicados, dni_alumnos, dni_padres_tutores, ID_horarios, ID_materias, dni_docentes, dni_directivos_p)
    
    cursor.execute(consulta7, valores7)
    
# Entidad asistencias
    ID_asistencias = fake.random_number(digits=5)
    fecha_asistencias = None #tuve un problema al ejecutar esta linea, todavia no encontre el problema
    estado_asistencias = random.choice(estado_de_asistencias)
    
    consulta8 = "INSERT INTO 'asistencias' (ID, fecha, estado, curso_ncurso_ndivision_ciclo, curso_alumnos_dni, curso_alumnos_padres_tutores_dni, curso_horarios_id, curso_horarios_materias_id, curso_horarios_materias_docentes_dni, curso_directivos_preceptores_dni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores8 = (ID_asistencias, fecha_asistencias, estado_asistencias, datos_curso, dni_alumnos, dni_padres_tutores, ID_horarios, ID_materias, dni_docentes, dni_directivos_p)
    
    cursor.execute(consulta8, valores8)
   
conexion.commit()

cursor.close()
conexion.close()

print("se subieron los datos falsos a la base de datos")