from module.colores import Temas
import module.ruta_carpeta_code as rc_code
import module.imagenes as img

from tkinter import font
from tkinter import ttk
import tkinter as tk

import os, string

'''
ruta_c_code = str
ventana = object
panel_de_comandos = object
espacio_de_trabajo = object
pie_de_pagina = object
'''
class VentanaInicio:
    def __init__(self,ancho,alto):
        self.ruta_c_code = rc_code.obtener_ruta_carpeta_code()

        self.fuente = "Ubuntu Mono"

        self.ventana = tk.Tk()

        self.ventana.title("documenta.")
        self.ventana.geometry(f"{ancho}x{alto}")
        self.ventana.minsize(self.menos_un_cuarto(ancho), self.menos_un_cuarto(alto))

        ruta_icon = os.path.join(self.ruta_c_code,"icons","icon-color.png")
        cargar_icon = tk.PhotoImage(file = ruta_icon)
        self.ventana.iconphoto(True, cargar_icon)

        #crear malla en la ventana principal
        for y in range(3):
            if y == 1:
                self.ventana.grid_rowconfigure(y, weight=1)
            else:
                self.ventana.grid_rowconfigure(y, weight=0)
        for x in range(1):
            self.ventana.grid_columnconfigure(x, weight=1)

        self.tema = Temas()

        self.crear_menu_bar()
        self.obtener_fuentes()
        self.crear_panel_de_comandos()
        self.crear_espacio_de_trabajo()
        self.crear_pie_de_pagina()
        self.actualizar_tema()

    def menos_un_cuarto(self,num):
        return int(num-(num/4))

    def mainloop(self):
        self.ventana.mainloop()

    def crear_menu_bar(self):
        self.lista_elementos_panel = []
        self.lista_elementos_trabajo = []
        self.lista_elementos_pie = []

        self.menu_bar = tk.Menu(self.ventana)
        self.ventana.config(menu = self.menu_bar)

        self.archivo_menu = tk.Menu(self.menu_bar, tearoff=0)
        # self.archivo_menu.add_command(label="Abrir")
        # self.archivo_menu.add_command(label="Guardar")
        # self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.ventana.quit)

        self.temas_menu = tk.Menu(self.menu_bar, tearoff=0)
        for posicion, tema in enumerate(self.tema.consultar_lista_temas()):
            nombre = tema["nombre"]
            self.temas_menu.add_command(label=nombre, command=lambda id_tema=posicion:self.actualizar_tema(id_tema))

        self.menu_bar.add_cascade(label="Sistema", menu=self.archivo_menu)
        self.menu_bar.add_cascade(label="Temas", menu=self.temas_menu)

    def crear_panel_de_comandos(self):
        # ancho_malla = 26
        # alto_malla = 2
        ancho_celda, alto_celda = 40, 40
        ubicacion = self.ventana
        pos_x, pos_y = 0, 0
        
        self.fondo_panel = CrearObjTk.crear_labelframe_con_malla(1,1,1,1,ubicacion,pos_x,pos_y,"","new")
        self.lista_elementos_panel.append(self.fondo_panel)

        self.panel_de_comandos = CrearObjTk.crear_frame_con_malla(4,1,ancho_celda,alto_celda,self.fondo_panel,0,0,"nw",False)
        self.lista_elementos_panel.append(self.panel_de_comandos)

        # Formato
        self.p_formato = CrearObjTk.crear_labelframe_con_malla(11,2,ancho_celda,alto_celda,self.panel_de_comandos,0,0,"Formato","nsew",True)
        self.lista_elementos_panel.append(self.p_formato)
        tx_fuentes = CrearObjTk.crear_label_en_malla("Fuentes",self.fuente,self.p_formato,0,0,2)
        tx_tamaño = CrearObjTk.crear_label_en_malla("Tamaño",self.fuente,self.p_formato,1,0,2)

        self.combo_fuentes = ttk.Combobox(self.p_formato, values=self.lista_fuentes)
        self.combo_fuentes.grid(row=0, column=2, columnspan=4, sticky="nsew", padx=4, pady=4)# rowspan=exp_y,
        self.combo_fuentes.bind("<<ComboboxSelected>>", lambda event:self.actualizar_fuente())

        self.boton_n = CrearObjTk.crear_boton_en_malla("N",self.fuente,self.p_formato,0,6)
        self.lista_elementos_trabajo.append(self.boton_n)
        self.boton_k = CrearObjTk.crear_boton_en_malla("k",self.fuente,self.p_formato,1,6)
        self.lista_elementos_trabajo.append(self.boton_k)
        self.boton_cita = CrearObjTk.crear_boton_en_malla("cita",self.fuente,self.p_formato,0,7,2)
        self.lista_elementos_trabajo.append(self.boton_cita)
        self.boton_m_code = CrearObjTk.crear_boton_en_malla("m code",self.fuente,self.p_formato,0,9,2)
        self.lista_elementos_trabajo.append(self.boton_m_code)
        self.boton_separador = CrearObjTk.crear_boton_en_malla("separador",self.fuente,self.p_formato,1,7,4)
        self.lista_elementos_trabajo.append(self.boton_separador)

        # Lista
        self.p_lista = CrearObjTk.crear_labelframe_con_malla(1,2,ancho_celda,alto_celda,self.panel_de_comandos,0,1,"Lista","nsew",True)
        self.lista_elementos_panel.append(self.p_lista)

        self.boton_lista_no_ordenada = CrearObjTk.crear_boton_en_malla("•",self.fuente,self.p_lista,0,0)
        self.lista_elementos_trabajo.append(self.boton_lista_no_ordenada)
        self.boton_lista_ordenada = CrearObjTk.crear_boton_en_malla("1.",self.fuente,self.p_lista,1,0)
        self.lista_elementos_trabajo.append(self.boton_lista_ordenada)

        # Insertar
        self.p_insertar = CrearObjTk.crear_labelframe_con_malla(6,2,ancho_celda,alto_celda,self.panel_de_comandos,0,2,"Insertar","nsew",True)
        self.lista_elementos_panel.append(self.p_insertar)

        self.boton_img = CrearObjTk.crear_boton_en_malla("img",self.fuente,self.p_insertar,0,0,2,2)
        self.lista_elementos_trabajo.append(self.boton_img)
        self.boton_link = CrearObjTk.crear_boton_en_malla("link",self.fuente,self.p_insertar,0,2,2,2)
        self.lista_elementos_trabajo.append(self.boton_link)
        self.boton_code = CrearObjTk.crear_boton_en_malla("code",self.fuente,self.p_insertar,0,4,2,2)
        self.lista_elementos_trabajo.append(self.boton_code)

        # Tablas
        self.p_tabla = CrearObjTk.crear_labelframe_con_malla(2,2,ancho_celda,alto_celda,self.panel_de_comandos,0,3,"Tablas","nsew",True)
        self.lista_elementos_panel.append(self.p_tabla)

        self.boton_img = CrearObjTk.crear_boton_en_malla("Tablas",self.fuente,self.p_tabla,0,0,2,2)
        self.lista_elementos_trabajo.append(self.boton_img)

    def crear_espacio_de_trabajo(self):
        ancho_malla = 2
        alto_malla = 1
        # ancho_celda = int(self.ventana.winfo_width()) / 2
        # alto_celda = int(self.ventana.winfo_height()) - 60
        ancho_celda = 1
        alto_celda = 1
        ubicacion = self.ventana
        pos_x, pos_y = 1, 0

        self.espacio_de_trabajo = CrearObjTk.crear_labelframe_con_malla(ancho_malla,alto_malla,ancho_celda,alto_celda,ubicacion,pos_x,pos_y)
        self.lista_elementos_trabajo.append(self.espacio_de_trabajo)

        self.edit = CrearObjTk.crear_area_texto_en_malla(self.espacio_de_trabajo,self.fuente,0,0)

        self.lista_elementos_trabajo.append(self.edit)
        fuente_edit = self.edit.cget("font")
        fuente_edit = fuente_edit[fuente_edit.find("{")+1:fuente_edit.find("}")]
        self.combo_fuentes.set(fuente_edit)

    def crear_pie_de_pagina(self):
        ancho_malla = 3
        alto_malla = 1
        ancho_celda = int(self.ventana.winfo_width())
        alto_celda = 20
        ubicacion = self.ventana
        pos_x, pos_y = 2, 0

        self.pie_de_pagina = CrearObjTk.crear_labelframe_con_malla(ancho_malla,alto_malla,ancho_celda,alto_celda,ubicacion,pos_x,pos_y,"","sew")
        self.lista_elementos_pie.append(self.pie_de_pagina)

        ruta_m_agua = os.path.join(self.ruta_c_code,"icons","documenta-marca-de-agua-color.png")
        cargar_m_agua = img.redimencionar_img_ajust_alto(ruta_m_agua,20)
        self.m_agua = tk.Label(self.pie_de_pagina, image=cargar_m_agua)
        self.m_agua.image = cargar_m_agua
        self.m_agua.grid(row=0,column=1, padx=4, pady=4)
        self.lista_elementos_pie.append(self.m_agua)

        tx_version = CrearObjTk.crear_label_en_malla("Alpha 0.1",self.fuente,self.pie_de_pagina,0,2,1,1,"e")

    def actualizar_tema(self,id_tema=0):
        self.tema.actualizar_tema(id_tema)

        for elemento_tk in self.lista_elementos_panel:
            elemento_tk.config(bg=self.tema.panel)

        for elemento_tk in self.lista_elementos_trabajo:
            elemento_tk.config(bg=self.tema.hoja, fg=self.tema.texto)

        for elemnto_tk in self.lista_elementos_pie:
            elemnto_tk.config(bg=self.tema.pie_pagina)

    def obtener_fuentes(self):
        fuentes_encontradas = list(font.families())
        fuentes_encontradas.sort()

        #variaciones_fuentes= ["Baltic","Black","Bold","CE","CYR","ExtraLight","Greek","Light","Med","Medium","Narrow","Ret","Semib","Semil","SemBd","Semibol","Semibold","Semilig","Semiligh","Semilight","TUR"]

        valor_letra = {}
        lista_letras = list(string.ascii_lowercase)

        for valor, letra in enumerate(lista_letras):
            valor_letra.update({f"{letra}":valor})

        empieza_lista = False
        self.lista_fuentes = []
        fuente_anterior = "a"
        for fuente in fuentes_encontradas:
            if not empieza_lista:
                if fuente[0].lower() == "a":
                    empieza_lista = True
            if empieza_lista and fuente[0].lower() in lista_letras: 
                if fuente == "Ubuntu Mono":
                    self.lista_fuentes.append(fuente)
                elif not (fuente.split()[0] == fuente_anterior) and valor_letra[f"{fuente[0].lower()}"] >= valor_letra[f"{fuente_anterior[0].lower()}"]:
                    self.lista_fuentes.append(fuente)
                    fuente_anterior = fuente.split()[0]

    def actualizar_fuente(self):
        fuente_seleccionada = self.combo_fuentes.get()
        self.edit.config(font=(fuente_seleccionada, 12))

