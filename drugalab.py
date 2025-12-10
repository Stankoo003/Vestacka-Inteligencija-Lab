from itertools import zip_longest

#1
def poredak(a,b):
    return [
        (x,y,'Jeste' if y == 2 * x else 'Nije ')
        for x,y in zip_longest(a,b,fillvalue=0)
    ]
#print(poredak([1, 7, 2, 4], [2, 5, 2]))


# zip_longest se koristi
#2
def spojidict(a, b):
    return [
        {'prvi': x, 'drugi': y}
        for x,y in zip_longest(a,b, fillvalue='-')
    ]
#print(spojidict([1, 7, 2, 4], [2, 5, 2]))
#3
def spoji(a,b):
    return [
        (min(x, y), max(x,y,), x+y)
        for x,y in zip_longest(a,b, fillvalue=0)
    ]
#print(spoji([1, 7, 2, 4], [2, 5, 2]))
#4
from functools import reduce
def suma(lst):
    return reduce(
        lambda acc, x: acc + (suma(x) if isinstance(x,list) else x),
        lst, 0 
    )
#print(suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

#5
def proizvod(A, B):
    return [reduce(lambda x, y: x + y, [b * x for x in a]) 
            for a, b in zip(A, B)]
#print(proizvod([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]))

# objasnjenje funkcije, ovde zip(A,B) pravi parove [1,2,3] sa [1], [4,5,6] sa [2] itd.
# unutrasnji deo lambda funkcije kaze spji element sa b * x koj je element iz a, i dodaj x na y koj je ukupan zbir do sada.

#6
def objedini(a, b):
    spojeno = zip_longest(a, b, fillvalue=0)
    return [tuple(sorted(par)) for par in spojeno]
#print(objedini([1, 7, 2, 4, 5], [2, 5, 2]))

#7
def objedini(podaci):
    return {t[0]: (list(t[1:]) if len(t) > 1 else None) for t in podaci}
# mnogo dobro radi, znaci uzme prvi element neironicno i onda napravi listu od svih elemenata pocesvi od prvog do zadnjeg
#print(objedini([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)]))

#8
def izracunaj(lst):
    return [
       reduce(lambda x, y: x * y, elem) if isinstance(elem,list) else elem
       for elem in lst 
    ]
print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))

#9
def zamena(lst,x):
    return [
        (sum(lst[i+1:]) if elem < x else elem)
        for i,elem in enumerate(lst)
    ]
print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))

#10
from itertools import pairwise
def stepen(lst):
    return [x**y for x, y in pairwise(lst)]
print(stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]))

#11
from functools import reduce
def proizvod(lst):
    return reduce(
        lambda acc, sub: acc * reduce(lambda a, b: a * b, sub, 1),
        lst,
        1
    )

print(proizvod([[1, 3, 5], [2, 4, 6], [1, 2, 3]]))  # 4320

#12
def izracunaj(lst):
    return [
        # prvi deo racuna zbir kvadrata svakog elementa u listi, a ako nije samo rokne kvadrat
        (sum(x*x for x in elem) if isinstance(elem,list)else elem*elem)
        for elem in lst
    ]
print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))

#13
from itertools import pairwise, zip_longest
def skupi(lst):
    return [
        [a+b for a,b in zip_longest(p,q,fillvalue=0)]
        for p, q in pairwise(lst) # pq su zapravo ovde parovi listi, e sad onda te parove listi spajamo i onda sabiramo
    ]
print(skupi([[1, 3, 5], [2, 4, 6], [1, 2]]))

#14
def suma(lst):
    # proizvod elemenata jedne podliste
    proizvod_podliste = lambda sub: reduce(lambda a, b: a * b, sub, 1)
    # sub je 1 2 3, a 1 b = 2 -> 2 a = 2 b = 3 -> 6
    # zbir proizvoda svih podlista
    #spoljni reduce 
    return reduce(lambda acc, sub: acc + proizvod_podliste(sub), lst, 0)
    # da se podsetimo reduce funkcija ima argumente: funkcija, kolekcija i pocetna vrednost.

print(suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 630

#15 

def promeni(lst,x):
    return [
        (elem - x) if elem >= x else (elem+x)
        for elem in lst
    ]
print(promeni([7, 1, 3, 5, 6, 2], 3))

#16
def broj(heksa):
    r_hex = heksa[1:3]
    g_hex = heksa[3:5]
    b_hex = heksa[5:7]
    r = int(r_hex,16)
    g = int(g_hex, 16)
    b = int(b_hex, 16)
    # ovde se pretvaraju hex vrednosti u int.
    return r * 65536 + g * 256 + b

print(broj("#FA0EA0"))

#17

def tekst(s):
    def zameni(ch):
        code = ord(ch) # daje sa tacna kodna tacka tipa za omega je 937 
        # velika slova, mala slova, cifre
        if 65 <= code <= 90 or 97 <= code <= 122 or 48 <= code <= 57: # proveri se to ako je karakter samo vrati karakter
            return ch
        # ostalo pretvaramo u \uXXXX
        heks = hex(code)[2:].upper()      # npr. 32 -> '20'
        return "\\u" + heks.zfill(4)      # '20' -> '0020' -> '\u0020' popuni da bude do 4.

    return "".join(zameni(ch) for ch in s)

# primer
print(tekst("Otpornost 10Ω."))
# 'Otpornost\\u002010\\u03A9\\u002E'

#18
import re
def brojevi(s):
    return [int(x) for x in re.findall(r'\d+',s)]

print(brojevi("42+10=52;10*10=100"))

from itertools import groupby

def brojanje(s):
    return sum(1 for _, g in groupby(s) if len(list(g))>1)
print(brojanje("aatesttovi"))

## group by prolazi i grupise uzastupne karaktere, 
#svaki groupby prolazi i dobija se kao kljuc i vrednost koliko se puta taj karakter ponavlja, 
#medjutim to nama nije bitno zato stavljamo donju crtu. 
# i onda sta se desava vrati 1 ako se desilo to poklapanje, i tako sabere sva ta poklapanja


#20
def izracunaj(niz, f):
    return [f(niz[i], niz[i+1], niz[i+2]) for i in range(len(niz) - 2)]

rez = izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z)
print(rez)  # [7, 11, 43]
