# 1. Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7].
# Sa se insereze in acest sir dupa fiecare element par, dublul acestuia (2 puncte)
n = [1, 2, 3, 4, 5, 6, 7]
# def DubluPar(n):
#
#     while len(n) != 10:
#         print(n[1::2])
#         for i in n[1::2]:
#             n.insert(i, i*2)
#         print(n)
#     return "DubluPar Gata"
#
# print(DubluPar(n))


def DubluPar(n):
    n.insert(2,4)
    n.insert(5,8)
    n.insert(8,12)
    print(n)


print(DubluPar(n))