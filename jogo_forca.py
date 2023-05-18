import random

frutas = ["uva","banana","morango"]
letras = []
cont = 0

secreto = random.choice(frutas)

while True:
    letra = input("Digite uma letra: ")

    if len(letra)>1:
        print("digite apenas 1 letra")
        continue

    letras.append(letra)

    secreto_temp = ""

    for i in secreto:
        if i in letras:
            secreto_temp += i
        else:
            secreto_temp += "*"

    if secreto_temp == secreto:
        print(f'a palavra secreta é {secreto} você ganhou')
        break
    else:
        print(f'a palavra secreta está assim {secreto_temp}')

    if letra not in secreto:
        cont += 1
        print(f'tentativas {cont}/3')

    if cont >= 3:
        print("Você não tem mais chances!")
        break
