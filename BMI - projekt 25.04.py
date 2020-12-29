#Problem do rozwiązania: Policzenie BMI. Program pobiera wzrost i wagę. BMI= masa/wzrost do kwadratu


masa = int(input("Podaj masę w kg: "))
wzrost = float(input("Podaj swój wzrost w (m): "))

B
MI = (masa // (wzrost ** 2))

print(f"Twoje BMI wynosi {BMI}, masz")

if BMI < 16.99:
    print('wychudzenie')
elif BMI < 18.49:
    print('niedowagę')
elif BMI < 24.99:
    print('prawidłową wagę')
elif BMI < 29.99:
    print('nadwagę')
elif BMI < 34.99:
    print('otyłość I stopnia')
elif BMI < 39.99:
    print('otyłość II stopnia')
else:
    print ('otyłość II stopnia')
