alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Se almacena una lista con las letras del abecedario
for i in range(len(alfabeto), 1, -1):
    if i % 3 == 0:      #Si una letra está ubicada en un multiplo de 3, no aparece en el resultado
        alfabeto.pop(i-1)    #Con la función .pop se elimina los números multiplos de 3
print(alfabeto)       #Se imprime el abecedario
