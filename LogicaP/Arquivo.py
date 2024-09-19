import random
from random import randint

#Jogo pedra, papel, tesoura
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Jogo Pedra, Papel e tesoura!")


#O item ue você escolher tem a função de ser mais forte que o do seu adversário
print("Suas opções:")
print("[1] Pedra")
print("[2] Papel")
print("[3] Tesoura")
pedra = 1
papel = 2
tesoura = 3


computador = random.randint (1,3)


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-==-=-=")
#Escolha um item entre: pedra, papel ou tesoura

usuario = int(input("Qual a sua jogada?"))


print("PEDRA...")
print("PAPEL...")
print("TESOURA...!")

print(f'o Jogador jogou --> {usuario}')
print(f'o computador escolheu --> {computador}')


#A logica de "força" do item é a seguinte: Pedra = quebra a tesoura. Tesoura = corta o papel. Papel = Enrola a pedra

if computador == pedra and usuario == pedra:
    print("empate")     #1

if usuario == pedra and computador == papel:
    print("Você perdeu! :c ")     #2

if usuario == pedra and computador == tesoura:
    print("Você ganhou!")     #3

if usuario == papel and computador == pedra:
    print("Você ganhou!")     #4

if usuario == papel and computador == papel:
    print("Empatou!")     #5

if usuario == papel and computador == tesoura:
        print("Você perdeu! :c")  #6

if usuario == tesoura and computador == pedra:
        print("Você perdeu! :c")  #7

if usuario == tesoura and computador == papel:
        print("Você ganhou!")  #8

if usuario == tesoura and computador == tesoura:
        print("Empatou!")  #9



# pedra mata tesoura
# tesoura mata papel
# papel mata pedra












