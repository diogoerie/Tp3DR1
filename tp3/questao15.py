x = "recursao"
letra = input("Digite uma letra: ")

def contadorstring(letra, x):
    contador = 0
    for i in x:
        if i == letra:
            contador += 1
    return contador

contador = contadorstring(letra, x)
print(f"A letra {letra} aparece {contador} vez em {x}.")


