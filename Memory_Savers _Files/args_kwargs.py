# def my_function(*param_1):
#     print(type(param_1))
#     return param_1
#
#
#
# print(my_function("string", "string1", "string2"))

# def numbers_sum(param1, *var):
#     suma = 0
#     for item in var:
#         suma = suma + item
#     return suma
#
# print(numbers_Sum(1, 2, 3, 4, 5, param=1))

# def diff_vars(a, *params):
#     diferenta = a
#     for item in params:
#         diferenta = diferenta * item
#     return diferenta
#
# print(diff_vars(1, 2, 3, 4))



def catalog(**kwargs):
    return kwargs.keys()

print(catalog(nume="Popa", prenume="Ionut", varsta="12"))