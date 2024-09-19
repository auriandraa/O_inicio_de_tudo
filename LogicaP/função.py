i = 0
entrada = int(input("vamos iniciar a contagem? 1 para sim 0 para não"))
def detectou(i):
    if detectou == 1:
        i = i + 1
        print("ovelha detectada")
    return i

def naodetectou(i):
    print("Ovelha não detectada")
    return i

if entrada == 1:
    while True:
        detectou_ovelha = int(input("Detectou ovelha ?(1 parar sim, 0 parar)"))
        if detectou_ovelha == 1:
            detectou(i)
        else:
         break