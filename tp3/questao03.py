torre1 = [3,2,1]
torre2 = []
torre3 = []

def mover_disco(origem, destino):
    if origem and (not destino or origem[-1] < destino[-1]):
        destino.append(origem.pop())
    else:
        print("Movimento inválido.")

def reorganizar_pinos(n, origem, auxiliar, destino):
    if n == 1:
        mover_disco(origem, destino)
        print(f"Torre1: {torre1}, Torre2: {torre2}, Torre3: {torre3}")
    else:
        reorganizar_pinos(n - 1, origem, destino, auxiliar)
        mover_disco(origem, destino)
        print(f"Torre1: {torre1}, Torre2: {torre2}, Torre3: {torre3}")
        reorganizar_pinos(n - 1, auxiliar, origem, destino)
reorganizar_pinos(len(torre1), torre1, torre2, torre3)