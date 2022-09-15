#Exercício 3

vidas = 5
letra = 'o'
while vidas > 0:
    palavra = str(input("Adivinhe a letra faltante: _v_ : "))
    if palavra != letra:
        vidas -= 1
    else:
        print("Vitória")
        break
else:
    print("Derrota")