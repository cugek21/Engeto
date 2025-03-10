'''Lesson 11, Exercise 2 - Sort keys'''

import json

JMENO_SOUBORU = "Lesson_11/exercise_2/serazene.json"
DATA = {'4': 5, '6': 7, '1': 3, '2': 4}


def zapis_serazene_klice(jmeno_souboru: str, data: dict) -> None:
    '''sort keys and save to JSON'''
    with open(jmeno_souboru, 'w', encoding='UTF-8') as json_soubor:
        json.dump(data, json_soubor, sort_keys=True)

def vypis_obsah_souboru(jmeno_souboru: str):
    '''return JSON'''
    with open(jmeno_souboru, encoding='UTF-8') as json_soubor:
        return json.load(json_soubor)


if __name__ == '__main__':
    zapis_serazene_klice(JMENO_SOUBORU, DATA)
    vysledek = vypis_obsah_souboru(JMENO_SOUBORU)
    print(vysledek)
