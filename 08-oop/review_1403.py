# class ClasaMea:
#
#     gamma = 0
#
#     def __init__(self):
#         self.alpha = 1
#         self.__delta = 3
#
#
# obj = ClasaMea()
# obj.beta = 2
# print(obj)


class Catalog:

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.absente = 0
        self.materii = {}

    def __str__(self):
        return f"{self.nume} {self.prenume} \n \t materii si note:{self.materii} \n \t absente: {self.absente}"

    def increment_abs(self):
        self.absente +=1

    def delete_abs(self, numar_abs):
        if self.absente > 0:
            self.absente -= numar_abs


class Extensie1(Catalog):
    def __init__(self,nume, prenume):
        super().__init__(nume, prenume)

    def add_subject(self, materie, note):
        self.materii.update({materie:note})
        self.note = note

student = Catalog("Roata", "Ion")
print(student)
student.increment_abs()
student.increment_abs()
student.increment_abs()
print(student)
student.delete_abs(2)
print(student)

student2 = Catalog("Cerc", "George")
print(student2)
student2.increment_abs()
student2.increment_abs()
student2.increment_abs()
student2.increment_abs()
print(student2)
student2.delete_abs(2)
print(student2)

obj = Extensie1("Ana", "Maria")
obj.add_subject("Python", [5, 7, 8])
print(obj)