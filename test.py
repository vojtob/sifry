import sys
import korp

korpus = korp.setup_korpus(diacritics=False, language='sk')
korpuscz = korp.setup_korpus(diacritics=False, language='cz')

abeceda = 'abcdefghijklmnoprstuvxyz'

if __name__ == "__main__":
    for w in korpus:
        # if w.endswith('niky'):
        #     print(w)
        # if w.startswith('yh'):
        #     print(w)
        # if 'meter' in w:
        #     print(w)
        if (len(w) == 8):
            if w[0] not in 'abcdefgh':
                continue
            if w[0] != w[6]:
                continue
            if w[3] != w[5]:
                continue
            x = {w[0], w[1], w[2], w[3], w[4]}
            if len(x) != 5:
                continue
            # if w[0] not in 'abcdefgh':
            #     continue
            # if 'znac' in w:
            print(w)
    
    print('DONE')