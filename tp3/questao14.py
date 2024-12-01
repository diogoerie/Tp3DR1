lista = [1,2,3,4]


def calcular(lista):
    lista_nova = lista[1] + lista[2] + lista[3]
    lista_nova1 = lista[0] + lista_nova
    return lista_nova1

print(calcular(lista))