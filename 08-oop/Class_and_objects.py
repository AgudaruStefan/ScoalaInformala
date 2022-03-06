# class MyFirstClass:
#     pass
#
# my_first_object = MyFirstClass()

# class Caine:
#     nr_picioare = 3 # atribut
#
#     def __init__(self, name, age):
#         self.nume = name
#         self.varsta = age
#
#     def __str__(self):
#         return f"{self.nume} - {self.varsta}"
#
#     def change_name(self, name):
#         self.nume = name
#         return ""
#
#
# # print(Caine.nr_picioare)
#
# cainele_meu = Caine("Rex", "2")
# # print(cainele_meu.nume)
# print(cainele_meu.change_name("Ben"))
# print(cainele_meu)

class Calculator:

    def __init__(self, op1, op2, operation):
        self.operator1 = op1
        self.operator2 = op2
        self.operatie = operation


    def adunare(self):
       return self.operator1 + self.operator2

    def __str__(self):
        if self.operatie == "+":
            return f"{self.adunare()}"


obiect_1 = Calculator(1, 2, "+")
print(obiect_1)

