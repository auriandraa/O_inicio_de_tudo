import time

for contagem in range(1,101):

    print(contagem)
print("x")

for contagem in range(100,0,-1):
    time.sleep(0.15)
    print(contagem)

# Importa o módulo time para usar a função sleep
# Loop que conta de 1 até 100 e imprime cada número
# Após a contagem, imprime "x"

# Loop que conta de 100 até 1, imprimindo cada número
# A cada número, espera 0,15 segundos usando time.sleep

