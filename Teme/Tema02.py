def functie(*args):
    sum = 0
    for i in args:
        if type(i) == int:
            sum = sum + i

    print(sum)


functie(1, 5, -3, 'abc', [12, 56, 'cad'])


def functie_2(*args, param_a):
    sum2 = 0
    for i in args:
        try:
            sum2 = sum2 + int(i)
        except ValueError:
            pass
        except TypeError:
            pass

    print(sum2)


functie_2(2, 4, 'abc', param_a=2)


def functie_3():
    numar_introdus = input("Introdu o valoare: ")
    valoare_1 = numar_introdus
    if valoare_1.isnumeric():
        print(valoare_1)
    else:
        print("0")


print(functie_3())