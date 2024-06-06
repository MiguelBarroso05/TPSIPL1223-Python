def exemplos():

    lista = []
    positions = []
    ok = int(input("Indique o nmr de elementos da sua lista: "))

    for i in range(ok):
        lista.append(int(input("indique a sua lista:")))

    inteiro = int(input("Indique o numero de elementos a somar: "))

    for j in range(inteiro):
        max_value = max(lista)
        max_position = lista.index(max_value)
        positions.append(max_position)
        lista.pop(max_position)
    positions.sort()
    positions = tuple(positions)
    print(positions)


def exemplo2():
    lista = [42, 3, 10, 33, 7, 6, 13]
    target_sum = 17
    # Itera sobre todos os pares de elementos
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == target_sum:
                print("Índices dos elementos que somam 17:", i, j)


exemplo2()