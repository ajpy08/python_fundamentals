def case1():
  return "Esta es la opcion 1"

def case2():
  return "Esta es la opcion 2"

def case3():
  return "Esta es la opcion 3"

def default_case():
  return "Opcion no valida"

switch_dic = {
  "opcion1": case1,
  "opcion2": case2,
  "opcion3": case3
}

def switch_example(case):
  return switch_dic.get(case, default_case)()

opcion = "opcion2"
resultado = switch_example(opcion)
print(resultado)