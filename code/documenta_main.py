from module.controlador import VentanaInicio
from module.fuentes import Fuentes

ancho = 1040
alto = 680

controlador_fuentes = Fuentes()
controlador_fuentes.crear_fuentes()

ventana = VentanaInicio(ancho,alto)
ventana.mainloop()

controlador_fuentes.eliminar_fuentes()