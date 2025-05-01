from PIL import Image, ImageTk

def redimencionar_img_ajust_alto(ruta, altura):
    ruta_imagen = Image.open(ruta)
    cargar_imagen = ImageTk.PhotoImage(ruta_imagen)
    
    #obtener las dimensiones de la imagen
    ancho_imagen = cargar_imagen.width()
    alto_imagen = cargar_imagen.height()
    ancho = int((altura*ancho_imagen)/alto_imagen)

    imagen = ruta_imagen.resize((ancho,altura))
    return ImageTk.PhotoImage(imagen)

def redimencionar_img_ajust_ancho(ruta, ancho):
    ruta_imagen = Image.open(ruta)
    cargar_imagen = ImageTk.PhotoImage(ruta_imagen)
    
    #obtener las dimensiones de la imagen
    ancho_imagen = cargar_imagen.width()
    alto_imagen = cargar_imagen.height()
    altura = int((ancho*alto_imagen)/ancho_imagen)

    imagen = ruta_imagen.resize((ancho,altura))
    return ImageTk.PhotoImage(imagen)

def redimencionar_img_anchoxalto(ruta, ancho, altura):
    ruta_imagen = Image.open(ruta)

    imagen = ruta_imagen.resize((ancho,altura))
    return ImageTk.PhotoImage(imagen)