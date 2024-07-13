'''
Autor: Ramiro Sebastian Gaspar
Fecha: 27/06/2024
Proyecto: PWA ETT 3139 GRAL Martin Miguel de Guemes
Institucion: E.E.T 3139 Gral. M.M de Guemes, Salta Capital

Proposito: Este programa de python convierte los cuatro excel de el codigo CrearExcel.py  a archivos JSON
Asi la bd puede almacenar ese tipo de dato. El sistema de como se realiza la subida de datos falsos y de la modificacion
de los excels y JSON no esta en su version final, pero es para terminar de hacer pruebas y deja la base de datos lista

Notas: IMPORTANTE, tienen que verificar la ruta de los archivos para su uso en esto codigo. Debido a que todas las rutas
que tengo en este codigo son rutas de mi equipo.

Se tiene que instalar la siguiente libreria:
pip install pandas

''' 
# Se importan las librerias
import os
import pandas as pd


def excel_to_json(ruta_excel, ruta_json):
    try:
        # Cargar el archivo Excel en un DataFrame
        df = pd.read_excel(ruta_excel)

        # Convertir DataFrame a formato JSON y guardar en un archivo
        df.to_json(ruta_json, orient='records')

        print(f"Archivo JSON generado correctamente: {ruta_json}")
    
    except Exception as e:
        print(f"Error al convertir Excel a JSON: {e}")

# Ejemplo de uso para cada archivo Excel y JSON correspondiente con rutas completas
# ACORDARSE DE VERIFICAR LA RUTA
ruta_Trimestre1_excel = r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\Excels\Trimestre1.xlsx"
ruta_Trimestre1_json = r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\JSON\Trimestre1.json"
excel_to_json(ruta_Trimestre1_excel, ruta_Trimestre1_json)

ruta_Trimestre2_excel = r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\Excels\Trimestre2.xlsx"
ruta_Trimestre2_json = r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\JSON\Trimestre2.json"
excel_to_json(ruta_Trimestre2_excel, ruta_Trimestre2_json)

ruta_Trimestre3_excel = r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\Excels\Trimestre3.xlsx"
ruta_Trimestre3_json = r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\JSON\Trimestre3.json"
excel_to_json(ruta_Trimestre3_excel, ruta_Trimestre3_json)

ruta_recuperacion_excel = r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\Excels\Recuperacion.xlsx"
ruta_recuperacion_json = r"C:\Users\Usuario\Desktop\BD_PWA_ETT3139 Salta_2024\JSON\Recuperacion.json"
excel_to_json(ruta_recuperacion_excel, ruta_recuperacion_json)

