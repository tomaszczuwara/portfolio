import random
gramy = True
mozliwosci = ['papier', 'nozyce', 'kamien']


while gramy:
#wybór przez indeks
  #  indeks = random.randint(0,2)
   # print(indeks)
    # komputer = mozliwosc[indeks]
    # wybor_gracza = input('Podaj papier/nozyce/kamien'.lower()
    komputer = random.choice(mozliwosci)
    wybor_gracza = input("Podaj papier/nozyce/kamien").lower()

    if wybor_gracza not in mozliwosci:
        print('podaj ponownie')
        continue
    if wybor_gracza == komputer:
        print ('Remis')
    elif wybor_gracza == 'nozyce' and komputer == 'papier':
        print('Win')
    elif wybor_gracza == 'nozyce' and komputer == 'kamien':
        print('Przegrałes')
    elif wybor_gracza == 'papier' and komputer == 'kamien':
        print ('Przegrales')
    elif wybor_gracza == 'papier' and komputer == 'nozyce':
        print('Win')
    elif wybor_gracza == 'kamien' and komputer == 'nozyce':
        print ('Win')
    elif wybor_gracza == 'kamien' and komputer == 'papier':
        print('Przegrales')
    else:
        print('invalid input')
        continue
    gramy_dalej = input("WYbierz \'t\' jesli chcesz grac dalej")
    if gramy_dalej == 't':
        continue
    else:
        break