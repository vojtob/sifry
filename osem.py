from itertools import permutations
import sys
import korp

korpus = korp.setup_korpus(diacritics=False, language='cz')

# zadanie = """
# fhoihrebarsoraijx
# forebarboraciuije
# fefhoakcijaaaaiji
# sfijodfsitlorioin
# tllijivjiksdjfoia
# roodkfpcojsdvoijv
# oosvdfosijdfoijvy
# mushopuhwriuhiusb
# musebrrakcijovdsb"""

zadanie = """
ANOGITNAQŠVEJKM
AGAKOHÓUČKELLSA
DOSTOJIDIOTJEIC
YÁONASEIYMTETTH
LIUPTRMNEOTVOŘP
LCKVNÍTAEOKFÁPO
4ÍNOOSOYJCROZAI
8APHŠKNIHOROGAR
9OPALIUZDNCAMRO
1RLIEQLOTAUHIJT
ÍCÍSHAROMEOAREX"""

def ries_riadok(r, l):
    # print(r, l)
    for i in range(len(r)-l+1):
        w = r[i:i+l]
        # print('test:', w)
        if w in korpus:
            print(w)


def ries(minlength=5, maxlength=12):
    global zadanie
    zadanie = zadanie.lower()
    zadanie = zadanie.split('\n')
    zadanie.pop(0)
    # riadky
    for r in zadanie:
        for l in range(minlength, maxlength+1):
            ries_riadok(r, l)
            # od konca
            ries_riadok(r[::-1], l)
    
    # stlpce
    for s in range(len(zadanie[0])):
        r = [zadanie[i][s] for i in range(len(zadanie))]
        r = ''.join(r)
        for l in range(minlength, maxlength+1):
            ries_riadok(r, l)
            # od konca
            ries_riadok(r[::-1], l)
    
    # diagonaly
    zadanie2 = []
    zadanie3 = []
    for i, row in enumerate(zadanie):
        zadanie2.append(row[i:]+row[:i])
        zadanie3.append(row[-i:]+row[:-i])
    for s in range(len(zadanie[0])):
        r2 = [zadanie2[i][s] for i in range(len(zadanie))]
        r2 = ''.join(r2)
        r3 = [zadanie3[i][s] for i in range(len(zadanie))]
        r3 = ''.join(r3)
        for l in range(minlength, maxlength+1):
            ries_riadok(r2, l)
            ries_riadok(r3, l)
            # od konca
            ries_riadok(r2[::-1], l)
            ries_riadok(r3[::-1], l)

if __name__ == "__main__":
    zadanie = korp.word_diacritics(zadanie.lower())
    ries()
    print('DONE')
