import random

qnts_lados = [0,0,0,0,0,0]
resultados = []

for i in range(1,100):
    numero = random.randint(1,6)
    resultados.append(numero)

    if numero == 1:
        qnts_lados[0] = qnts_lados[0]+1
    elif numero == 2:
        qnts_lados[1] = qnts_lados[1] + 1
    elif numero == 3:
        qnts_lados[2] = qnts_lados[2] + 1
    elif numero == 4:
        qnts_lados[3] = qnts_lados[3] + 1
    elif numero == 5:
        qnts_lados[4] = qnts_lados[4] + 1
    elif numero == 6:
        qnts_lados[5] = qnts_lados[5] + 1

print(f"Quantidades do aparições do lado 1: {qnts_lados[0]} \n")
print(f"Quantidades do aparições do lado 2: {qnts_lados[1]} \n")
print(f"Quantidades do aparições do lado 3: {qnts_lados[2]} \n")
print(f"Quantidades do aparições do lado 4: {qnts_lados[3]} \n")
print(f"Quantidades do aparições do lado 5: {qnts_lados[4]} \n")
print(f"Quantidades do aparições do lado 6: {qnts_lados[5]} \n")
print(f"Resultados: {resultados}")

