lista = []
i = 0
while i < 5:
    numero = int(input("Insira um valor para inserir no vetor:"))
    lista.append(numero)
    i = i + 1

print("Lista inputada:", lista)
print("Lista inversa:", lista[::-1])
