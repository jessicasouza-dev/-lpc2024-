CPF = input("INSIRA SEU CPF NO FORMATO 'xxx.xxx.xxx-xx': ")




if len(CPF) == 14:
    if CPF[3] != "." or CPF[7] != "." or CPF[11] != "-":
        print("formato inválido! o formato 'xxx.xxx.xxx-xx' não foi seguido!")
        exit(1)

    else:
        for i in range(len(CPF)):
            if i != 3 and i != 7 and i != 11:
                checar_numero = CPF[i].isdigit()

            if checar_numero != True:
                print("formato inválido! há algum dígito que não pode ser aceito!")
                exit(1)
else:
    print("formato inválido!")
    exit(1)

print(f"muito obrigado! seu CPF é: {CPF}")
