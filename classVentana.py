class Ventana:
    __titulo = ''
    __x_supiz = 0
    __y_supiz = 0
    __x_infder = 0
    __y_infder = 0
    def __init__(self, t, xsi=0, ysi=0, xid=500, yid=500):
        self.__titulo = t
        self.__x_supiz = xsi
        self.__y_supiz = ysi
        self.__x_infder = xid
        self.__y_infder = yid
    def mostrar(self):
        print("Ventana {} | ({},{}) Margen superior Izquiedo - ({},{}) Margen inferior Derecho".format(self.__titulo, self.__x_supiz, self.__y_supiz, self.__x_infder, self.__y_infder))
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__y_supiz + self.__y_infder
    def ancho(self):
        return self.__x_supiz + self.__x_infder
    def moverDerecha(self, mod=1):
        if (self.__x_supiz + mod < 0) or (self.__x_infder + mod > 500):
            print("ERROR: Los valores superan el limite")
        else:
            self.__x_supiz += mod
            self.__x_infder += mod
    def moverIzquierda(self, mod=1):
        if (self.__x_supiz - mod < 0) or (self.__x_infder - mod > 500):
            print("ERROR: Los valores superan los limites")
        else:
            self.__x_supiz -= mod
            self.__x_infder -= mod
    def Bajar(self, mod=1):
        if (self.__y_supiz + mod < 0) or (self.__y_infder + mod > 500):
            print("ERROR: Los valores superan los limites")
        else:
            self.__y_supiz += mod
            self.__y_infder += mod
    def Subir(self, mod=1):
        if (self.__y_supiz - mod < 0) or (self.__y_infder - mod > 500):
            print("ERROR: Los valores superan los limites")
        else:
            self.__y_supiz -= mod
            self.__y_infder -= mod