'''
label = object
boton = object
area_texto = object
frame = object
labelframe = object
'''
class CrearObjTk:
    def crear_label_en_malla(texto,fuente,ubicacion,pos_x,pos_y,exp_x=1,exp_y=1,orientacion="nsew"):
        label = tk.Label(ubicacion,text=texto,font=(fuente, 12))
        label.grid(row=pos_x, column=pos_y, columnspan=exp_x, rowspan=exp_y, sticky=orientacion, padx=4, pady=4)
        return label

    def crear_boton_en_malla(texto,fuente,ubicacion,pos_x,pos_y,exp_x=1,exp_y=1):
        boton = tk.Button(ubicacion,text=texto,font=(fuente, 12))# command=lambda:funcion, command=a
        boton.grid(row=pos_x, column=pos_y, columnspan=exp_x, rowspan=exp_y, sticky="nsew", padx=4, pady=4)
        return boton

    def crear_area_texto_en_malla(ubicacion,fuente,pos_x,pos_y):
        area_texto = tk.Text(ubicacion, font=(fuente, 12), padx=10, pady=10, width=1, height=1)
        area_texto.grid(row=pos_x, column=pos_y, sticky="nsew")
        return area_texto

    def crear_frame_con_malla(ancho_malla,alto_malla,ancho_celda,alto_celda,ubicacion,pos_x,pos_y,sticky="nsew",malla_flexible=True):
        frame = tk.Frame(ubicacion)
        frame.grid(row=pos_x, column=pos_y, sticky=sticky)

        flexibilidad_malla = 1
        if not malla_flexible:
            flexibilidad_malla = 0

        for x in range(ancho_malla):
            frame.grid_columnconfigure(x, weight=flexibilidad_malla, minsize=ancho_celda)
        for y in range(alto_malla):
            frame.grid_rowconfigure(y, weight=flexibilidad_malla, minsize=alto_celda)

        return frame

    def crear_labelframe_con_malla(ancho_malla,alto_malla,ancho_celda,alto_celda,ubicacion,pos_x,pos_y,texto="",sticky="nsew",margen=False):
        labelframe = tk.LabelFrame(ubicacion, text=texto)
        labelframe.grid(row=pos_x, column=pos_y, sticky=sticky)

        if margen:
            labelframe.grid(padx=4, pady=4)

        flexibilidad_malla = 1
        if texto != "":
            flexibilidad_malla = 0

        for x in range(ancho_malla):
            labelframe.grid_columnconfigure(x, weight=flexibilidad_malla, minsize=ancho_celda)
        for y in range(alto_malla):
            labelframe.grid_rowconfigure(y, weight=flexibilidad_malla, minsize=alto_celda)

        return labelframe