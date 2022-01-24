#                                                  Tema 1

# 1.Declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).

lista_1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# 2.Afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă).

print(sorted(lista_1))

# 3.Afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă).

print(sorted(lista_1, reverse=True))

# 4.Afișează o listă ce conține numerele pare din lista ordonată (folosind slice).

lista_2 = sorted(lista_1)

print(lista_2[1::2])

# 5.Afișează o listă ce conține numerele impare din lista ordonată (folosind slice).

print(lista_2[::2])

# 6.Afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).

print(lista_2[2::3])

# Lista initiala

print(lista_1)
