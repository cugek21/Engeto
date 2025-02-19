prvni_radek = "První řádek v souboru,\n"
druhy_radek = "druhý řádek v souboru,\n"
treti_radek = "třetí řádek v souboru."

with open('Lesson_09/exercise_2/txt_soubor.txt', 'w') as txt_soubor: #path
    txt_soubor.write(prvni_radek)
    txt_soubor.write(druhy_radek)
    txt_soubor.write(treti_radek)

with open('Lesson_09/exercise_2/txt_soubor.txt', 'r') as obsah_txt: #path
    print(obsah_txt.read())