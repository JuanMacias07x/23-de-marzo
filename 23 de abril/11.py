Palabra = input("introduce una palabra: ")
reversed palabra = palabra
palabra = list(palabra)
reversed palabra = list(reversed palabra)
reversed palabra.reverse()
if palabra == reversed palabra:
    print("Es un palídromo")
else:
    print("No es un palíndromo")
