from itertools import permutations
import sys
import korp

korpus = korp.setup_korpus(diacritics=False, language='sk')

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
