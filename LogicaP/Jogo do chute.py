#importando biblioteca random
import random
from idlelib.colorizer import prog_group_name_to_tag

#declanrando variaveis
numero_chute = 0
chute = 0


numero_x = random.randint (0,9) #randomiza um numero de 0 a 9
print("vamos jogar um jogo...")

contador = 0 #declara um contador de tentativas

#estrutura de chutes para erros  e acertos
while numero_x !=numero_chute:
    numero_chute = int(input ("chute um numero de 1 a 9"))
    contador = contador + 1

    if numero_chute < numero_x :
        print("valor baixo, tente novamente")

    elif numero_chute > numero_x:
        print("valor alto, tente novamente")

    else:
        print(f"você acertou em {contador} tentativas!")
