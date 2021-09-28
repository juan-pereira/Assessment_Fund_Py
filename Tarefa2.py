total = 0
n = int(input("Insira até que número deseja somar os números pares: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print("Valor a ser somado:", i)
        total = total + i
print("Valor total:", total)
