direccion = input("Ingrese el correo de email = ")
def validar(direccion):
    if direccion.find('@' and ('.com' or '.co')) >= 0: #Utiliza funcion .find() para validar email.
        print("Direccción válida")
    else:
        print("Dirección inválida")
validar(direccion) #Devuelve que es válida o no dependiendo si cumplen las condiciones anteriores.
