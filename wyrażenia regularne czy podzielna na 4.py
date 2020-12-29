import re

def is_div_four(numer):
# pattern = r'-?\d*[4|8|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96|00]' #moja metoda, też dobra
# ""
# pierwsza cyfra jest nieparzysta (1, 3, 5, 7 lub 9), a druga to 2 lub 6
# pierwsza cyfra jest parzysta (0, 2, 4, 6 lub 8), a druga to 0, 4 lub 8
        pattern = r'-?([13579][26]|[02468][048]|[048])'
        return bool(re.fullmatch(pattern, numer_str))

#test = input('Podaj liczbę by dowiedzieć się, że jest podzielna na 4:\n')
# print(is_div_four(numer))

test = ["8", "42","60", "757465", "2036", "1100", "-12"]
for numer_str in test:
    print(numer_str, is_div_four(numer_str))



