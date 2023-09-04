# # __init__(self, ...)
# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

# juan = Persona("Juan", 30)
# print(juan.edad)

# # __str__(self)
# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def __str__(self):
#         return f"{self.nombre}, {self.edad} años"

# juan = Persona("Juan", 30)
# print(str(juan))  # Imprimirá "Juan, 30 años"

# # __repr__(self)
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Punto({self.x}, {self.y})"

# p = Punto(1, 2)
# print(repr(p))  # Imprimirá "Punto(1, 2)"

# # __len__(self)
# class MiLista:
#     def __init__(self, elementos):
#         self.elementos = elementos

#     def __len__(self):
#         return len(self.elementos)

# lista = MiLista([1, 2, 3, 4, 5])
# print(len(lista))  # Imprimirá 5

# # __getitem__(self, clave)
# class MiLista:
#     def __init__(self, elementos):
#         self.elementos = elementos

#     def __getitem__(self, indice):
#         return self.elementos[indice]

# lista = MiLista([1, 2, 3, 4, 5])
# print(lista[2])  # Imprimirá 3

# # __setitem__(self, clave, valor)
# class MiDiccionario:
#     def __init__(self):
#         self.datos = {}

#     def __setitem__(self, clave, valor):
#         self.datos[clave] = valor

#     def __getitem__(self, clave):
#         return self.datos[clave]

# diccionario = MiDiccionario()
# diccionario["clave1"] = "valor1"
# print(diccionario["clave1"])  # Imprimirá "valor1"

# # __delitem__(self, clave)
# class MiDiccionario:
#     def __init__(self):
#         self.datos = {}

#     def __delitem__(self, clave):
#         del self.datos[clave]

# diccionario = MiDiccionario()
# diccionario["clave1"] = "valor1"
# del diccionario["clave1"]
# print(diccionario.get("clave1"))  # Imprimirá "None"

# # __iter__(self)
# class Contador:
#     def __init__(self, limite):
#         self.limite = limite

#     def __iter__(self):
#         self.valor = 0
#         return self

#     def __next__(self):
#         if self.valor < self.limite:
#             resultado = self.valor
#             self.valor += 1
#             return resultado
#         else:
#             raise StopIteration

# contador = Contador(5)
# for numero in contador:
#     print(numero)  # Imprimirá del 0 al 4

# # __contains__(self, elemento)
# class MiConjunto:
#     def __init__(self, elementos):
#         self.elementos = elementos

#     def __contains__(self, elemento):
#         return elemento in self.elementos

# conjunto = MiConjunto([1, 2, 3, 4, 5])
# print(3 in conjunto)  # Imprimirá True

# # __eq__(self, otro)
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, otro):
#         return self.x == otro.x and self.y == otro.y

# p1 = Punto(1, 2)
# p2 = Punto(1, 2)
# print(p1 == p2)  # Imprimirá True

# # __ne__(self, otro)
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __ne__(self, otro):
#         return self.x != otro.x or self.y != otro.y

# p1 = Punto(1, 2)
# p2 = Punto(1, 2)
# print(p1 != p2)  # Imprimirá False

# # __lt__(self, otro)
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __lt__(self, otro):
#         return self.x < otro.x and self.y < otro.y

# p1 = Punto(1, 2)
# p2 = Punto(2, 3)
# print(p1 < p2)  # Imprimirá True

# # __le__(self, otro)
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __le__(self, otro):
#         return self.x <= otro.x and self.y <= otro.y

# p1 = Punto(1, 2)
# p2 = Punto(2, 3)
# print(p1 <= p2)  # Imprimirá True

# # __gt__(self, otro)
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __gt__(self, otro):
#         return self.x > otro.x and self.y > otro.y

# p1 = Punto(1, 2)
# p2 = Punto(0, 1)
# print(p1 > p2)  # Imprimirá True

# # __ge__(self, otro)
# class Punto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __ge__(self, otro):
#         return self.x >= otro.x and self.y >= otro.y

# p1 = Punto(1, 2)
# p2 = Punto(0, 1)
# print(p1 >= p2)  # Imprimirá True


'''
__init__(self, ...): Constructor de la clase. Se llama automáticamente cuando se crea una nueva instancia de la clase y se utiliza para inicializar sus atributos.

__str__(self): Se llama cuando se utiliza la función str(objeto) para obtener una representación de cadena legible para humanos del objeto.

__repr__(self): Devuelve una representación de cadena del objeto que se puede utilizar para recrear el objeto utilizando eval.

__len__(self): Se llama cuando se utiliza la función len(objeto) para obtener la longitud del objeto.

__getitem__(self, clave): Se llama cuando se utiliza la notación de corchetes para acceder a elementos de un objeto (por ejemplo, objeto[clave]).

__setitem__(self, clave, valor): Se llama cuando se utiliza la notación de corchetes para asignar un valor a un elemento de un objeto (por ejemplo, objeto[clave] = valor).

__delitem__(self, clave): Se llama cuando se utiliza la declaración del para eliminar un elemento de un objeto (por ejemplo, del objeto[clave]).

__iter__(self): Se llama cuando se itera sobre un objeto utilizando un bucle for.

__next__(self): Se llama para obtener el siguiente elemento en una iteración. Junto con __iter__, se utiliza para crear objetos iterables.

__contains__(self, elemento): Se llama cuando se utiliza el operador in para verificar si un elemento está en un objeto.

__eq__(self, otro): Se llama cuando se utiliza el operador == para comparar dos objetos.

__ne__(self, otro): Se llama cuando se utiliza el operador != para comparar dos objetos.

__lt__(self, otro): Se llama cuando se utiliza el operador < para comparar dos objetos.

__le__(self, otro): Se llama cuando se utiliza el operador <= para comparar dos objetos.

__gt__(self, otro): Se llama cuando se utiliza el operador > para comparar dos objetos.

__ge__(self, otro): Se llama cuando se utiliza el operador >= para comparar dos objetos.
'''

# Imprimir metodos dunder

class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"Objeto de MiClase con valor {self.valor}"

    def __add__(self, otro):
        return self.valor + otro.valor

    def metodo_normal(self):
        pass

# Obtén una lista de todos los atributos y métodos de la clase
atributos_y_metodos = dir(MiClase)

# Filtra y muestra solo los métodos dunder
metodos_dunder = [nombre for nombre in atributos_y_metodos if nombre.startswith("__") and nombre.endswith("__")]

for metodo in metodos_dunder:
    print(metodo)