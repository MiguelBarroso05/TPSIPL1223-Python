import exer5 as ex
# ----------------------------------------------------------
cor = input("digite a cor: ")
circ = float(input("digite a circunferência: "))
material = input("Qual o material: ")

bola = ex.Bola(cor, circ, material)

print("---" * 10)
bola.mostraCor()

print("---" * 10)
nova_cor = input("digite a nova cor: ")
bola.trocaCor(nova_cor)
bola.mostraCor()
# ----------------------------------------------------------
lado = float(input("digite o tamanho do lado do quadrado"))
quadrado1 = ex.Quadrado(lado)
Quadrado.mostra_valor()
