from enum import Enum

class Producto(Enum):
    SABRITAS = 'sabritas'
    REFRESCOS = 'refrescos'
    GALLETAS = 'galletas'
    HELADOS = 'helados'
    JUGOS = 'jugos'

class Market:
  def __init__(self):
    self.active = False
    self.caja = 110
    self.admin_name = 'Angel Puc'

  def login(self, username, password):
    if username == 'ajpy08' and password == '12345':
      self.active = True
    else:
      self.active = False
    
    return self.active


  def __str__(self):
    return f'Bienvenido: {self.admin_name}, el total en caja es ${self.caja}'

  # precios
  precio_sabritas = 15
  precio_refrescos = 18
  precio_galletas = 16
  precio_helados = 25
  precio_jugos = 12

  # stock
  total_sabritas = 0
  total_refrescos = 10
  total_galletas = 5
  total_helados = 8
  total_jugos = 12

  def venta(self, producto, cantidad):
    errorMessage = f'No hay suficiente stock para vender {cantidad} {producto}'
    salesMessage = f'{cantidad} {producto} vendid@(s), cobrar $'
    if producto == 'sabritas':
      if cantidad <= self.total_sabritas:
        self.total_sabritas -= cantidad
        total = cantidad * self.precio_sabritas
        self.caja += total
        print('{} {}'.format(salesMessage, total))
      else:
        print(errorMessage)
    elif producto == 'refrescos':
      if cantidad <= self.total_refrescos:
        self.total_refrescos -= cantidad
        total = cantidad * self.precio_refrescos
        self.caja += total
        print('{} {}'.format(salesMessage, total))
      else:
        errorMessage
    elif producto == 'galletas':
      if cantidad <= self.total_galletas:
        self.total_galletas -= cantidad
        total = cantidad * self.precio_galletas
        self.caja += total
        print('{} {}'.format(salesMessage, total))
      else:
        errorMessage
    elif producto == 'helados':
      if cantidad <= self.total_helados:
        self.total_helados -= cantidad
        total = cantidad * self.precio_helados
        self.caja += total
        print('{} {}'.format(salesMessage, total))
      else:
        errorMessage
    elif producto == 'jugos':
      if cantidad <= self.total_jugos:
        self.total_jugos -= cantidad
        total = cantidad * self.precio_jugos
        self.caja += total
        print('{} {}'.format(salesMessage, total))
      else:
        errorMessage
    else:
      print('Producto no disponible')
  
  def surtido(self, producto, cantidad):
    if self.active:
      if producto == 'sabritas':
        self.total_sabritas += cantidad
        print(f'Surtido de {producto}: {cantidad}')
      elif producto == 'refrescos':
        self.total_refrescos += cantidad
        print(f'Surtido de {producto}: {cantidad}')
      elif producto == 'galletas':
        self.total_galletas += cantidad
        print(f'Surtido de {producto}: {cantidad}')
      elif producto == 'helados':
        self.total_helados += cantidad
        print(f'Surtido de {producto}: {cantidad}')
      elif producto == 'jugos':
        self.total_jugos += cantidad
        print(f'Surtido de {producto}: {cantidad}')
      else:
        print('Producto no disponible')
    else :
      print('Usuario no autorizado')

  def inventario(self):
    print('*' * 50)
    print('STOCKS')
    print('*' * 50)
    print(f'Sabritas: {self.total_sabritas}')
    print(f'Refrescos: {self.total_refrescos}')
    print(f'Galletas: {self.total_galletas}')
    print(f'Helados: {self.total_helados}')
    print(f'Jugos: {self.total_jugos}')
    print(f'Total en caja: ${self.caja}')
    print('*' * 50)

market = Market()
allowed = market.login('ajpy08', '12345')

if allowed:
  print(market)
  market.inventario()
  market.surtido(Producto.SABRITAS.value, 4)
  market.venta(Producto.SABRITAS.value, 2)
  market.inventario()
  market.surtido(Producto.REFRESCOS.value, 5)
  market.venta(Producto.REFRESCOS.value, 3)
  market.inventario()
  market.surtido(Producto.GALLETAS.value, 2)
  market.venta(Producto.GALLETAS.value, 1)
  market.inventario()
  market.surtido(Producto.HELADOS.value, 3)
  market.venta(Producto.HELADOS.value, 1)
  market.inventario()
  market.surtido(Producto.JUGOS.value, 2)
  market.venta(Producto.JUGOS.value, 1)
  market.inventario()
else:
  print('Usuario no autorizado')