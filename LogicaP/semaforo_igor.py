import time

semaforo = ['verde', 'amarelo', 'vermelho']
i = 0

ligar = 0
ligar = int(input("""Deseja iniciar o programa?
[1]Ativar Semaforo
[2]Ativar Alerta
[3]Desativar Semaforo
"""))

time.sleep(2)

if ligar == 1:
    while True:
        print(semaforo[i])
        i = i + 1
        time.sleep(3)
        print(semaforo[i])
        i = i + 1
        time.sleep(3)
        print(semaforo[i])
        i = 0
        time.sleep(3)
elif ligar == 2:
    while True:
        print(semaforo[1])
        time.sleep(2)
else:
    while True:
        print("se não")
        break