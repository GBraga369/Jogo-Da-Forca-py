from funcoes import *
import random

lista_frutas = ["uva", "morango", "banana"]
palavra = []

secreto = random.choice(lista_frutas)

while True:
    letras = input("Digite uma letra: ")

    if len(letras)>1:
        print("Digite apenas uma letra: ")
        continue

    palavra.append(letras)

    secreto_temp = ""

    chute_s = chute(secreto,letras)

    secreto_temp += chute_s

    print(secreto_temp)
