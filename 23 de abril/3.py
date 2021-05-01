cursos = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]
lista = []
for orden in cursos:
    notas = float(input("Digite sus notas en " + orden + ": "))
    lista.append(notas)
    print("Las notas digitadas fueron: " + str(lista))