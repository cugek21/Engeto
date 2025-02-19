def zobraz_slova(textovy_soubor):
    with open(textovy_soubor, 'r') as file:
        data = file.read()
        vsechna_slova = data.split()

    for slovo in vsechna_slova:
        if len(slovo) >= 7:
            print(slovo)

if __name__ == "__main__":
    zobraz_slova('Lesson_09/exercise_1/slova.txt') #check the path