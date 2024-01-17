def farfallino_encode(s: str) -> str:
    for c in str:
        if c == 'e':
            out += 'efe'
        elif c == 'a':
            out += 'afa'
        elif c == 'i':
            out += 'ifi'
        elif c == 'o':
            out += 'ofo'
        elif c == 'u':
            out += 'ufu'
        else:
            out += c
    return out

def farfallino_encode02(s: str) -> str:
    for c in str:
        match c:
            case 'e':
                out += 'efe'
            case 'a':
                out += 'afa'
            case 'i':
                out += 'ifi'
            case 'o':
                out += 'ofo'
            case 'u':
                out += 'ufu'
            case _:
                out += c
    return out
    

def farfallino_encode03(s: str) -> str:
    # s.replace("'a', 'e', 'i', 'o', 'u'", "'afa', 'efe', 'ifi', 'ofo', 'ufu'")
    return s.replace("a","afa").replace("e", "efe").replace("i", "ifi").replace("o", "ofo").replace("u", "ufu")

def farfallino_encode04(s: str) -> str:
    for c in ['a', 'e', 'i', 'o', 'u']:
        s = s.replace(c, c+'f'+c)
        
    return s

def translate(s: str, from_lst: str, to_lst: str) -> str:
    for c in s:
        if c in from_lst:
            idx = from_lst.rfind(c)
            s = s.replace(c, to_lst[idx])
    return s


def conta_parole (s: str) -> int:
    count = 0
    for c in s:
        if c == ' ':
            count += 1
    return count

def conta_parole02 (s: str) -> int:
    return len(s.split())


#HEX STRING
def hexstring2vec(s: str) -> list[int]:
    temp = list()

    for c in range(0,len(s),2):
        st = '0'+'x'+str(s[c])+str(s[c+1]);
        temp.append(int(st,16))

    #i restanti valori a zero
    if len(s) < 16:
        for c in range(len(s), 16, 2):
            st = '0x00'
            temp.append(int(st,16))

    return temp

# ss = '35AF'
# n_ss = hexstring2vec(ss)
# print(n_ss)

#RIMUOVI SPAZI
def rimuovi_singoli_spazi(s: str) -> str:
    res = str()
    for c in range(len(s)):
        if s[c] != " " or (c>0 and s[c-1] == " ") or (c<len(s)-1 and s[c+1] == " "):
            res += s[c]
    return res

ss = 'c  i a o'
print(rimuovi_singoli_spazi(ss))
    
#È possibile ridefinire nomi di funzioni e metodi definiti dal linguaggio.
#Ad esempio vado a ridefinire la print se devo printare una serie di cose tutte con uno specifico layout
old_print = print
def print(*args): #, **kargs):  -> qui non servono i key arguments
    # old_print("|", *args, "|", sep="", **kargs)
    old_print("|", end="")
    old_print(*args, end="")
    old_print("|", end="")

# print("|", rimuovi_singoli_spazi("a b c"), "|", sep="")
print(rimuovi_singoli_spazi("a b c")) #con il nuovo print definito questa mi produce l'effetto del vecchio print impostato come nella riga precedente commentata



