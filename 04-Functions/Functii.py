# print("mesaj")
# format()
# a = input("")
#def functia_mea(param_1):
#    pass

# def suma(a, b, c=3):
#     return a + b + c
#
# variabila_1 = 1
# variabila_2 = 2
#
# total_suma = suma(variabila_1,variabila_2)
# print(total_suma)


def suma(a: int, b: int = 1, c: int = 0) -> (int, int):
    """
    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of params
    """
    return a + b + c, a - b - c

variabila_1 = 1
variabila_2 = 2
sum, dif = suma(a=variabila_1, c=0, b=variabila_2)
print(sum)
print(dif)