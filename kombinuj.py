import sys
import korp
import itertools

korpus = korp.setup_korpus(diacritics=False, language='sk')

words = ['lidsajt', 'fdhseimja', 'lsinfktema', 'ipcqrsema', 'slemgboca', 'cdkanfjptem', 'ihptgqaro', 'eslnorbajkpgm', 'ldqcng', 'ipkfjtrneamo', 'sehmgacbto', 'lfonbkgpea', 'kqdstrcgo', 'cijemdsnto', 'lptfaegqn', 'fqngobmckr', 'kcpron', 'qpcobgr']

if __name__ == "__main__":
    print('START')
    for x in itertools.product(*(words[5:11])):
        w = ''.join(x)
        # print(w)
        if(w in korpus):
            print(w)

    print('DONE')