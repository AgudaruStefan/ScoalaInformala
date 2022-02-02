# 2 variabile
# 1 operator
# 1 rezultat

def suma(a: int, b: int) -> str:
    return f"{a} + {b} =  {a + b}"


def deferenta(a: int, b: int) -> str:
    return f"{a} - {b} =  {a - b}"


def inmultire(a: int, b: int) -> str:
    return f"{a} * {b} =  {a * b}"


def impartire(a: int, b: int) -> str:
    if b == 0:
        while b == 0:
            b = int(input("Aloca o noua valoare pentru b: "))
    return f"{a} / {b} = {a / b}"


def operator() -> str:
    op = input("Alege operatorul: ")
    if op in ['*', '/', '+', '-']:
        return op
    else:
        while op not in ['*', '/', '+', '-']:
            op = input("Alege operatorul: ")
        return op


def calcualtor():
    nr1 = int(input("primul numar: "))
    nr2 = int(input("Al doilea numar: "))
    op = operator()
    if op == "+":
        rezultat = suma(nr1, nr2)
    elif op == "-":
        rezultat = deferenta(nr1, nr2)
    elif op == "*":
        rezultat = inmultire(nr1, nr2)
    else:
        rezultat = impartire(nr1, nr2)
    return rezultat

print(calcualtor())
