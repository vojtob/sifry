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

def convertfiles():
    # prev = ''
    # with open("db_slov/slovensky_narodny_korpus_ma-2015-02-05.txt", "r", encoding='UTF-8') as searchfile:
    #     with open("db_slov/kratky_korpus.txt", "w", encoding='UTF-8') as kratkyfile:
    #         with open("db_slov/dlhy_korpus.txt", "w", encoding='UTF-8') as dlhyfile:
    #             with open("db_slov/kratky_korpus_bez_diakritiky.txt", "w", encoding='UTF-8') as kratkybezfile:
    #                 for line in searchfile:
    #                     s = line.split('\t')
    #                     w = s[0].strip().lower()
    #                     if w != prev:
    #                         kratkyfile.write(w+'\n')
    #                         kratkybezfile.write(word_diacritics(w+'\n'))
    #                         prev = w
    #                     dlhyfile.write(s[1].strip().lower()+'\n')
    prev = ''
    with open("db_slov/cz_korpus.txt", "r") as searchfile:
        with open("db_slov/cz_korpus_bez_diakritiky.txt", "w", encoding='UTF-8') as kratkybezfile:
            for line in searchfile:
                w = line.strip().lower()
                if w != prev:
                    kratkybezfile.write(word_diacritics(w+'\n'))
                    prev = w

convertfiles()

print('DONE')