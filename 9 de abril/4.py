def impr_tabla (num): #La tabla llega hasta el número 10
    lim = 10 #Se comienza en 1
    cont = 1
    while cont <= lim:
        resultado = cont * num
        print("{} x {} = {}".format(num, cont, resultado)) #Se incrementa el contador para evitar el ciclo infinito
        cont = cont + 1
impr_tabla(5)