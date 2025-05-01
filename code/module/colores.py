'''
Default - https://www.colorhunt.co/palette/ffa725fff5e4c1d8c36a9c89
Color - https://www.colorhunt.co/palette/ff7f3efff6e980c4e9604cc3
Claro - https://www.colorhunt.co/palette/f8fafcd9eafdbcccdc9aa6b2
Oscuro - https://www.colorhunt.co/palette/404258474e6850577a6b728e

extra
Oficina - https://www.colorhunt.co/palette/161a3031304db6bbc4f0ece5
Madera - https://www.colorhunt.co/palette/3936464f45576d5d6ef4eee0
'''

'''
panel = str
hoja = str
extra = str
pie_pagina = str
texto = str
tema_defecto = dict
tema_claro = dict
tema_oscuro = dict
tema_color = dict
tema_oficiona = dict
lista_temas = list
'''
class Temas:
    def __init__(self):
        self.panel = ""
        self.hoja = ""
        self.extra = ""
        self.pie_pagina = ""
        self.texto = ""
        self.crear_dic_temas()
        self.actualizar_tema(0)

    def actualizar_tema(self,id_tema=0):
        self.panel = (self.lista_temas[id_tema])["panel"]
        self.hoja = (self.lista_temas[id_tema])["hoja"]
        self.extra = (self.lista_temas[id_tema])["extra"]
        self.pie_pagina = (self.lista_temas[id_tema])["pie_pagina"]
        self.texto = (self.lista_temas[id_tema])["texto"]

    def crear_dic_temas(self):        
        #0
        self.tema_defecto = {
            "nombre": "Predeterminado",
            "panel": "#FFA725",
            "hoja": "#FFF5E4",
            "extra": "#C1D8C3",
            "pie_pagina": "#6A9C89",
            "texto": "#000000"
        }
        #1
        self.tema_claro = {
            "nombre": "Claro",
            "panel": "#BCCCDC",
            "hoja": "#F8FAFC",
            "extra": "#D9EAFD",
            "pie_pagina": "#9AA6B2",
            "texto": "#000000"
        }
        #2
        self.tema_oscuro = {
            "nombre": "Oscuro",
            "panel": "#404258",
            "hoja": "#6B728E",
            "extra": "#50577A",
            "pie_pagina": "#474E68",
            "texto": "#ffffff"
        }
        #3
        self.tema_color = {
            "nombre": "Color",
            "panel": "#FF7F3E",
            "hoja": "#FFF6E9",
            "extra": "#80C4E9",
            "pie_pagina": "#604CC3",
            "texto": "#000000"
        }
        #4
        self.tema_oficiona = {
            "nombre": "Oficina",
            "panel": "#31304D",
            "hoja": "#F0ECE5",
            "extra": "#B6BBC4",
            "pie_pagina": "#161A30",
            "texto": "#000000"
        }

        self.lista_temas = [self.tema_defecto,
                            self.tema_color,
                            self.tema_claro,
                            self.tema_oscuro,
                            self.tema_oficiona
                            ]

    def consultar_lista_temas(self):
        return self.lista_temas