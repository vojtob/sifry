import sys
import korp

korpus = korp.setup_korpus(diacritics=False, language='sk')

def najdi_slova(inputl, inputw):
    for w in korpus:
        if (inputl > 0) and (len(w) != inputl):
            continue
        if (inputw != 'xx') and (not w.startswith(inputw)):
            continue
        print(w)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        najdi_slova(sys.argv[1].lower())
    else:
        print('usage: zacina.py hlada slova danej slzky zacinajuce na dane pismena')
        l = input('zadaj dlzku slova, 0 ak nechces zadat')
        w = input('zadaj zaciatocne pismena, xx ak nechces zadat')
        najdi_slova(int(l), w.lower())
    print('DONE')
