lista = [1, 2, 3, 4]
def soma(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma(lista[1:])
print(soma(lista))
