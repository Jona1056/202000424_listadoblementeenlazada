##lista doblemente enlazada
class Nodo: ##contructor
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class lista:

    def __init__(self) :
        self.primero = None
        self.ultimo = None
        self.tam = 0

    def agregar_dato(self, dato):
        nuevo = Nodo(dato) #crea un nuevo nodo
        if self.primero == None: #si la lista esta vacia
            self.primero = nuevo #el primero es el nuevo nodo
            self.ultimo = nuevo #el ultimo es el nuevo nodo
        else:
            nuevo.siguiente = self.primero  #el siguiente del nuevo nodo es el primero
            self.primero.anterior = nuevo #el anterior del primero es el nuevo nodo
            self.primero = nuevo #el primero es el nuevo nodo
        self.tam += 1 #aumenta el tamano de la lista

    def mostrar_dato(self, dato):
        if self.primero == None:
            print("Lista vacia")
        else:
            aux = self.primero
            while aux != None: 
                if aux.dato == dato:
                    print("dato siguiente: " +str(aux.siguiente.dato)+", " + "dato actual: "+ str(aux.dato)+", " +"dato anterior: " + str(aux.anterior.dato))
                    break
                aux = aux.siguiente

    def mostrar_lista(self):
        if self.primero == None:
            print("Lista vacia")
        else:
            aux = self.primero
            while aux != None:
                print(aux.dato, end=" ")
                aux = aux.siguiente

lista = lista()
lista.agregar_dato(7)
lista.agregar_dato(2)
lista.agregar_dato(5)
lista.agregar_dato(3)
lista.agregar_dato(4)
lista.mostrar_lista()
dato = int(input("Seleccione un numero: "))
lista.mostrar_dato(dato)

