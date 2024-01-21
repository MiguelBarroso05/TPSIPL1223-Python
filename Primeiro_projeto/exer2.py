def f1():
    nmr1 = float(input("Introduza um numero:"))
    nmr2 = float(input("Introduza outro numero:"))
    if nmr1 > nmr2:
        return f"o nmr maior é {nmr1}"
    elif nmr1 == nmr2:
        return "Os nmr são iguais"
    else:
        return f"o nmr maior é {nmr2}"



def f2():
    nmr1 = float(input("Introduza um numero:"))
    if nmr1 >= 0:
        return f"o nmr é positivo"
    else:
        return f"o nmr é negativo"




def f3():
    sex = input("Introduza o seu sexo (F/M):")
    if sex == "F":
        return "Feminino"
    elif sex == "M":
        return "Masculino"
    else:
        return "Sexo Invalido"




def f4():
    vowel = ["a", "e", "i", "o", "u"]
    letter = input("Introduza uma letra:")
    if letter in vowel:
        return "A letra é uma vogal"
    else:
        return "A letra é uma consoante"




def f5():
    note1 = float(input("Introduza a primeira nota:"))
    note2 = float(input("Introduza a segunda nota:"))
    average = (note1 + note2) / 2
    if average >= 7:
        return "Aprovado"
    elif average == 10:
        return "Aprovado top"
    else:
        return "Reprovado"



def f6():
    nmr1 = float(input("Introduza um 1º número:"))
    nmr2 = float(input("Introduza um 2º nmr:"))
    nmr3 = float(input("Introduza um 3º nmr:"))
    lista = [nmr1, nmr2, nmr3]
    return max(lista)


def f7():
    nmr1 = float(input("Introduza um 1º número:"))
    nmr2 = float(input("Introduza um 2º nmr:"))
    nmr3 = float(input("Introduza um 3º nmr:"))
    lista = [nmr1, nmr2, nmr3]
    return f"O maior nmr é {max(lista)} e o menor é {min(lista)}"



def f8():
    prdt1 = float(input("Introduza o Preço do Produto 1:"))
    prdt2 = float(input("Introduza o Preço do Produto 2:"))
    prdt3 = float(input("Introduza o Preço do Produto 3:"))
    if prdt1 > prdt2:
        prdt1 = prdt2
    elif prdt1 > prdt3:
        prdt1 = prdt3
    return f"O produto aconselhado a comprar é o prdt com o preço de {prdt1}"


def f9():
    nmr1 = float(input("Introduza um 1º número:"))
    nmr2 = float(input("Introduza um 2º nmr:"))
    nmr3 = float(input("Introduza um 3º nmr:"))
    ordem =[nmr1, nmr2, nmr3]
    return sorted(ordem)


def f10():
    turno = str(input("Em que turno trabalha? "))
    if (turno == "M"):
        return "Bom dia!"
    elif (turno == "T"):
        return "Boa tarde!"
    elif (turno == "N"):
        return "Boa noite!"
    else:
        return "Valor Invalido"






