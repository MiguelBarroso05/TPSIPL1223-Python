
def min_three_number():
    nmr1 = float(input("Introduza um 1º número:"))
    nmr2 = float(input("Introduza um 2º nmr:"))
    nmr3 = float(input("Introduza um 3º nmr:"))
    list = [nmr1, nmr2, nmr3]
    return f"O maior nmr é {max(list)} e o menor é {min(list)}"


print(min_three_number())
