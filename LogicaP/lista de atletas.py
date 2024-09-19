from datetime import date

nome = input("Nome:")

ano_nascimento = int (input("Ano de nascimento:"))

idade = date.today().year  - ano_nascimento



categoria = ("Mirim" if idade <=  9  else
             "Infantil" if idade <= 14 else
             "Junior" if idade <= 19 else
             "sênior" if idade <= 25 else
             "Master")
print(f'Olá {nome} a sua incrição feita com sucesso! Sua categoria é a {categoria}')

