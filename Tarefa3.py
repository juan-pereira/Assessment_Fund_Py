def potencia(num1, num2):
    resultado = num1 ** num2
    print(resultado)


def potencia_while(num1, num2):
    i = 0
    potenciacao = 1
    while i < num2:
        potenciacao *= num1
        i = i + 1
    print(potenciacao)


n1 = int(input("Insira um número inteiro: "))
n2 = int(input("Insira a que potência esse número será elevado: "))
potencia(n1, n2)
potencia_while(n1, n2)
