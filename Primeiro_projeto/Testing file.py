from Exercicios import exer1 as e1


def escolha():
    pagina = input("Escolha a pag. de exercicios!: ")
    exer = input("Escolha o exer!: ")
    show = pagina.exer()
    if pagina == 1:
        pagina = e1
        print(show)
    else:
        pass


print(escolha())