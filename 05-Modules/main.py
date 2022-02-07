# print()     #str
# input()     #str
# "".format() #str

# def functie2():
#     my_function()
#
#
# def my_function():
#     # function body
#     # return None
#     pass
#
#
# print(my_function())


# def message():
#     print("Enter a value")
# #
# # message()
#
# def yourfunction(x: str) -> str:
#     # print("Hello", x)
#     return x
#
# name = input("Numele meu este: ")
# yourfunction(name)


# def my_function(a: str, b: str, c: str) -> (str, str, str):
#     return a, b ,c

# print(my_function(a="1" , b="2", c="3"))
# print(my_function("1", "2", "3"))
#print(my_function("3", a="1" ,b="2")) nu e corect

# def my_function():
#     pass
#
# a = my_function()
# print(a)
# b = None
# print(type(b))

# def my_function(n: int) -> bool
#     if n % 2 == 0:
#         return True
#     return False
#
# # print(my_function(3))
# nr = input("Introdu un nr: ")
# if my_function(int(nr)) is True
#     print("Nr este divizibil")
# elif my_function(int(nr)) is False:
#     print("Nr nu este divizibil")
#
# var = 1
# def my_function():
#     global var
#     var = 2
#     return F"Cunosti aceasta variabila: {var}"
#
# print(my_function())
# print(var)
#
# lista = [1, 2, 3, [4, 5, [6, 7]]]
#
# print(lista[3][2][1])

# try:
#     bloc de expresii
# except:
#     daca apare o exceptie si vrem sa afisam ceva

try:
    valoare = int(input("Prima cifra din cnp: "))
except ValueError:
    print("Ai introdus o litera in loc de cifra")
