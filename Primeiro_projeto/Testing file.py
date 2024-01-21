import exer1 as e1
import exer2 as e2


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