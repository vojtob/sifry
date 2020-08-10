from itertools import permutations
import sys

special_chars = ['á', 'ó', 'ý', 'č', 'ľ', 'ú', 'ť', 'ä', 'ž', 'š', 'í', 'é', 'ô', 'ň', 'ŕ', 'ď', 'ĺ', 'ö', 'ě', 'è', 'ü', 'ř', 'ê', 'à', 'å']
replacement_chars = ['a', 'o', 'y', 'c', 'l', 'u', 't', 'a', 'z', 's', 'i', 'e', 'o', 'n', 'r', 'd', 'l', 'o', 'e', 'e', 'u', 'r', 'e', 'a', 'a']
def word_diacritics(w):
    w1 = ''
    for l in w:
        if not l.isascii():
            w1 = w1 + replacement_chars[special_chars.index(l)]
        else:
            w1 = w1 + l
    return w1

# setup db
def setup_korpus(diacritics):
    words = {'ahoj'}
    korpusname = 'db_slov/'
    if diacritics:
        korpusname = korpusname + 'kratky_korpus.txt'
    else:
        korpusname = korpusname + 'kratky_korpus_bez_diakritiky.txt'
    with open(korpusname, "r", encoding='UTF-8') as searchfile:
        for line in searchfile:
            words.add(line.strip())
    return words

korpus = setup_korpus(diacritics=False)

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
"""
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
    ries()
    print('DONE')
