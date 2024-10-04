#kalkulator

while True:
    x=float(input('Wprowadz liczbe x: '))
    y=float(input('Wprowadz liczbe y: '))

    dzialanie = input("wybierz dzialanie  + - * /")

    while True:
        if dzialanie == '+':

            wynik = x + y
            print(wynik)
            break

        elif dzialanie == '-':
            wynik = x - y
            print(wynik)
            break
        elif dzialanie == '*':
            wynik = x * y
            print(wynik)
            break
        elif dzialanie == '/':
            if y==0:
                print("nie dziel przez zero")
                y=float(input('wstaw poprawna liczbe y: '))

            else:
                wynik = x / y
                print(wynik)
                break
        else:
            dzialanie=input("wybierz poprawne dzialanie")
            continue


    czy_ponownie_skorzystac=input("czy chcesz skorzystac z kallkulatora jeszcze raz? t/n")
    if czy_ponownie_skorzystac == 't':
        continue
    else:
        break




