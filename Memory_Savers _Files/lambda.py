# my_lambda = lambda x, y: x + y
# my_sum = my_lambda(2, 3)
# print((my_sum))



# diferenta = lambda x, y: x - y
# my_dif = diferenta(4, 3)
# print(my_dif)

players = [{
    "first_name": "Ion",
    "last_name": "Gheorhe",
    "varsta": 12
}, {
    "first_name": "Andreea",
    "last_name": "Popa",
    "varsta": 35

}, {
    "first_name": "Isabela",
    "last_name": "Enache",
    "varsta": 25
    }




]


jucatori_sortati = sorted(players, key=lambda jucator: jucator["last_name"])
print(jucatori_sortati)