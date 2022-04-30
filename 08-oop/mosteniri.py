def control(self):
    cnpbst = int(self.cnp[-1])
    cast = '279146358279'
    rod = 0
    for x, y in enumerate(cast):
        rod += int(y) * int(self.cnp[x])
    intro = rod % 11
    if intro == 10:
        intro = 1
    else:
        intro = intro == int(intro)
    if cnpbst == intro:
        print('control ok')
    else:
        print('control nasol')