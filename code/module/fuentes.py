import module.ruta_carpeta_code as rc_code
import os, platform, ctypes

'''
ruta_c_code = str
sistema_operativo = str
lista_fuentes_mono = list
'''
class Fuentes:
    def __init__(self):
        self.ruta_c_code = rc_code.obtener_ruta_carpeta_code()

        self.lista_fuentes_mono =["UbuntuMono-Regular.ttf",
                                  "UbuntuMono-Italic.ttf",
                                  "UbuntuMono-Bold.ttf",
                                  "UbuntuMono-BoldItalic.ttf"]

        self.sistema_operativo = str(platform.system()).lower()
        '''
        'Linux', 'Darwin'(macOS), 'Java', 'Windows'
        '''

    def crear_fuentes(self):
        if self.sistema_operativo == "windows":
            for fuente in self.lista_fuentes_mono:
                ctypes.windll.gdi32.AddFontResourceW(os.path.join(self.ruta_c_code,"fonts","Ubuntu_Mono",fuente))

    def eliminar_fuentes(self):
        if self.sistema_operativo == "windows":
            for fuente in self.lista_fuentes_mono:
                ctypes.windll.gdi32.RemoveFontResourceW(os.path.join(self.ruta_c_code,"fonts","Ubuntu_Mono",fuente))