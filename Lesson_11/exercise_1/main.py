''' Lesson 11, Exercise 1 - JSON reader'''

import json

def najdi_zadane_klice(jmeno_souboru: str) -> list:
    '''open JSON and search for jmeno'''
    with open(jmeno_souboru, 'r', encoding='UTF-8') as soubor:
        obsah_json = json.load(soubor)
        return [slovnik.get('jmeno') for slovnik in obsah_json]


if __name__ == '__main__':
    print(najdi_zadane_klice('Lesson_11/exercise_1/udaje.json'))
