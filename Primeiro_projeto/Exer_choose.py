import os
import exer1 as e1
import exer2 as e2

pagina = int(input("Escolha a pag. de exercicios!: "))
exer = int(input("Escolha o exer!: "))
if pagina == 1:
        match(exer):
            case 1:
                print(e1.f1())
            case 2:
                print(e1.f2())
            case 3:
                print(e1.f3())
            case 4:
                print(e1.f4())
            case 5:
                print(e1.f5())
            case 6:
                print(e1.f6())
            case 7:
                print(e1.f7())
            case 8:
                print(e1.f8())
            case 9:
                print(e1.f9())
            case 10:
                print(e1.f10())
            case 11:
                print(e1.f11())
            case 12:
                print(e1.f12())
            case 13:
                print(e1.f13())
            case 14:
                print(e1.f14())
            case 15:
                print(e1.f15())
            case 16:
                print(e1.f16())

elif pagina == 2:
        match exer:
            case 1:
                print(e2.f1())
            case 2:
                print(e2.f2())
            case 3:
                print(e2.f3())
            case 4:
                print(e2.f4())
            case 5:
                print(e2.f5())
            case 6:
                print(e2.f6())
            case 7:
                print(e2.f7())
            case 8:
                print(e2.f8())
            case 9:
                print(e2.f9())
            case 10:
                print(e2.f10())






