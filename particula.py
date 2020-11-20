from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id=0, origenx=0, origeny=0, destinox=0, destinoy=0, velocidad=0, red=0, green=0, blue=0, distancia=0):
        self.__id = id
        self.__origenx = origenx
        self.__origeny = origeny
        self.__destinox = destinox
        self.__destinoy = destinoy
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.distancia = distancia_euclidiana(origenx, destinox, origeny, destinoy)

    def __str__(self):
        return(
            'ID: ' + str(self.__id) + '\n' +
            'Origen x: ' + str(self.__origenx) + '\n' +
            'Origen y: ' + str(self.__origeny) + '\n' +
            'Destino x: ' + str(self.__destinox) + '\n' +
            'Destino y: ' + str(self.__destinoy) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.distancia) + '\n'
        )
    
    def __lt__(self, other):
        return self.id < other.id

    @property
    def id(self):
        return self.__id

    @property
    def origenx(self):
        return self.__origenx

    @property
    def origeny(self):
        return self.__origeny

    @property
    def destinox(self):
        return self.__destinox

    @property
    def destinoy(self):
        return self.__destinoy

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    def to_dict(self):
        return{
            "id": self.__id,
            "origenx": self.__origenx,
            "origeny": self.__origeny,
            "destinox": self.__destinox,
            "destinoy": self.__destinoy,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
