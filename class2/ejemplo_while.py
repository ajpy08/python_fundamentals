contador = 0

while contador < 5:
  print(contador)
  contador += 1


frutas = ["manzana", "banana", "cereza", "pera", "uva"]

for fruta in frutas:
  if fruta == "pera":
    break
  print(fruta)

contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("Fin del bucle")