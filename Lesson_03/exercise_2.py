#Vstupni data
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}

#overeni
if uzivatel.get(jmeno) == heslo:
    print('Ahoj', jmeno, 'vítej v aplikaci! Pokračuj...')
else:
    print('Uživatelské jméno nebo heslo nejsou v pořádku!')