import time

vermelho1 = "VERMELHO"
amarelo1 = "AMARELO"
verde1 = "VERDE"

vermelho2 = "VERMELHO"
amarelo2 = "AMARELO"
verde2 = "VERDE"

rua1 = "Pinheiro Machado"
rua2 = "Xv de Novembro"

ligar = int(input('''  [1] para ativar o sinal 
  [2] para ativar o alerta
'''))
if ligar == 1:
    while True:
        print(f"{rua2} *{vermelho2}*, {rua1} *{verde1}*")
        time.sleep(2)
        print(f"{rua2} *{vermelho2}*, {rua1} *{amarelo1}*")
        time.sleep(2)
        print(f"{rua2} *{verde2}*, {rua1} *{vermelho1}*")
        time.sleep(2)
        print(f"{rua2} *{amarelo2}*, {rua1} *{vermelho1}*")
        time.sleep(2)


elif ligar == 2:
    while True:
        print(f"{rua2} *{amarelo2}* {rua1} *{amarelo1}*")
        time.sleep(1)

        print(f"{rua2} *off*, {rua1} *off*")
        time.sleep(1)






