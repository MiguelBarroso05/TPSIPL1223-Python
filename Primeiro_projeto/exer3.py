def f1():
    print("Indique 5 números: ")
    lista = []
    for i in range(5):
        x = int(input())
        lista.append(x)
    return lista


def f2():
    print("Indique 10 números: ")
    lista = []
    for i in range(10):
        x = int(input())
        lista.append(x)
    return lista.sort(reverse=True)


def f3():
    print("Indique 4 notas: ")
    lst = []
    for i in range(4):
        x = int(input())
        lst.append(x)
    return sum(lst) / len(lst)


def f4():
    vetor = input("Digite um vetor de 10 caracteres: ")
    if len(vetor) == 10:
        pass
    else:
        print("Erro: O vetor deve ter exatamente 10 caracteres.")

    consoantes = [c for c in vetor if c.isalpha() and c.lower() not in 'aeiou']
    total_consoantes = len(consoantes)

    print(f"Total de consoantes: {total_consoantes}")

    if total_consoantes > 0:
        return "Consoantes encontradas:", ', '.join(consoantes)
    else:
        return "Nenhuma consoante encontrada."


def f5():
    vetor = []
    print("Introduza 20 números inteiros: ")
    for i in range(20):
        x = int(input())
        vetor.append(x)
    if len(vetor) == 20:
        pass
    else:
        print("Erro: O vetor deve ter exatamente 10 caracteres.")

    par = [c for c in vetor if (c % 2) == 0]
    impar = [c for c in vetor if (c % 2) != 0]
    return f"{impar}\n{par}"
