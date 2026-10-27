
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None


class ListaSimple:
    def __init__(self):
        self.inicio = None

    # Mostrar la lista
    def mostrar(self):
        if self.inicio is None:
            print("La lista está vacía")
            return

        actual = self.inicio

        while actual is not None:
            print(actual.info, end=" -> ")
            actual = actual.liga

        print("NIL")

    # Insertar al inicio
    def insertar_inicio(self, info):
        nuevo = Nodo(info)
        nuevo.liga = self.inicio
        self.inicio = nuevo
        print("Nodo insertado al inicio")

    # Insertar al final
    def insertar_final(self, info):
        nuevo = Nodo(info)

        if self.inicio is None:
            self.inicio = nuevo
            print("Nodo insertado al final")
            return

        actual = self.inicio

        while actual.liga is not None:
            actual = actual.liga

        actual.liga = nuevo
        print("Nodo insertado al final")

    # Insertar antes de un valor X
    def insertar_antes(self, x, info):
        if self.inicio is None:
            print("La lista está vacía")
            return

        if self.inicio.info == x:
            self.insertar_inicio(info)
            return

        actual = self.inicio

        while actual.liga is not None and actual.liga.info != x:
            actual = actual.liga

        if actual.liga is None:
            print("No se encontró el valor", x)
            return

        nuevo = Nodo(info)
        nuevo.liga = actual.liga
        actual.liga = nuevo
        print("Nodo insertado antes de", x)

    # Insertar después de un valor X
    def insertar_despues(self, x, info):
        actual = self.inicio

        while actual is not None and actual.info != x:
            actual = actual.liga

        if actual is None:
            print("No se encontró el valor", x)
            return

        nuevo = Nodo(info)
        nuevo.liga = actual.liga
        actual.liga = nuevo
        print("Nodo insertado después de", x)

    # Eliminar un elemento por su valor
    def eliminar(self, x):
        if self.inicio is None:
            print("La lista está vacía")
            return

        # Si el elemento está al inicio
        if self.inicio.info == x:
            self.inicio = self.inicio.liga
            print("Elemento eliminado")
            return

        actual = self.inicio

        # Buscar el elemento anterior al que se eliminará
        while actual.liga is not None and actual.liga.info != x:
            actual = actual.liga

        if actual.liga is None:
            print("No se encontró el elemento", x)
            return

        # Saltar el nodo que se quiere eliminar
        actual.liga = actual.liga.liga
        print("Elemento eliminado")


# Programa principal
lista = ListaSimple()

cantidad = int(input("¿Cuántos nodos deseas ingresar al inicio? "))

for i in range(cantidad):
    dato = input("Ingresa el dato del nodo: ")
    lista.insertar_final(dato)

opcion = 0

while opcion != 7:
    print("\n--- LISTA SIMPLEMENTE LIGADA ---")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Insertar antes de un valor X")
    print("4. Insertar después de un valor X")
    print("5. Eliminar un elemento")
    print("6. Mostrar lista")
    print("7. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        dato = input("Ingresa el nuevo dato: ")
        lista.insertar_inicio(dato)

    elif opcion == 2:
        dato = input("Ingresa el nuevo dato: ")
        lista.insertar_final(dato)

    elif opcion == 3:
        x = input("¿Antes de qué valor deseas insertar? ")
        dato = input("Ingresa el nuevo dato: ")
        lista.insertar_antes(x, dato)

    elif opcion == 4:
        x = input("¿Después de qué valor deseas insertar? ")
        dato = input("Ingresa el nuevo dato: ")
        lista.insertar_despues(x, dato)

    elif opcion == 5:
        x = input("¿Qué elemento deseas eliminar? ")
        lista.eliminar(x)

    elif opcion == 6:
        lista.mostrar()

    elif opcion == 7:
        print("Programa finalizado")

    else:
        print("Opción no válida")
