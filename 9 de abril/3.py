if op == '1':#Si el usuario elige opción 1 llamamos a sumar
    sumar()
        break
    elif op == '2':#Si el usuario elige opción 2 llamamos a restar
        restar()
        break
    elif op == '3':#Si el usuario elige opción 3 llamamos a multiplicar
        multiplicar()
        break
    elif op == '4':#Si el usuario elige opción 4 llamamos a dividir
        dividir()
        break
    else:
        print ("""Has ingresado un número de opción erróneo""")#Esto se muestra si el número digitado por el ususario es inválido
