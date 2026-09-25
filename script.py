import datetime
import os
import requests

# Configuración: Reemplaza con tu enlace directo al archivo .xlsx
URL_EXCEL = "https://geoportalgasolineras.es/resources/files/preciosEESS_es.xls"

def descargar_copia_excel():
    try:
        # Generar el nombre del archivo con la fecha de hoy (Ej: copia_2026-09-25.xlsx)
        fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")
        nombre_archivo = f"copia_{fecha_hoy}.xlsx"
        
        # Crear carpeta de copias si no existe
        os.makedirs("copias_excel", exist_ok=True)
        ruta_guardado = os.path.join("copias_excel", nombre_archivo)
        
        print(f"Descargando archivo desde {URL_EXCEL}...")
        respuesta = requests.get(URL_EXCEL, timeout=30)
        
        # Verificar que la descarga fue exitosa (código 200)
        if respuesta.status_code == 200:
            with open(ruta_guardado, "wb") as f:
                f.write(respuesta.content)
            print(f"¡Éxito! Archivo guardado como: {ruta_guardado}")
        else:
            print(f"Error al descargar. Código de estado: {respuesta.status_code}")
            
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    descargar_copia_excel()
