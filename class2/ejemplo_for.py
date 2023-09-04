frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
  print(fruta)

mi_cadena = "Hola mundo"

for caracter in mi_cadena:
  print(caracter)

for numero in range(1,6):
  print(numero)

mi_diccionario = {"a": 1, "b": 2, "c": 3}

for clave in mi_diccionario:
  print(clave)

for valor in mi_diccionario.values():
  print(valor)

for clave, valor in mi_diccionario.items():
  print(clave, valor)

mi_lista = ["a", "b", "c"]

for indice, valor in enumerate(mi_lista):
  print("Indice: ", indice, "Valor: ", valor)

nombres = ["Juan", "Pedro", "Maria"]
edades = [20, 30, 40]
print(nombres + edades)

for indice, (nombre, edad) in enumerate(zip(nombres, edades)):
  print("Indice: ", indice, "Nombre: ", nombre, "Edad: ", edad)

# Expresion de una sola linea
mi_lista2 = (x for x in range(1,6))
mi_generador = (x for x in range(1,6))

print(mi_lista2)
print(mi_generador)