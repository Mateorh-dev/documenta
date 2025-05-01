import os

def obtener_ruta_carpeta_code():
    ruta_carpeta_principal = os.path.dirname(os.getcwd())
    if not "code" in ruta_carpeta_principal.split(os.path.sep):
        ruta_carpeta_principal = os.path.join(ruta_carpeta_principal, "code")
    return ruta_carpeta_principal