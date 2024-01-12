import math


def tintas():
    metros_pintura = float(input("introduza os metros^2 que deseja printar: "))
    litros_area = metros_pintura / 6
    latas = litros_area /18
    galoes = litros_area/ 3.6
    latas_galoes= ((litros_area % 18) / 3.6) * 1.1
    math.ceil(latas)
    math.ceil(galoes)
    math.ceil(latas_galoes)
    print(latas_galoes)
    price_latas = latas * 80
    round(price_latas,2)
    price_galoes = galoes * 25
    price_mix = 0
    print(round(price_latas,2))
print(tintas())