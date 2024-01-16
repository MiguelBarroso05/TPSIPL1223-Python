def nmrmaior():
    nmr1 = float(input("Introduza um numero:"))
    nmr2 = float(input("Introduza outro numero:"))
    if nmr1 > nmr2:
        return f"o nmr maior é {nmr1}"
    elif nmr1 == nmr2:
        return "Os nmr são iguais"
    else:
        return f"o nmr maior é {nmr2}"


print(nmrmaior())


def positivo_negativo():
    nmr1 = float(input("Introduza um numero:"))
    if nmr1 >= 0:
        return f"o nmr é positivo"
    else:
        return f"o nmr é negativo"


print(positivo_negativo())


def sex_verification():
    sex = input("Introduza o seu sexo (F/M):")
    if sex == "F":
        return "Feminino"
    elif sex == "M":
        return "Masculino"
    else:
        return "Sexo Invalido"


print(sex_verification())


def volgal_consoante():
    vowel = ["a", "e", "i", "o", "u"]
    letter = input("Introduza uma letra:")
    if letter in vowel:
        return "A letra é uma vogal"
    else:
        return "A letra é uma consoante"


print(volgal_consoante())


def aproved_or_not():
    note1 = float(input("Introduza a primeira nota:"))
    note2 = float(input("Introduza a segunda nota:"))
    average = (note1 + note2) / 2
    if average >= 7:
        return "Aprovado"
    elif average == 10:
        return "Aprovado top"

    else:
        return "Reprovado"


print(aproved_or_not())


def three_numbers_max():
    nmr1 = float(input("Introduza um 1º número:"))
    nmr2 = float(input("Introduza um 2º nmr:"))
    nmr3 = float(input("Introduza um 3º nmr:"))
    list = [nmr1, nmr2, nmr3]
    return max(list)


print(three_numbers_max())


def min_three_number():
    nmr1 = float(input("Introduza um 1º número:"))
    nmr2 = float(input("Introduza um 2º nmr:"))
    nmr3 = float(input("Introduza um 3º nmr:"))
    list = [nmr1, nmr2, nmr3]
    return f"O maior nmr é {max(list)} e o menor é {min(list)}"


print(min_three_number())
