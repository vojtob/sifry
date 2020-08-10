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

korpus = setup_korpus(diacritics=True)

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
