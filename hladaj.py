import sys
import korp

korpus = korp.setup_korpus(diacritics=False, language='sk')

def najdi_slova(inputw):
    for w in korpus:
        if len(w) != len(inputw):
            continue
        match = True
        for i, l in enumerate(inputw):
            if l == '.':
                continue
            if l == w[i]:
                continue
            else:
                match = False
                break
        if match:
            print(w)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        najdi_slova(sys.argv[1].lower())
    else:
        print('usage: hladaj.py <pismena, pouzi . miesto neznameho>')
        w = input('pismena slova, pouzi . miesto neznameho: ')
        najdi_slova(w.lower())
    print('DONE')
