# UPDATE: 13.08.2022

import sys

def check_correctness(pesel:str)->None:
    if not pesel.isnumeric():
        print('Nieprawidłowy numer PESEL - PESEL musi zawierać jedynie cyfry.')
        sys.exit(1)
    
    if len(pesel) != 11:
        print('Nieprawidłowy numer PESEL - nieodpowiednia liczba cyfr.') 
        sys.exit(2)


def check_sex(pesel:str, raport:dict)->dict:
    sex = int(pesel[9])
    if sex % 2 == 0:
        raport['Płeć'] = 'kobieta'
    else:
        raport['Płeć'] = 'mężczyzna'
    
    return raport


def day_of_birth(pesel:str, raport:dict)->dict:
    
    day_birth = int(pesel[4:6])
    if day_birth < 32:
        raport['Dzień urodzenia'] = day_birth
    else:
        print('Dzień urodzenia: BŁĄD NUMERU PESEL - sprawdź poprawność 5 i 6 cyfry numeru.')
        sys.exit(3)
    
    return raport


def month_of_birth(pesel:str, raport:dict)->dict:
    month_birth = pesel[2:4]
        
    if month_birth == '01' or month_birth == '21':
        month = 'styczeń'
    elif month_birth == '02' or month_birth == '22':
        month = 'luty'
    elif month_birth == '03' or month_birth == '23':
        month =  'marzec'
    elif month_birth == '04' or month_birth == '24':
        month =  'kwiecień'
    elif month_birth == '05' or month_birth == '25':
        month =  'maj'
    elif month_birth == '06' or month_birth == '26':
        month =  'czerwiec'
    elif month_birth == '07' or month_birth == '27':
        month =  'lipiec'
    elif month_birth == '08' or month_birth == '28':
        month =  'sierpień'
    elif month_birth == '09' or month_birth == '29':
        month =  'wrzesień'
    elif month_birth == '10' or month_birth == '30': 
        month =  'październik'
    elif month_birth == '11' or month_birth == '31':
        month =  'listopad'
    elif month_birth == '12' or month_birth == '32':
        month =  'grudzień'
    else:
        month =  'BŁĄD NUMERU PESEL - sprawdź poprawność 3 i 4 cyfry numeru.'
        sys.exit(4)
    
    raport['Miesiąc urodzenia'] = month

    return raport


def year_of_birth(pesel:str, raport:dict)->dict:
    year_birth = pesel[:2]
    if int(year_birth) < 23:  # in 2023 it should be changed to 24 and so on
        year = '20' + year_birth
    else:
        year = '19' + year_birth
        
    raport['Rok urodzenia'] = year
    
    return raport


def main():
    try:
        pesel = sys.argv[1]
    except IndexError:
        pesel = input('Podaj numer PESEL: ')
    
    check_correctness(pesel)

    raport = {}
    check_sex(pesel, raport)
    day_of_birth(pesel, raport)
    month_of_birth(pesel, raport)
    year_of_birth(pesel, raport)

    for key, value in raport.items():
        print(key, '-', value)
    

if __name__ == '__main__':
    main()
