while True: #
    try: #Intentamos obtener los datos de entrada
        a = int(input("Ingresa el primer numero: \n")) #Se digita el primer número
        b = int(input("Ingresa el segundo numero: \n"))#Se digita el segundo número
        print (("Que cálculo quieres realizar entre"), (a), ("y"), (b), ("?\n")) #Se pide el cálculo a realizar entre los números ingresados
        op = str(input(""" #Ofrecemos las opciones de cálculo que van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))
    except: #En caso de error:
        print ("Error")
        op = '?'