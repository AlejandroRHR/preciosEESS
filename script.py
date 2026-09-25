import datetime
import os
import requests

# REEMPLAZA ESTE ENLACE POR EL TUYO:
URL_EXCEL = "https://geoportalgasolineras.es/resources/files/preciosEESS_es.xls"

def descargar_copia_excel():
    try:
        fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")
        nombre_archivo = f"copia_{fecha_hoy}.xlsx"
        
        os.makedirs("copias_excel", exist_ok=True)
        ruta_guardado = os.path.join("copias_excel", nombre_archivo)
        
        print(f"Descargando archivo desde {URL_EXCEL}...")
        respuesta = requests.get(URL_EXCEL, timeout=30)
        
        if respuesta.status_code == 200:
            with open(ruta_guardado, "wb") as f:
                f.write(respuesta.content)
            print(f"¡Éxito! Archivo guardado como: {ruta_guardado}")
        else:
            print(f"Error al descargar. Código: {respuesta.status_code}")
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    descargar_copia_excel()
