produto = int(input("qual o nº do produto?"))

if produto == 1:
    print("Não perecivel!")
elif produto  > 1 and produto < 5:
    print("Perecivel")

elif produto > 4 and produto< 7:
    print("Vestuário")

elif produto == 7:
    print("Higiene Pessoal")

elif produto  > 7 and produto < 16:
    print("Limpeza e utensilio domésticos")

if produto  > 15 :
    print("Produto Invalido")
if produto  == 0 :
    print("Produto Invalido")

