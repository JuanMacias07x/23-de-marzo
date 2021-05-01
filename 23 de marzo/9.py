c =0 #Se determina la variable “c”para saber dónde va a iniciar, en este caso, desde “0”
for i in range(1000): #Determinamos la variable “i”mediante un rango (0-999), usando el for para esto
    ultimo_digito =(i **3) %10 #Se calculan los números naturales menores a mil, cuyo cubo termina en siete (7)
if ultimo_digito == 7:  # Si el último dígito es “7”, se cuenta en el código
    c=c +1 #Se toma la variable “c”y se le suma de unoen uno “+1”
print (c) #Seimprime la variable “c”por cada dato solicitado