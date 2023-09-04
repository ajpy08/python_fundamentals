try:
  resultado = 10 / 0
except Exception as e:
  print("Error: ", e)
else:
  print("La división es correcta")
finally:
  print("Finalizado")

try:
  resultado = 10 / 0
except Exception as e:
  print("Error: ", e)

try:
  numero = int("texto")
except ValueError as e:
  print("Error de valor: ", e)

try:
  resultado = 10 / "2"
except TypeError as e:
  print("Error de tipo: ", e)

try:
  print(variable_no_definida)
except NameError as e:
  print("Error de nombre: ", e)

try:
  with open("archivo_no_existe", "r") as archivo:
    contenido = archivo.read()
except FileNotFoundError as e:
  print("Error de archivo no encontrado: ", e)

try:
  lista = [1, 2, 3]
  elemento = lista[10]
except IndexError as e:
  print("Error de índice: ", e)


try:
  diccionario = {"clave1": "valor1"}
  valor = diccionario["clave2"]
except KeyError as e:
  print("Error de clave: ", e)

class MiExcepcion(Exception):
  def __init__(self, mensaje, codigo_error):
    super().__init__(mensaje)
    self.codigo_error = codigo_error

  def obtener_codigo_error(self):
    return self.codigo_error

try:
  raise MiExcepcion("Ocurrió un error personalizado", 42)
except MiExcepcion as e:
  print("Se ha producido una excepcion personalizada", e)
  print("Codigo de error:", e.obtener_codigo_error())