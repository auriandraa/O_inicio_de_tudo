a = int(input("Valor A:"))
b = int(input("valor B:"))
c = int(input("Valor C:"))

if a > b and a > c:
    print(f"{a} é o maior valor")
if b > a and c > c:
    print(f"{b} é o maior valor")
if c > a and c > b:
    print(f"{c} é o maior valor")
print("---------------------")

if a < b and a < c:
    print(f"{a} é o menor valor")
if b < a and c < c:
    print(f"{b} é o menor valor")
if c < a and c < b:
    print(f"{c} é o menor valor")