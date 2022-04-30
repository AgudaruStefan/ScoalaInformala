#                                           Mid_Test
# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. (1 punct)
#
lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def elimination(lista):

    while lista != []:
        print(f'elemente sterse: {lista[::3]}')
        for i in lista[::3]:
            lista.remove(i)
        print(f'lista: {lista}')
    return f'lista goala'

print(elimination(lista))



