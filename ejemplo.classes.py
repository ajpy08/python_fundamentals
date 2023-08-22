class Empleado:
  def __init__(self, nombre, puesto, antiguedad):
    self.nombre = nombre
    self.puesto = puesto
    self.antiguedad = antiguedad

  def __str__(self):
    return f'Nombre: {self.nombre}, Puesto: {self.puesto}, Antiguedad: {self.antiguedad}'

    
  def ascender(self, nuevo_puesto):
    self.puesto = nuevo_puesto

  def aumentar_antiguedad(self, anios):
    self.antiguedad += anios


empleado1 = Empleado('Angel', 'Software Developer', 3)
empleado1.aumentar_antiguedad(2)

print("Datos de empleado: ", empleado1)