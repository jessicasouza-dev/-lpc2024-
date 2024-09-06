import sys
import random

palavras = []
erros = 0
resposta = []
ganhou = False

arquivo = sys.argv[1]
with open(arquivo, 'r') as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())


palavra = palavras[random.randint(0, len(palavras)-1)]

for i in range(0, len(palavra)):
    resposta.append("_")

while ganhou == False and erros < 6:
    resposta_final = ""
    aparicoes = []

    letra = input("DIGITE UMA LETRA: ").upper().strip()

    tem_letra = palavra.find(letra)

    for i in range(len(palavra)):
        if palavra[i] == letra:
            aparicoes.append(i)

    if tem_letra == -1:
        erros = erros+1
        print(f"Você errou pela {erros}ª vez. Tente de novo")

    else:
        for i in aparicoes:
            resposta[i] = letra

        for i in resposta:
            resposta_final = resposta_final + i

        resposta_final = resposta_final.strip()

        print(f"A palavra é: {resposta_final}")
        if resposta_final == palavra:
            ganhou = True


if erros == 6:
    print(f"VOCÊ PERDEU! A PALAVRA ERA {palavra}")
else:
    print("VOCÊ GANHOU! :D")

