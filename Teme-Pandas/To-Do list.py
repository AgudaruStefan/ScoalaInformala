import pandas as pd
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
    inputForTask = input("Doriti sa introduceti un nou(y/n): ")
    while inputForTask != 'n':
        with open("cerinte.txt", "w,r") as file:
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
            file.write(datalimita)
            file.write(oralimita)
            file.write(responsabilTask)
            file.write(categfortask)
            