
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class MyLinkedList:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo_nodo

        self.tamano += 1

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamano += 1

    def buscar(self, dato):
        actual = self.cabeza

        while actual is not None:
            if actual.dato == dato:
                return True

            actual = actual.siguiente

        return False

    def eliminar(self, dato):
        if self.cabeza is None:
            return False

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1
            return True

        actual = self.cabeza

        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                self.tamano -= 1
                return True

            actual = actual.siguiente

        return False

    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("La lista esta vacia")
            return

        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("None")

    def obtener_tamano(self):
        return self.tamano
