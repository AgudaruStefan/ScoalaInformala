from operator import itemgetter


class Catalog_Prajituri():
    lista_prajituri = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        caracteristici_obiect = [self.nume, self.pret, self.gramaj]
        self.lista_prajituri.append(caracteristici_obiect)

    @staticmethod
    def sortare_pret():
        sortare_pret = sorted(Catalog_Prajituri.lista_prajituri, key=itemgetter(2))
        return f"Prajiturile sortate dupa pret sunt {sortare_pret}"

    @staticmethod
    def sortare_gramaj():
        sortare_gramaj = sorted(Catalog_Prajituri.lista_prajituri, key=itemgetter(3))

class Tort(Catalog_Prajituri):
    def __init__(self, nume, pret, gramaj):
        super().__init__(nume, prenume)

prj1 = Catalog_Prajituri("Eclere", 10, 500)
prj2 = Catalog_Prajituri("Ecler mic", 7, 115)
prj3 = Catalog_Prajituri("Lavacake", 15, 324)

print(Catalog_Prajituri.lista_prajituri)

print(Catalog_Prajituri.sortare_pret())