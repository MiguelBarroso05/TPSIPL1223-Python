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
    area =  lado ** 2
    area2 = (lado ** 2) * 2
    return f"A area do quadrado é {area} \n"  f"O dobro da area do quadrado é : {area2}"


print(area_quadrado())


def salario():
    dinheiro_hora = float(input("introduza o valor/hora: "))
    horas_trabalhadas = float(input("introduza as horas trabalhadas no mês: "))
    salary = dinheiro_hora * horas_trabalhadas
    return f"O seu salario mensal é: {salary}"


print(salario())

def temperatura():
    temp_f = float(input("introduza a temp em Fahrenheit: "))
    temp_c = 5 * ((temp_f - 32) / 9)
    return f"A temperatura em Celsius é: {temp_c}"


print(temperatura())


def temperatura2():
    temp_c2 = float(input("introduza a temp em Celsius: "))
    temp_f2 =((temp_c2 * 9) + 32) / 5
    return f"A temp em Fahrenheit é: {temp_f2}"


print(temperatura2())


def tnumeros():
    nmr1 = float(input("introduza um numero real: "))
    nmr2 = float(input("introduza outro numero real: "))
    nmr3 = int(input("introduza um numero inteiro: "))
    conta1 = (2 * nmr1) * (nmr2 * 0.5)
    conta2 = (3 * nmr1) + nmr3
    conta3 = nmr3 ** 3
    return conta1, conta2, conta3


print(tnumeros())


def peso_ideal():
    alt = float(input("introduza a sua altura(m): "))
    peso = (72.7 * alt) -58
    return f"O seu peso ideal é: {peso}"


print(peso_ideal())


def peso_man_woman():
    alt = float(input("introduza a sua altura(m): "))
    sex = input("introduza a seu sexo (h/m): ")
    if sex == "h":
        peso = (72.7 * alt) - 58
    elif sex == "m":
        peso = (62.1 * alt) - 44.7
    else:
      return "sexo invalido"
    return peso


print(peso_man_woman())


def joao_pescador():
    peso_peixe = float(input("Indique em quilos o peso do peixe:"))
    peso_excesso = peso_peixe - 50
    if peso_excesso < 0:
        peso_excesso = 0

    round(peso_excesso, 0)
    multa = 4 * peso_excesso
    return (f"O peso do peixe foi de {peso_peixe}kg\n"
            f"A quantidade foi excedida em {peso_excesso}kg\n"
            f"O valor da sua multa é de {multa}€")


print(joao_pescador())


def salario_mensal():
    money_hour = float(input("introduza o preço/hora: "))
    hours_worked = float(input("introduza o nº de horas trabalhadas no mês: "))
    salario_bruto = money_hour * hours_worked
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato
    return f"+ Salário Bruto : {salario_bruto}€\n- IR (11%) : {ir}€\n- INSS (8%) : {inss}€\n- Sindicato ( 5%) : {sindicato}€\n= Salário Liquido : {salario_liquido}€"


print(salario_mensal())

import math
def tintas():
    metros_pintura = float(input("introduza os metros^2 que deseja printar: "))
    litros_area = metros_pintura / 3
    latas = litros_area /18
    galoes = litros_area/ 3.6
    math.ceil(latas)
    price_latas = latas * 80
    price_galoes = galoes * 25
    price_mix =



