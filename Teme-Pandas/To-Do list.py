import csv
import datetime

def makeCateg():
    sequentz = True
    while sequentz:
        firstQ = input('Doriti sa introduceti o categorie(y/n): ')
        if firstQ.lower() != "n":
            lista_categorii_task = [[input("Introduceti categoria: ")]]
            with open('datacategorii.csv', 'a') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                for categorie in lista_categorii_task:
                    csv_writer.writerow(categorie)
        elif firstQ.lower() == "n":
            sequentz = False

def TaskOK(task):
    with open("cerinte.txt", "r") as file:
        for line in file.readlines():
            if task in line:
                print("Task ul este deja introdus!")
                return False
        return True

def taskinCateg():
    inputForTask = input("Doriti sa introduceti un task nou?(y/n): ")
    while inputForTask != 'n':
        with open("cerinte.txt", "a") as file:
            task = input("Introduceti taskul: ")
            if TaskOK(task) == False:
                break

            datalimita = input("Introduceti data limita task ului introdus: ")
            try:
                datetime.datetime.strptime(datalimita, "%d.%m.%Y")
            except ValueError as e:
                print('Data invalida!', e)
                break

            oralimita = input("Introduceti ora limita task ului introdus: ")
            try:
                datetime.datetime.strptime(oralimita, "%H:%M")
            except ValueError as e:
                print('Ora invalida!', e)
                break

            responsabilTask = input("Introduceti numele persoanei resposabile cu task ul introdus: ")

            categfortask = input("Introduceti categoria aferenta task ului introdus: ")

            file.write(task)
            file.write(", ")
            file.write(datalimita)
            file.write(", ")
            file.write(oralimita)
            file.write(", ")
            file.write(responsabilTask)
            file.write(", ")
            file.write(categfortask)

            inputForTask = input("Doriti sa introduceti un task nou?(y/n): ")
            if inputForTask == "y":
                file.write("\n")

def listare_date():
    with open("cerinte.txt", "r") as file:
        citire = file.readlines()

        for i in sorted(citire, key=lambda i: i.split(",")[3]):
            print(i)


def asc_data():
    with open("cerinte.txt", "r") as file:
        for line in file:
            data = line.split('|')
            sorted_data = sorted(data, key=lambda line: line[1],)
            print(sorted_data)

def desc_data():
    with open("cerinte.txt", "r") as file:
        for line in file:
            data = line.split('|')
            sorted_data = sorted(data, key=lambda line: line[1], reverse=True)
            print(sorted_data)


def asc_responsabil():
    with open("cerinte.txt", "r") as file:
        citire = file.readlines()

        for i in sorted(citire, key=lambda i: i.split(",")[2]):
            print(i)

def desc_responsabil():
    with open("cerinte.txt", "r") as file:
        citire = file.readlines()

        for i in sorted(citire, key=lambda i: i.split(",")[2], reverse=True):
            print(i)

def Menu():
    print("0.Iesire\n")
    print("1.Listare date\n")
    print("2.Creare categorie\n")
    print("3.Creare task\n")
    print("4.Sortare ascendentă data\n")
    print("5.Sortare descendentă data\n")
    print("6.Sortare ascendentă persoana responsabila\n")
    print("7.Sortare descendentă persoana responsabila\n")

    actiuni = {
        "0": exit,
        "1": listare_date,
        "2": makeCateg,
        "3": taskinCateg,
        "4": asc_data,
        "5": desc_data,
        "6": asc_responsabil,
        "7": desc_responsabil,
    }

    numMenu = "8"

    while numMenu != "0":
        numMenu = input("Introduceti numarul operatiei: ")
        actiuni[numMenu]()

Menu()