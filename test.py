import sys
import korp

korpus = korp.setup_korpus(diacritics=True, language='sk')

abeceda = 'abcdefghijklmnoprstuvxyz'

if __name__ == "__main__":
    for w in korpus:
        if len(w) != 11:
            continue
        if w[1] != w[5]:
            continue
        if w[0] != 's':
            continue
        
        print(w)
    
    
    print('DONE')