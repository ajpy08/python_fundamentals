import json
import os
import re

contacts_file = 'contacts.json'

def get_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file)

def validations(name, phone, email, contacts):
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

  if name in contacts:
    phone, email = contacts[name]
    print ('\nError: Ya existe un contacto con ese nombre.')
    return False

  if not name:
    print('\nError: El nombre del contacto no puede estar vacío.')
    return False

  if not phone.isdigit() or len(phone) != 10:
    print('\nError: El número de teléfono debe ser un número de 10 dígitos.')
    return False

  if not (re.fullmatch(regex, email)):
    print('\nError: El correo electrónico debe tener un formato válido.')
    return False

  return True

def add_contact(contacts, name, phone, email):
    
    if validations(name, phone, email, contacts):
      contacts[name] = (phone, email)
      save_contacts(contacts)
      print('Contacto agregado exitosamente.')
    else:
      print('---------------------------')
      print('No se pudo agregar el contacto.')
      print('---------------------------')

def find_contact(contacts, name):
    if name in contacts:
        phone, email = contacts[name]
        print('---------------------------')
        print(f'Información del contacto:')
        print('---------------------------')
        print(f'Nombre: {name}')
        print(f'Teléfono: {phone}')
        print(f'Correo electrónico: {email}')
        print('---------------------------')
    else:
        print('El contacto no existe.')

def list_contacts(contacts):
    print('Lista de contactos:\n')
    print("{:<10} {:<10} {:<10}".format('NAME', 'PHONE', 'EMAIL'))
    if contacts.items().__len__() > 0:
      for name, (phone, email) in contacts.items():
          print('---------------------------')
          print("{:<10} {:<10} {:<10}".format(name, phone, email))     
      print('---------------------------')
    else:
        print('---------------------------')
        print('No hay contactos registrados.')
        print('---------------------------')
      

def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name] = (phone, email)
        save_contacts(contacts)
        print('---------------------------')
        print('Contacto actualizado exitosamente.')
        print('---------------------------')
    else:
        print('---------------------------')
        print('El contacto no existe.')
        print('---------------------------')

def delete_contact(contacts, name):
    if name in contacts:
      confirm = input('Estás seguro de eliminar el contacto? (y/n): ')
      print(confirm)
      if (confirm.lower() == 'y') or (confirm.lower() == 'yes'):
        del contacts[name]
        save_contacts(contacts)
        print('---------------------------')
        print('Contacto eliminado exitosamente.')
        print('---------------------------')
      else:
        print('---------------------------')
        print('Operación cancelada.')
        print('---------------------------')
    else:
        print('---------------------------')
        print('El contacto no existe.')
        print('---------------------------')

def main():
    contacts = get_contacts()

    while True:
        print('\n--- Administrador de Contactos ---')
        print('1. Agregar nuevo contacto')
        print('2. Buscar contacto')
        print('3. Mostrar lista de contactos')
        print('4. Actualizar contacto')
        print('5. Eliminar contacto')
        print('6. Salir')

        opcion = input('Selecciona una opción: ')

        if opcion.isdigit():
            opcion = int(opcion)

        if opcion == 1:
            name = input('Nombre del contacto: ')
            phone = input('Número de teléfono: ')
            email = input('Correo electrónico: ')
            add_contact(contacts, name, phone, email)
        elif opcion == 2:
            name = input('Nombre del contacto a buscar: ')
            find_contact(contacts, name)
        elif opcion == 3:
            list_contacts(contacts)
        elif opcion == 4:
            name = input('Nombre del contacto a actualizar: ')
            phone = input('Nuevo número de teléfono: ')
            email = input('Nuevo email electrónico: ')
            update_contact(contacts, name, phone, email)
        elif opcion == 5:
            name = input('Nombre del contacto a eliminar: ')
            delete_contact(contacts, name)
        elif opcion == 6:
            save_contacts(contacts)
            print('¡Adios!')
            break
        else:
            print('Opción no válida. Por favor, intenta de nuevo.')

if __name__ == '__main__':
    main()
