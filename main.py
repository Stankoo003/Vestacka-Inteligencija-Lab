def parni(lista):
    return {
        'Parni': list(filter(lambda x: x%2 == 0, lista)),
        'Neparni': list(filter(lambda x: x% 2== 1, lista)) 
    }

#print(parni([1,7,2,4,5]))


def numlista(lista):
    tipovi = set(type(element).__name__ for element in lista) # okej..
    # tipovi mora da budu jedinstveni
    return {
        tip: list(filter(lambda x: type(x).__name__ == tip,lista))
        for tip in tipovi
    }
#print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))

def uredi(lista,n,vrednost):
    return [
        x+vrednost if i<n else x-vrednost
        for i, x in enumerate(lista)            
    ]
#print(uredi([1, 2, 3, 4, 5], 3, 1))

"""
    Kreira novu listu gde je svaki element zbir dva susedna elementa
    iz prosleđene liste.
"""

from itertools import pairwise
def zbir(lista):
    return [a+b for a,b in pairwise(lista)]

#print(zbir([1,2,3,4,5]))

def brojel(*args):
    return [len(x) if type(x) == list else -1 for x in args]
#print(brojel([1,2],[3,4,5],'el',['1',1]))

def razlika(lista1,lista2):
    return list(set(lista1) - set(lista2))
print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))

def operacija(lista):
    return [sum(t) for t in lista]
print(operacija([(1, 4, 6), (2, 4), (4, 1)]))

from itertools import accumulate

def izmeni(lista):
    return list(accumulate(lista))
print(izmeni([1,2,4,7,9]))

def prosek(lista):
    return [sum(podlista) / len(podlista) for podlista in lista]
print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))


def izbroj(lista):
    if type(lista) !=list:
        return 1
    return sum(izbroj(elem) for elem in lista)

print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))

from itertools import pairwise
def razlika(lista):
    return [x-y for x, y in pairwise(lista)]
print(razlika([8,5,3,1,1]))

def presek(lista1,lista2):
    return list(set(lista1) & set(lista2))
print(presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]))


def izmeni(lista):
    return{
        'pp': [x+1 for x in lista[::2]],
        'np': [x-1 for x in lista[1::2]]
    }
print(izmeni([8, 6, 3, 1, 1]))

def unija(lista1,lista2):
    return list(set(lista1 + lista2))
print(unija([5, 4, "1", "8", 7], [1, 9, "1"]))

def izdvoji(lista):
    return [podlista[i] if i < len(podlista) else 0 for i, podlista in enumerate(lista)]
print(izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))
# enumerate prolazi kroz listu i za svaki element vraca TUPLE sa indeks vrednost.


from collections import Counter

def brojanje(recnik):
    tipovi = [type(vrednost).__name__ for vrednost in recnik.values()]
    brojac = Counter(tipovi) # Counter automatski pravi tuple on vrati tip i broj ponavljanja.
    return list(brojac.items())

print(brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8}))


def kreiraj(N):
    return[(i, sum(range(i+1)) ** 2) for i in range(N+1)]
print(kreiraj(4))

from itertools import pairwise

def kreiraj(lista):
    return [[x for x in p1 if x not in p2] for p1,p2 in pairwise(lista)]
print(kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]))

from functools import reduce
from operator import pow
def stepenuj(lista):
    return [reduce(pow,t) for t in lista]
print(stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]))

def boje(hex_boja):
    return {
        "Red": int(hex_boja[1:3],16),
        "Green": int(hex_boja[3:5],16),
        "Blue": int(hex_boja[5:7],16)
    }
print(boje("#FA1AA0"))



# 18

def kreirajj(lista):
    return [[x for x in p1 if not x in p2] for p1,p2 in pairwise(lista) ]
print(kreirajj([[1,2,3],[2,4,5],[4,5,6,7],[1,5]]))

# 12
def presekk(lista1,lista2):
    return [set(lista1) & set(lista2)]
print(presekk([5,4,"1","8",3,7],[1,9,"1",5] ))

#15
#def izvojii(lista):
#   return [podlista[i] if i<len(podlista) else 0 for i,podlista in enumerate(lista)]
#print(izvojii([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))

def izvojii(lista):
    return [podlista[i] if i<len(podlista) else 0 for i,podlista in enumerate(lista)]
print(izvojii([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))

#17
def kreirajj(N):
    return [(i, sum(range(i+1))** 2) for i in range(N+1)]
print(kreirajj(5))

#14
def unijaa(lista1,lista2):
    return [set(lista1 + lista2)]
print(unijaa([5, 4, "1", "8", 7], [1, 9, "1"]) )

#19
#from functools import reduce
#from operator import pow
def stepenujj(lista):
    return [reduce(pow,t) for t in lista]
print(stepenujj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]))

#1
def parnii(lista):
    return{
        "Parni": list(filter(lambda x: x%2==0, lista)),
        "Neparni": list(filter(lambda x: x%2==1,lista))
    }
print(parnii([1,7,2,4,5]))
#20
def bojee(hex_boja):
    return {
        "Red": int(hex_boja[1:3],16),
        "Green": int(hex_boja[3:5],16),
        "Blue": int(hex_boja[5:7],16)
    }
print(bojee("#FA1AA0"))

#15
print(izvojii([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))

#7
def savberii(lista):
    return [ sum(t) for t in lista]
print(savberii([(1, 4, 6), (2, 4), (4, 1)]))
#2
def numlistaa(lista):
    tipovi: set(type(element).__name__ for element in lista)
    return {
        tip: list(filter(lambda x: type(x).__name__ == tip,lista))
        for tip in tipovi
    }
print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))


#10
def izbrojj(lista):
    if type(lista)!=list:
        return 1
    return sum(izbrojj(elem) for elem in lista)
print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))
#11
from itertools import pairwise
def razlikaa(lista):
    return [x-y for x,y in pairwise(lista)]
print(razlika([8,5,3,1,1]))

#9
def prosekk(lista):
    return [sum(podlista)/len(podlista) for podlista in lista]
print(prosekk([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))

#10
def izbrojjj(lista):
    if type(listaa) != list:
        return 1
    return sum(izbroj(elem) for elem in lista)

#16
def brojanjeeee(rencik):
    tipovi = [type(vrednost).__name__ for vrednost in rencik.values()]
    brojac = Counter(tipovi)
    return list(brojac.items())
print(brojanjeeee({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8}))

#5
def brojelll(*args):
    return [len(x) if type(x) == list else -1 for x in args]
print(brojel([1, 2], [3, 4, 5], 'el', ['1', 1]))

#9
def prosekkk(lista):
    return [sum(podlista) / len(podlista)for podlista in lista]
print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))

#6 razlika

def razlikaaaaa(lista1,lista2):
    return [set(lista1)- set(lista2)]

