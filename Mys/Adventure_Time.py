nume_utilizator = input("Care este numele tau: ")
nr_vieti = 5
Game_Start = input(f'Salut {nume_utilizator}, ai inceput aventura cu {nr_vieti} vieti iar in momentul de fata te afli la iesirea unui templu. '
                   f'Ai de ales\n'
      f'dintre a merge pe poteca intunecoasa din dreapta sau pe cea luminoasa din stanga.Fa o alegere!(Dreapta/Stanga):').lower()
if Game_Start == "dreapta":
    nr_vieti -= 1
    dreapta2 = input(f'Ai ales poteca dreapta. Pe poteca dreapta ai fost atacat de catre un trol si ti a furat o viata! '
                     f'Acum mai ai {nr_vieti} vieti.\n'
                     f'Dupa ce ai fost atacat de trol in ai zarit un iaz si o pestera.\n'
                     f'Din iaz poti bea apa iar din pestera ai auzit un sunet ciudat. Vrei sa mergi la iaz sau pestera?(iaz/pestera):').lower()
    if dreapta2 == 'iaz':
        nr_vieti -=1
        dreapta_apa = input(f'{nume_utilizator}, ai ales sa mergi la iaz si sa bei apa. Ceea ce nu stiai este ca apa era otravita ceea ce inseamna '
                            f'ca acum ai {nr_vieti} vieti.\n Poti alege sa continui drumul sau sa intrii in pestera(continua/pestera): ').lower()

        if dreapta_apa == 'pestera':
            nr_vieti += 1
            drum_pestera = input('Ai intrat in pestera si ai gasit un mag care ti a redat o viata inapoi. Poti continua drumul prin pestera\n'
                                 'sau poti iesii.(pestera/afara): ')
            if drum_pestera == 'afara':
                print(f'Felicitari {nume_utilizator} ai ajuns la capatul aventurii cu {nr_vieti} vieti')
            elif drum_pestera == 'pestera':
                print('Ai ales sa continui prin pestera iar magul care ti a dat o viata inapoi ti a luat toate vietile pentru a nu afla\n'
                      'ce se ascunde in pestera!')
        elif dreapta_apa == 'continua':
            nr_vieti -= 4
            print('La acest stagiu din poveste ai ramas fara vieti pentru ca apa pe care ai baut o ti a afectat si celelalte vieti!')
    elif dreapta2 == 'pestera':
        nr_vieti += 1
        drum_pestera2 = input(
            'Ai intrat in pestera si ai gasit un mag care ti a redat o viata inapoi. Poti continua drumul prin pestera '
            'sau poti iesii.(pestera/afara): ')
        if drum_pestera2 == 'afara':
            print(f'Felicitari {nume_utilizator} ai ajuns la capatul aventurii cu {nr_vieti} vieti')
        elif drum_pestera2 == 'pestera':
            print(
                'Ai ales sa continui prin pestera iar magul care ti a dat o viata inapoi ti a luat toate vietile pentru a nu afla'
                'ce se ascunde in pestera!')
elif Game_Start == "stanga":
    pass