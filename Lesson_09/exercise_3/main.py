kombinace = 1.234
presnost_str = "Hello"
presnost_cisla = 123.4567

formatovana_presnost = \
    f'|{presnost_cisla:.3}|{presnost_cisla:.4}|{presnost_cisla:.5}|'
formatovana_kombinace = f'|{kombinace:$<6.4}|'
formatovana_presnost_str = f'|{presnost_str:.4}|'

print(f'''\
Naformátovaná přesnost:\t\t{formatovana_presnost},
Naformátovaná kombinace:\t{formatovana_kombinace},
Naformátovaný string:\t\t{formatovana_presnost_str}.''')

print('Zapisuji do souboru')

with open('Lesson_09/exercise_3/vysledek.txt', 'w') as vysledek: #path
    vysledek.write('\n'.join((formatovana_presnost, formatovana_kombinace, formatovana_presnost_str)))