import modelos as m
import datetime

"""





    idade: int

    comestivel: bool

"""

f1 = m.Fruta("Verde", "10", "Oval", "Pera", 1, "lisa", True)
f2 = m.Fruta("Azul", 10, "Oval", "Morango", 1, "lisa", True)
f3 = m.Fruta(nome="Laranja",
             cor="Roxa",
             textura="bla bla bla",
             tamanho=10,
             formato="Oval",
             idade=1,
             comestivel=True)

f4 = m.Fruta("Maça", "Vermalha", 10)
f5 = m.Fruta("Maça", "Vermalha", 10, textura="Lisa")

print(f5)

print("----" * 10)
f12 = f1

print(f1)
print(f12)

f12.nome = "Ana"

print(f12)
print(f1)

print("----" * 10)

g = m.Gato("Tom", 20)
g2 = m.Gato("Tom2", 20)

g.peso = 10
print(g.peso)
# print(g2.peso)

print(dir(g))
print(dir(g2))

g = m.Gato("gato 1", 20)
g2 = m.Gato("gato 2", 20)
f1 = m.Fruta("cor 1", "10", "Oval", "Pera", 1, "lisa", True)
f2 = m.Fruta("cor 2", 10, "Oval", "Morango", 1, "lisa", True)

l = [f1, f2, g, g2]

for item in l:
    print(item.comestivel)