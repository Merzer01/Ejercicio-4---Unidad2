from classVentana import Ventana

#PROGRAMA A EJECUTAR
if __name__ == '__main__':
    print("====Ventana Inicio====")
    ventanaInicio = Ventana('Inicio')   #constructor
    ventanaInicio.mostrar()             #metodo que muestra los datos
    print("Ventana: {} Alto: {} Ancho: {}".format(ventanaInicio.getTitulo(), ventanaInicio.alto(), ventanaInicio.ancho()))  #metoodos que retornar valores
    print("====Ventana Cargar====")
    ventanaCargar = Ventana('Cargar',10,20) #constructor
    ventanaCargar.mostrar()
    print("***Mueve a la derecha***")
    ventanaCargar.moverDerecha(10)      #metodo que mueve toda la ventana a la derecha
    ventanaCargar.mostrar()
    print("***Mueve a la Izquierda***")
    ventanaCargar.moverIzquierda(10)    #metodo que mueve toda la ventana a la izquierda
    ventanaCargar.mostrar()
    print("***Bajar***")
    ventanaCargar.Bajar(10)             #metodo que mueve toda la ventana hacia abajo
    ventanaCargar.mostrar()
    print("===Ventana Borrar===")
    ventanaBorrar = Ventana('Borrar',10,20,100,200)
    ventanaBorrar.mostrar()
    print("***SUbir***")
    ventanaBorrar.Subir(5)              #metodo que mueve toda la ventana hacia arriba
    ventanaBorrar.mostrar()
    print("***Bajar***")
    ventanaBorrar.Bajar()
    ventanaBorrar.mostrar()


'''
el metodo bajar modifica los (y) aumentando su valor
el metodo subir modifica los (y) disminuyendo su valor

el metodo mover izquierda modifiica los (x) disminuyendo su valor
el metodo mover derecha modifica los (x) aumentando su valor

es necesario validar que  este en los valores iniciales de la ventana
si escede los valores, mediante un while pide ingresar un nuevo valor
'''