
def f1():
    listapar= []
    listaimpar= []
    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    """"
    for i in range(20):
        lista.append(int(input("indique numr: ")))
    """
    for i in lista:
        if i % 2 == 0:
            listapar.append(i)
        else:
            listaimpar.append(i)
    print(lista)
    print(listapar)
    print(listaimpar)
    print("-" * 60)


f1()


def f2():
    lista1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    lista2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    lista3 = []
    for i in range(10):
        lista3.append(lista2[i])
        lista3.append(lista1[i])
    print(lista3)


months = ["janeiro", "feveiro", "março", "abril", "maio","junho",
          "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
lst_temp = [12, 25, 17, 40,  37, 24, 11, 30, 35, 29, 36, 33]
lst_bigger = []
soma = sum(lst_temp)
avarage = soma / len(lst_temp)
print(soma)
print(round(avarage))
for i in lst_temp:
    if i > avarage:
        lst_bigger.append(i)
print(lst_bigger)
for j in range(len(lst_bigger)):
    for k in range(len(lst_temp)):
        if lst_bigger[j] == lst_temp[k]:
            print(lst_temp.index(lst_temp[k]) + 1, months[lst_temp.index(lst_temp[k])])


