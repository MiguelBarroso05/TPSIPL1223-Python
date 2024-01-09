def ola_mundo():
    txt_mundo = "ola Mundo"
    return txt_mundo


print(ola_mundo())


def numero_input():
    nmr = input("digite um numero: ")

    nmr2 = f"o numero inserido foi : {nmr}"
    return nmr2


print(numero_input())


def soma():
    nmr3 = int(input("digite o primeiro numero da soma: "))
    nmr4 = int(input("digite o segundo numero da soma: "))
    resultado = nmr3 +  nmr4
    return resultado


print(soma())


def notas():
    note1 = float(input("insira a primeira nota: "))
    note2 = float(input("insira a segunda nota: "))
    note3 = float(input("insira a terceira nota: "))
    note4 = float(input("insira a quarta nota: "))
    media = (note1 + note2 + note3 + note4) / 4
    return f"a media é: {media} "


print(notas())


def metros():
    medida_m = float(input("insira uma medida em m: "))
    medida_cm = medida_m * 100
    return f"{medida_m}m são {medida_cm} cm"


print(metros())


def area_circulo():
    raio = float(input("digite o raio do circulo: "))
    area_circ = (raio ** 2) * 3.14
    return f"A area do circulo é: {area_circ}"


print(area_circulo())


def area_quadrado():
    lado = float(input("indique a medida da aresta:"))
    area2 = (lado ** 2) * 2
    return f"O dobro da area do quadrado é : {area2}"


print(area_quadrado())