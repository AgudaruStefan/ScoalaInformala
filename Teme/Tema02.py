# 1:

def functie(*args):
    sum_1 = 0
    for i in args:
        if type(i) == int:
            sum_1 = sum_1 + i

    print(sum_1)
functie(1, 5, -3, 'abc', [12, 56, 'cad'])

# 2:
def functie_0():
    return 0
print(functie_0())


# 3:
def functie_2(*args, param_a):
    sum_2 = 0
    for i in args:
        try:
            sum_2 = sum_2 + int(i)
        except ValueError:
            pass
        except TypeError:
            pass

    print(sum_2)
functie_2(2, 4, 'abc', param_a=2)
# 4:
def functie_3():
    numar_introdus = input("Introduceti o valoare: ")
    valoare = numar_introdus
    if valoare.isnumeric():
        print(valoare)
    else:
        print("0")

print(functie_3())
