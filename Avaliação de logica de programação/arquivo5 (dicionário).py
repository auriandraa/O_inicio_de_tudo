pessoas = {} #dicionario
nome1 = input("Nome:") #entrada do nome de usuário1
idade1 = int(input("Idade:")) #entrada da idade do usuário1

nome2 = input("Nome:") #entrada do nome de usuário2
idade2 = int(input("Idade:"))#entrada da idade do usuário2

nome3 = input("Nome:") #entrada do nome de usuário3
idade3 = int(input("Idade:"))#entrada da idade do usuário3

pessoas [nome1] = idade1 #armazenamento das chaves no dicionario
pessoas [nome2] = idade2 #armazenamento das chaves no dicionario
pessoas [nome3] = idade3 #armazenamento das chaves no dicionario


#abaixo o que usei para fazer o pc comparar as idades e me informar qual é o mais velho

if idade1 > idade2 and idade1 > idade3:
    print(f"{nome1} é o mais usuário mais velho")
if idade2 > idade1 and idade2 > idade3:
    print(f"{nome2} é o mais usuário mais velho")
if idade3 > idade1 and idade3 > idade2:
    print(f"{nome3} é o mais usuário mais velho")




