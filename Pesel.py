# Project - 4.04.2022;
# Data based on the PESEL number;

pesel = input('Podaj numer PESEL: ')

if pesel.isnumeric():
    if len(pesel) == 11:
        sex = int(pesel[9])
        if sex % 2 == 0:
            print('Płeć: kobieta')
        else:
            print('Płeć: mężczyzna')

        day_1 = pesel[4]
        day_2 = pesel[5]
        day_birth = int(day_1 + day_2)
        if day_birth < 32:
            print('Dzień urodzenia:', day_birth)
        else:
            print('Dzień urodzenia: BŁĄD NUMERU PESEL - sprawdź poprawność 5 i 6 cyfry numeru.')
        
        month_1 = pesel[2]
        month_2 = pesel[3]
        month_birth = month_1 + month_2
        if month_birth == '01' or month_birth == '21':
            print('Miesiąc urodzenia: styczeń')
        elif month_birth == '02' or month_birth == '22':
            print('Miesiąc urodzenia: luty')
        elif month_birth == '03' or month_birth == '23':
            print('Miesiąc urodzenia: marzec')
        elif month_birth == '04' or month_birth == '24':
            print('Miesiąc urodzenia: kwiecień')
        elif month_birth == '05' or month_birth == '25':
            print('Miesiąc urodzenia: maj')
        elif month_birth == '06' or month_birth == '26':
            print('Miesiąc urodzenia: czerwiec')
        elif month_birth == '07' or month_birth == '27':
            print('Miesiąc urodzenia: lipiec')
        elif month_birth == '08' or month_birth == '28':
            print('Miesiąc urodzenia: sierpień')
        elif month_birth == '09' or month_birth == '29':
            print('Miesiąc urodzenia: wrzesień')
        elif month_birth == '10' or month_birth == '30': 
            print('Miesiąc urodzenia: październik')
        elif month_birth == '11' or month_birth == '31':
            print('Miesiąc urodzenia: listopad')
        elif month_birth == '12' or month_birth == '32':
            print('Miesiąc urodzenia: grudzień')
        else:
            print('Miesiąc urodzenia: BŁĄD NUMERU PESEL - sprawdź poprawność 3 i 4 cyfry numeru.')
        
        year_1 = pesel[0]
        year_2 = pesel[1]
        year_birth = year_1 + year_2
        if int(year_birth) < 23:  # in 2023 it should be changed to 24 and so on
            print('Rok urodzenia:', '20' + year_birth)
        else:
            print('Rok urodzenia:', '19' + year_birth)
    else:
        print('Nieprawidłowy numer PESEL - nieodpowiednia liczba cyfr.') 
else:
    print('Nieprawidłowy numer PESEL - PESEL musi zawierać jedynie cyfry.')
