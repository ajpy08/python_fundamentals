import os.path as path

file = "example.txt"

numpalabras = 0

if (path.exists(file)):
  archivo = open(file, "r")
  for linea in archivo:
      palabras = linea.split()
      for palabra in palabras:
          numpalabras += 1
  archivo.close()
  print('El texto contiene %s palabras' %numpalabras)
else:
  print('El archivo no existe o es invalido!!!')