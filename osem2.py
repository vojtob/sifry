from itertools import permutations
import sys
import korp

korpus = korp.setup_korpus(diacritics=True, language='sk')

riesenie = set()

zadanie = """
EŤŠEPADUBIŽÍRAPF
FERVLHOOVKRANLAE
PREAŠOCIHSBIANUN
MMARTLTKKRLRÍRIO
MAŠŠOAKOABAČÍNIN
ODŇAKNKTUJAMGOEČ
SREVHDIDJSFRKMIE
KEDAOSRALRÉSÁANS
VTETLKPOACDKTOEK
ASIAMOVNKÉPÉLOMO
PMVSNECOVRNEUMEK
EAVSNÚEŠAYĽÍKÝCS
KMKSZÚAHUADRLFKĽ
IOKSOMAĎARSKOROO
NOKRTALIANSKOIEP
GORAKÚSKOKSURNTB"""

# zadanie = """
# MENAVLSLEUÝMK
# OKXXXXEŠSNWÄN
# OXTUOKHEAUŠČA
# OMHKRĽÓUSLTOD
# ĹŽEELZSMCÉIKO
# QYHÚIJKLENOAL
# PŇVVMEAKADONA
# AAŔFÁPEUROIIE
# DFOTPODIKÓMVO
# ÁRNÁRARČEREÁQ
# MERCEDESÔFYÄC
# EPKAAKJURAJBA
# ZEMIXXXXXXÉVL"""

def test(zadanie, r, c, w):
    if zadanie[r][c]=='X':
        return

    global riesenie
    w = w+zadanie[r][c]
    # if (len(w)>3) and (w in korpus):
    #     riesenie.add(w)
    #     print(w, r, c)
    # if w in ['agon','amur','amia','cejn','fugu','hejk','hruz','ikan','lien','okun','orka','sled','uhor']:
    if w in ['audi','avia','fiat', 'jawa','golf','mini','saab','tata']:
        print(w, r, c)

    if c==12:
        return # impossible to continue
    # if c>(len(zadanie[r])-1):
    #     return

    if r>0:
        test(zadanie, (r-1) % 13, (c+1) % 13, w)
    test(zadanie, (r) % 13, (c+1) % 13, w)
    if r<12:
        test(zadanie, (r+1) % 13, (c+1) % 13, w)

if __name__ == "__main__":
    # lines = korp.word_diacritics(zadanie.lower()).split('\n')[1:]
    lines = zadanie.lower().split('\n')[1:]
    for r in range(13):
        for c in range(13):
            test(lines, r, c, '')
    print(list(riesenie))
    riesenie = list(riesenie)
    riesenie.sort(key=lambda x:len(x))
    print(riesenie)
    print('DONE')
