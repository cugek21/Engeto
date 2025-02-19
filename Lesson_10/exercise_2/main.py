'''Lesson 10, exercise 2 - add dirty list'''

def secti_hodnoty(udaje: list) -> float:
    '''add only float from data'''

    for udaj in udaje:
        clean_data = 0.0
        try:
            clean_data += float(udaj)
        except Exception:
            print(f'{udaj} is not number.')
    return clean_data

if __name__ == '__main__':
    test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, [], '\\n', 4]
    print(f'Vysledek: {secti_hodnoty(test)}')
