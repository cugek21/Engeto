'''Lesson 10, exercise 3 - dictionary search'''

muj_slovnik = {
    'jmeno':'Pepa',
    'prijmeni': 'Novak',
    'rok_narozeni': 1990
}

def obsahuje_klic_a_hodnotu(klic: str, hodnota: str, slovnik: dict) -> bool:
    '''search for a key in dict and compare its value'''

    key = None
    try:
        key = slovnik[klic]
        print(f'Klic {klic} nalezen.')
    except KeyError:
        print(f'Klic {klic} nenalezen.')
    if key == hodnota:
        return True
    else:
        print(f'Hodnota {hodnota} nenalezena.')
        return False

if __name__ == '__main__':
    print(obsahuje_klic_a_hodnotu('jmeno', 'Pepa', muj_slovnik))
