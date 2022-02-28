import pandas as pd
import csv
def CategorieTask():
    Categ_Task_1 = input("Introduceti prima categorie de taskuri: ")
    Categ_Task_2 = input("Introduceti a 2 a categorie de taskuri: ")
    Categ_Task_3 = input("Introduceti a 3 a categorie de taskuri: ")
    Categ_Task_4 = input("Introduceti a 4 a categorie de taskuri: ")

    lista_categorii_task = [{Categ_Task_1}, {Categ_Task_2}, {Categ_Task_3}, {Categ_Task_4}]

    with open('to-do-categ.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for Catergorie in lista_categorii_task:
            csv_writer.writerow(Catergorie)

    pd_variavbila = pd.Series(lista_categorii_task)

    if Categ_Task_1 == Categ_Task_2:
        print("Categoriile trebuie sa fie diferite!")
    elif Categ_Task_1 == Categ_Task_3:
        print("Categoriile trebuie sa fie diferite!")
    elif Categ_Task_1 == Categ_Task_4:
        print("Categoriile trebuie sa fie diferite!")
    elif Categ_Task_2 == Categ_Task_3:
        print("Categoriile trebuie sa fie diferite!")
    elif Categ_Task_2 == Categ_Task_4:
        print("Categoriile trebuie sa fie diferite!")
    elif Categ_Task_3 == Categ_Task_4:
        print("Categoriile trebuie sa fie diferite!")
    else:
        return pd_variavbila

def Cerinte():
    Cerinte = input("Doriti sa introduceti elemente in categorie?(1/0-->{DA/NU}): ")
    while Cerinte == 1:
        inputtask = input("Introduceti task: ")
        data_limita = str(input("Introduceti data limita task: "))
        presoana_responsabila = input("Introduceti persoana responsabila: ")

        dictrionar_cerinte = {
            "Tasks": [{inputtask}],
            "Deadline": [{data_limita}]
        }
        pd_cerince = pd.DataFrame(dictrionar_cerinte, index=[presoana_responsabila])
        print(pd_cerince)

Start = input("Doriti sa creati un To-Do list?(y/n): ")
if Start == "y":
    CategorieTask()
    Cerinte()
else:
    print("La revedere!")

