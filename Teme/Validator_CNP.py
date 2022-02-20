import random
def CNP():
    user_input = input("Introduceti CNP: ")

    tup_1 = user_input[0]
    tup_2 = user_input[1:3]
    tup_3 = user_input[3:5]
    tup_4 = user_input[5:7]
    tup_5 = user_input[7:9]
    tup_6 = user_input[9:12]
    tup_7 = user_input[-1]

    tup_1_verified = "1" <= tup_1 <= "9"
    tup_2_verified = "00" <= tup_2 <= "99"
    tup_3_verified = "01" <= tup_3 <= "12"
    tup_4_verified = "01" <= tup_4 <= "31"
    tup_5_verified = "01" <= tup_5 <= "51"
    tup_6_verified = "001" <= tup_6 <= "999"

    c_intup = 0
    ex_numar = '279146358279'
    for intup, anyin in enumerate(user_input[:12]):
        c_intup += int(anyin) * int(ex_numar[intup])
    c_intup = c_intup % 11
    if c_intup == 10:
        c_intup = 1
    tup_7_verified = c_intup == int(tup_7)

    if len(user_input) == 13 \
            and tup_1_verified \
            and tup_2_verified \
            and tup_3_verified \
            and tup_4_verified \
            and tup_5_verified \
            and tup_6_verified \
            and tup_7_verified:
        print("CNP-ul introdus este valid!")
    else:
        print("CNP-ul introdus este invalid")

CNP()