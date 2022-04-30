#                                           Mid_Test
# 1. Scrie un program care sa calculeze suma dintre trei numere. Daca valorilesunt egale,
# returnati de trei ori suma acestora.(1 punct)

def my_sum(a, b, c):
    if a == b == c:
        return (a + b + c)*3
    else:
        return a + b + c


print(my_sum(2, 2, 2))
print(my_sum(1, 2, 3))
