special_chars = ['á', 'ó', 'ý', 'č', 'ľ', 'ú', 'ť', 'ä', 'ž', 'š', 'í', 'é', 'ô', 'ň', 'ŕ', 'ď', 'ĺ', 'ö', 'ě', 'è', 'ü', 'ř', 'ê', 'à', 'å', 'ů']
replacement_chars = ['a', 'o', 'y', 'c', 'l', 'u', 't', 'a', 'z', 's', 'i', 'e', 'o', 'n', 'r', 'd', 'l', 'o', 'e', 'e', 'u', 'r', 'e', 'a', 'a', 'u']
def word_diacritics(w):
    w1 = ''
    for l in w:
        if not l.isascii():
            w1 = w1 + replacement_chars[special_chars.index(l)]
        else:
            w1 = w1 + l
    return w1

# setup db
def setup_korpus(diacritics, language):
    words = {'ahoj'}
    korpusname = 'db_slov/'
    if language=='cz':
        if diacritics:
            korpusname = korpusname + 'cz_korpus.txt'
        else:
            korpusname = korpusname + 'cz_korpus_bez_diakritiky.txt'
    else: # sk
        if diacritics:
            korpusname = korpusname + 'kratky_korpus.txt'
        else:
            korpusname = korpusname + 'kratky_korpus_bez_diakritiky.txt'

    with open(korpusname, "r", encoding='UTF-8') as searchfile:
        for line in searchfile:
            words.add(line.strip())
    return words