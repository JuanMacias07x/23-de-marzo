cond= "si"
def frecuencia(numero,digito):
    cantidad = 0
    while numero!=0:
        ultDigito=numero%10
        if ultDigito==digito:
            cantidad+=1
        numero=numero//10
    return cantidad
while cond=="si":
    num=int(input("Ingrese un número: "))
    un_digito= int(input("Ingrese un dígito: "))
    print("Frecuencia del dígito en el número:" ,frecuencia(num, un_digito))
    cond=input("Quieres volver a ingresar un número y dígito = sí o no")
    if cond == "no":
        print("Vuelve pronto :3")