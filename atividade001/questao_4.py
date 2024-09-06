unidades = [
    "ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO",
    "SEIS", "SETE", "OITO", "NOVE"
]

casa_dez = [
    "DEZ", "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE",
    "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE"
]

dezenas = [
    "", "", "VINTE", "TRINTA", "QUARENTA", "CINQUENTA",
    "SESSENTA", "SETENTA", "OITENTA", "NOVENTA"
]

numero = input("Insira um número: ").strip()

if int(numero) > 99 or int(numero) < 0:
    print("número inválido.")
else:
    casas = len(numero)

    if casas == 1:
        print(f"O NÚMERO {numero} ESCRITO EM EXTENSO: {unidades[int(numero)]}")

    elif casas == 2:
        if numero[0] == "1":
            print(f"O NÚMERO {numero} ESCRITO EM EXTENSO: {casa_dez[int(numero[1])]}")

        elif numero[0] != "1" and numero[1] == "0":
            print(f"O NÚMERO {numero} ESCRITO EM EXTENSO: {dezenas[int(numero[0])]}")

        else:
            print(f"O NÚMERO {numero} ESCRITO EM EXTENSO: {dezenas[int(numero[0])]} E {unidades[int(numero[1])]}")
