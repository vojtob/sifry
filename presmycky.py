from itertools import permutations
import sys

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

def presmycky(word):
    perm = list(permutations(word))
    for p in perm:
        w = ''
        for s in p:
            w = w+s
        if w in korpus:
            print(w)

if __name__ == "__main__":
    # presmycky('rieka')
    if len(sys.argv) == 2:
        presmycky(sys.argv[1].lower())
    else:
        print('usage: hladaj.py <pismena_presmycky>')
        w = input('pismena presmycky: ')
        presmycky(w.lower())
    print('DONE')
