def f1():
    nota = float(input("Insira uma nota (entre 0 a 10): "))
    while (10<nota<0):
        return ("Insira um valor valido: ")
        f1()
    return f"A sua nota foi {nota}"

