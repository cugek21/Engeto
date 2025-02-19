''' Lesson 10, Exercise 1 - lines reader'''

def nacti_radky(cesta_k_souboru: str) -> str | list[str]:
    '''read lines'''
    try:
        with open(cesta_k_souboru, 'r', encoding='UTF-8') as jazyky:
            vysledek = jazyky.readlines()
    except FileNotFoundError:
        vysledek = f'Soubor: {cesta_k_souboru} neexistuje!'
    return vysledek

if __name__ == '__main__':
    print(nacti_radky('Lesson_10/exercise_1/jazyky.txt'))
