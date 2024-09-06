palindromo = ""
palindromo_separado = ""

frase = input("Insira uma frase: ").strip()

frase_junta = frase.replace(" ", "")

for i in range(len(frase_junta)-1, -1, -1):
    palindromo = palindromo + frase_junta[i]

for i in range(len(frase) - 1, -1, -1):
    palindromo_separado = palindromo_separado + frase[i]

if palindromo == frase_junta:
    print(f"A frase {frase} é um palíndromo.")
else:
    print(f"A frase {frase} não é um palíndromo. A sua versão inversa: {palindromo_separado}.")
