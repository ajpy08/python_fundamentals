numeros = [1, 2, 3, 4, 5]

frutas = ["manzana", "banana", "cereza", "pera", "uva"]

mixta = [10, "hola", True, 3.14]

numeros[2] = 15

print(numeros[2])

print(frutas[4])

print(numeros)
print("lenght:", len(numeros))
print("min: ", min(numeros))
print("max: ", max(numeros))
print("sum: ", sum(numeros))

# Metodos de Listas

numeros = [1, 2, 3, 4, 5]

numeros.append(6)
print("append:", numeros)

numeros.insert(0, 0)
print("insert:", numeros)

numerosII = [1, 7, 8, 9]
numeros.extend(numerosII)
print("extend:", numeros)

numeros.remove(2)
print("remove:", numeros)

numeros.pop()
print("pop:", numeros)

print("index:", numeros.index(5))

print("count:", numeros.count(1))

mi_lista = [1,6,2,45,7,2,34,8,2,1]
mi_lista.sort()
print("sorted:", mi_lista)

mi_lista.reverse()
print("reverse:", mi_lista)

mi_lista.clear()
print("clear:", mi_lista)

mi_lista = [1,2,3,4,5]
sublista = mi_lista[1:3]
print("sublista:", sublista)

original = [1,2,3,4,5]
copia1 = original.copy()
copia2 = list(original)
copia3 = original[:]

print("original:", original)
print("copia1:", copia1)
print("copia2:", copia2)
print("copia3:", copia3)

cadena = "Hola mundo"
lista = list(cadena)
print(lista)

secuencia = list(range(10))
print(secuencia)

nombres = ["Juan", "Pedro", "Maria"]
edades = [20, 30, 40]

combinada = zip(nombres, edades)
print("combinada:", list(combinada))

frutas = ["manzana", "banana", "cereza"]
enumerada = enumerate(frutas, start = 1)
print("enumerada:", list(enumerada))

mi_lista = list(range(1, 6))
print(mi_lista)

mi_tupla = tuple(mi_lista)
print("mi_tupla:", mi_tupla)

def cuadrado(x):
  return x ** 2

cuadrados = list(map(cuadrado, mi_lista))
print("cuadrados:", cuadrados)