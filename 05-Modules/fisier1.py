# import primul_nostru_modul
#
# if ___name__ == "__main__":
#      print(primul_nostru_modul.my_sum(1, 4))






# from primul_nostru_modul import my_sum as suma
#
# if ___name__ == "__main__":
#     print(suma(4, 5))


my_var = input("Numar intreg: ")
my_int = None
try:
    my_int = int(my_var)
except Exception as e:
    my_int = "test"
    print(("Exception generica"), e)
else:
    print("Daca nu apare exceptie ", my_int)
finally:
    my_int = "www"
    print("Afiseaza in orice caz")
print(my_int)