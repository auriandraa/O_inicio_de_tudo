Pseudosocial = 1
dormi_na_praca = 2
borboletas = 3
musica = '''
Vamos aos trabalhos, celas nos cavalos
Samba nos cavacos, servos e vassalos
Férias do passado tudo é relembrado
Nada é por caso todo espelho é falso
Sabem quanto eu falo
Sabem quanto eu bebo
Mas não sabem quanto eu caio'''


print(f'''
Jogo do advinhe a musica:

Dica: {musica}

[1]Pseudosocial
[2]dormi na praça
[3]borboletas 

''')
usuario = int(input("qual é a música?"))

if usuario == 1 :
    print ("voce acertou!") #\n cria uma nova linha

else:
    print("voce errou!")

