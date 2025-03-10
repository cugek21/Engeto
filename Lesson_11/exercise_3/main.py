'''Lesson 11, Exercise 3 - write and read CSV'''

import csv

DATA = [
    [10,'a1', 1],
    [12,'a2', 3],
    [14, 'a3', 5],
    [16, 'a4', 7],
    [18, 'a5', 9]
]

def zapis_csv(data: list) -> None:
    with open('Lesson_11/exercise_3/moje_csv.csv', 'w', encoding='UTF-8') as csv_soubor:
        csv_zapisovac = csv.writer(csv_soubor)
        csv_zapisovac.writerows(data)
        

def cteni_csv():
    with open('Lesson_11/exercise_3/moje_csv.csv', 'r', encoding='UTF-8') as csv_soubor:
        csv_data = csv.reader(csv_soubor, delimiter=' ')
        for row in csv_data:
            print(', '.join(row))

if __name__ == '__main__':
    zapis_csv(DATA)
    print(cteni_csv())
