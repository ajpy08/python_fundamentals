tupla = (10, 20, 30, 40, 50)
print(tupla[3])

a, b, *_ = tupla

print (a)
print (b)

print(tupla[2:4])
print(*_)

tuple_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
first, *rest = tuple_2
print(f"First value is {first}")
print(f"Rest of values are {rest}")

tuple_3 = (10, 20, 20, 30, 40, 50, 60, 70, 80, 90)
sub_tuple = tuple_3[1:3]
print("subtuple: ", sub_tuple)

print("length: ", len(tuple_3))

conteo = tuple_3.count(20)
print("conteo: ", conteo)

index = tuple_3.index(30)
print("index", index)

otra_tupla = ("a", "b", "c")

tupla_concatenada = tuple_3 + otra_tupla
print(tupla_concatenada)

# print(tuple_3 * 100)

lista_tupla = list(tupla)
print(lista_tupla)

tupla_lista = tuple(lista_tupla)
print(tupla_lista)

print ("existe") if 30 in tupla else print("No existe")

if 300 in tupla:
  print("Existe")
else:
  print("No existe")

for i in tupla:
  print(i)

nombres = {
  (1,2): "Juan",
  (1,2): "Javier",
  (1,3): "Pedro",
  (1,4): "Maria"
}

print(nombres)
print(nombres[(1,2)])