#Exercício 1

list = []

while len(list) < 3:
    numero = int(input("Por favor, digite um número: "))
    list.append(numero)

    if len(list) == 3:
        print("O maior número digitado foi: ", max(list))
        break