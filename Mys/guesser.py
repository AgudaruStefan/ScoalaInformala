import random
def GhicesteNum():
    nr_incercari = 0
    nr_calculator = random.randint(1, 20)
    while True:
        nr_incercari += 1
        userImput2 = input('Ghiceste numarul ales de catre calculator(intre 1 si 20): ')
        if userImput2.isdigit():
            userImput2 = int(userImput2)
        else:
            print('scrie un numar!')
            continue

        if userImput2 > nr_calculator:
            print("Prea mult! Mai scade!")
        elif userImput2 < nr_calculator:
            print('Mai baga vere!')
        elif userImput2 == nr_calculator:
            print(f'L-ai ghicit! Bravo! --- Numar de incercari:{nr_incercari}')
            break

if __name__ == "__main__":
    userImput1 = input('Vrei sa joci "Ghiceste numarul"?(Da/Nu): ')
    if userImput1 == "da":
        GhicesteNum()
    print('La Revedere!')


