def detectou(i):
    i = i + 1
    #print("ovelha detectada")
    return i

def naodetectou(i):
    print("Ovelha não detectada")
    return i

def contar_ovelhas():
    i = 0
    entrada = int(input("Vamos iniciar a contagem de ovelhas ? (1 para sim, 0 para não)."))

    if entrada == 1:
        while True:
            detector_de_ovelha = int(input("Detectou ovelha? (1 para sim, 0 para não)"))
            if detector_de_ovelha == 1:
                i = detectou(i) #conta ovelha
            elif detector_de_ovelha == 0:
                naodetectou(i)
                break #quebra o codigo


    print(f"O número de ovelhas contadas foi: {i}")

def saudacoes():
    print("Função 4")

contar_ovelhas()
saudacoes()