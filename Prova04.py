#Exercício 4

opcoes = int(input("Olá, boa noite! Digite 1 para consultar o saldo, 2 para saque, 3 depósito e 4 para sair: "))
saldo = 0

while opcoes != 4:

    if opcoes == 1:
        print("O seu saldo é: R$", saldo)
        break
    if opcoes == 2:
        valorSaque = int(input("Digite o valor do saque: "))
        valorRetirado = valorSaque - saldo
        saldo -= valorRetirado
        print("Voce retirou R$", valorRetirado, "e seu saldo ficou: R$", saldo)
        break
    if opcoes == 3:
        valorDeposito = int(input("Digite o valor do depósito: "))
        valorDepositado = valorDeposito + saldo
        saldo += valorDepositado
        print("Voce depositou R$", valorDepositado, "e seu saldo ficou: R$", saldo)
        break