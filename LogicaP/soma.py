soma = 0  #variavel "soma"
cont = 0 #variavel "cont"

for c in range (1,4):
    numero = float(input (f'Digite o {c} valor: '))
    if numero %2 == 0:
        soma += numero
        cont += 1

print (f' Você informou {cont}, a soma de valores pares foi: {soma}')
