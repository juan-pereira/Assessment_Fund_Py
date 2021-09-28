def lista_em_tupla():
    i = 0
    lista_numeros = []

    while i < 8:
        num = int(input("Insira um número desejado: "))
        lista_numeros.append(num)
        i = i + 1
    return tuple(lista_numeros)

def impar_ou_par(separa_tupla):
    lista_impar = []
    lista_par = []

    for i in range(len(separa_tupla)):
        if separa_tupla[i] % 2 != 0:
            lista_impar.append(separa_tupla[i])
        elif separa_tupla[i] % 2 == 0:
            lista_par.append(separa_tupla[i])
    return lista_impar, tuple(lista_par)



tupla_total = lista_em_tupla()
lista_impar, lista_par = impar_ou_par(tupla_total)
print(tupla_total)
print(lista_par)
print(lista_impar)