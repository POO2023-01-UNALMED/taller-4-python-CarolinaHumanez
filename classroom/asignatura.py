class Asignatura:

    def __init__(self, nombre, salon="Remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        cadena=self._nombre+" "+self._salon
        return cadena

    # def __str__(self):
    #     pass
