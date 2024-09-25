peso = int(input("Qual é o peso?"))
altura = float (input("Qual é a altura?"))
#A fórmula é IMC = peso/(altura x altura)
imc = peso / (altura * altura)
print(imc)

#baixo 18,5
#normal 24,9
#excesso de peso 29,9

if imc <=18.5:
    print("Seu peso está abaixo do ideal")

elif 18.5 < imc <= 24.9:
    print("Seu peso está ideal")

elif 25<= imc <= 29.9:
    print("você está com sobrepeso")

else:
    print("Obesidade")


#o usuário faz insere seu peso e altura
#o programa verifica se o usuário está classificado em:
#abaixo do ideal, ideal, sobrepeso ou obesidade

#os dados informados são apenas ilustrativos






