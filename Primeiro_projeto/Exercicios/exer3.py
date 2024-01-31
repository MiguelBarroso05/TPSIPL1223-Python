def f1():
    nota = float(input("Insira uma nota (entre 0 a 10): "))
    while 0 <= nota <= 10:
        return nota
    print("Insira uma nota valida!")
    return f1()


def f2():
    user = input("indique o seu username: ")
    password = input("indique a sua password: ")
    while user != password:
        return user, password
    print("ERROR PASSWORD MUST BE DIFERENT FROM USERNAME!!!")
    return f2()


def f3():
    name = input("insira o seu nome: ")
    age = int(input("insira a sua idade: "))
    salary = float(input("Insira o seu salario: "))
    sex = input("Insira o seu sexo (f, m): ")
    married = input("Indique o seu estado civil (s, c, v, d): ")
    while len(name) < 3 and 150 > age > 0 > salary and sex == ("f", "m") and married == ("s", "c", "v", "d"):
        return name, age, salary, sex, married
    print("Erro um dos valores invalidos!!!")
    f3()


def f4():
    pais_a = 80000
    pais_b = 200000
    n = 0
    while pais_a < pais_b:
        pais_a *= 1.03
        pais_b *= 1.015
        n += 1
    return n


def f5():
    pais_a = float(input("Insira a populaçao do primeiro pais: "))
    taxa_a = float(input("Insira a taxa de crescimento do primeiro pais (em %): "))
    pais_b = float(input("Insira a populaçao do segundo pais: "))
    taxa_b = float(input("Insira a taxa de crescimento do segundo pais (em %): "))
    taxa_a = taxa_a/100 + 1
    taxa_b = taxa_b / 100 + 1
    n = 0
    while pais_a <= pais_b:
        pais_a *= taxa_a
        pais_b *= taxa_b
        n += 1
    return n