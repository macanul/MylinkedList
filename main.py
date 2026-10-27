
from MyLinkedList import MyLinkedList

# Crear una lista enlazada
lista = MyLinkedList()

# Insertar elementos
lista.insertar_al_final(10)
lista.insertar_al_final(20)
lista.insertar_al_final(30)

print("Lista inicial:")
lista.mostrar()

# Insertar un elemento al inicio
lista.insertar_al_inicio(5)

print("\nLista despues de insertar al inicio:")
lista.mostrar()

# Buscar un elemento
print("\n¿Existe el numero 20?")
print(lista.buscar(20))

# Eliminar un elemento
lista.eliminar(20)

print("\nLista despues de eliminar el 20:")
lista.mostrar()

# Mostrar el tamano
print("\nTamano de la lista:")
print(lista.obtener_tamano())

# Comprobar si esta vacia
print("\n¿La lista esta vacia?")
print(lista.esta_vacia())
