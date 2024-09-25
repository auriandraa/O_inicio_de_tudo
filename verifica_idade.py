ano_nascimento = int(input("insira o ano de nascimento")) #variavel
ANO=2024 #constante
idade = ANO - ano_nascimento #variavel
print(idade) #comando para mostrar o valor da idade de acordo com o ano da constante

if  idade >= 16 and idade <=17:
    print("usuário possui idade para votar")
if idade >= 18:
    print("o usuário pode votar e tirar a carteira de habilitação")
    if idade >= 30:
        print("o usuário tem dor nas costas")


