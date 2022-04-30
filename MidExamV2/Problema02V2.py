# 2. Sa se scrie un program care sa calculeze impartirea dintre trei numere.
# Daca valorile sunt egale, returnati de trei ori rezultatul.
# Impartirea la 0 va duce la rezultatul 0. (1 punct)

def impart(x, y, z):
    if x == y == z:
        return f'Rezultatul este: {(x/y/z)*3}'
    elif x == 0 or y == 0 or z == 0:
        return "Rezultatul este 0"
    return f'Rezultatul este: {x/y/z}'

print(impart(4, 4, 4))

