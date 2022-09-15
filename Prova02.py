#Exercício 2

idade = int(input("Olá, por favor, digite a sua idade com dois dígitos: "))

tempoServico = int(input("E agora digite o seu tempo de servico: "))

if idade >= 65:
    print("Voce já pode tirar a sua aponsetadoria!")

elif tempoServico >= 30:
    print("Voce já pode tirar a sua aposentadoria!")

elif idade >= 60 and tempoServico >= 25:
    print("Voce já pode tirar a sua aposentadoria!")

else:
    print("Infelizmente voce ainda não pode tirar a sua aposentadoria.")