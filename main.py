 
# Feladat: Két szám összege.
# Írj egy függvényt "osszead" néven, amely két számot kap és visszatér a két szám összegével.

def osszead(a,b):
    return a + b




#  02
# Feladat: Melyik a kisebb?
# Írj egy függvényt "kisebb" néven, amely két számot kap és visszatér a legkisebbel.
def kisebb(a,b):
    if a > b:
        return b
    if a < b:
        return a




#  03
# Feladat: Melyik a nagyobb?
# Írj egy függvényt "nagyobb" néven, amely két számot kap és visszatér a legnagyobbal.
def nagyobb(a,b):
    if a > b:
        return a
    if a < b:
        return b


 

#  04
# Feladat: Számtani közép
# Írj "szamtani_kozep" néven függvényt, amely két számot kap bemenetként és visszatér a számtani középpel.
def szamtani_kozep(a,b):
    return (a + b)/2





#  05

# Feladat: Négyzet kerülete
# Írj "negyzet_kerulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet kerületével.
def negyzet_kerulet(a):
    return a * 4



#  06

# Feladat: Négyzet területe
# Írj "negyzet_terulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet területével.
def negyzet_terulet(a):
    return a*a




#  07

# Feladat: Téglalap kerülete
# Írj "teglalap_kerulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap kerületével.
def teglalap_kerulet(a,b):
    return (a+b)*2




#  08

# Feladat: Téglalap területe
# Írj "teglalap_terulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap területével.
def teglalap_terulet(a,b):
    return a*b




#  09

# Feladat: Két szám különbsége
# Írj "kulonbseg" néven függvényt, amely két számot kap bemenetként és visszatér a két szám különbségével.
def kulonbseg(a,b):
    return a - b




#  10
# Feladat: Maradékos osztás:  
# Írj egy "maradek" nevü függvényt, amely két számot kap bemenetként és visszatér a két szám osztásának maradékával.
def maradek(a,b):
    return a % b




#  11
# Feladat: Páros szám:  
# Írj egy "paros" nevü függvényt, amely egy számot kap bemenetként, majd True-val tér vissza, ha a szám páros és False-al ha a szám páratlan.
def paros(a):
    if a % 2 == 0:
        return True
    else:
        return False




#  12-
# Feladat: Kettővel osztható:  
# Írj egy "kettovel_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám kettővel osztható és False-al ha nem.
def kettovel_oszthato(a):
    if a % 2 == 0:
        return True
    else:
        return False




#  13
# Feladat: Hárommal osztható:
# Írj egy "harommal_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám hárommal osztható és False-al ha nem.
def harommal_oszthato(a):
    if a % 3 == 0:
        return True
    else:
        return False




#  14
# Feladat: Héttel osztható:  
# Írj egy "hettel_oszthato" nevü függvényt , amely egy számot kap bemenetként és True-val tér vissza, ha a szám héttel osztható és False-al ha nem.
def hettel_oszthato(a):
    if a % 7 == 0:
        return True
    else:
        return False




#  15
# Feladat: Kocka térfogat:  
# Írj egy "kocka_terfogat" nevü függvényt , amely bemenetként megkapja a kocka oldal hosszúságát és a kocka térfogatával tér vissza.
def kocka_terfogat(a):
    return a * a * a




#  16
# Feladat: Téglatest térfogat:  
# Írj egy "teglatest_terfogat" nevü függvényt , amely bemenetként megkapja a téglatest oldalainak hosszúságát és a téglatest térfogatával tér vissza.
def teglatest_terfogat(a,b,c):
    return a*b*c
    



#  17------------------------------------------------------------------------------------------------------------
# Feladat: Derékszögü háromszög területe:  
# Írj egy "derekszogu_haromszog_terulet" nevü függvényt , amely bemenetként megkapja a befogók hosszát és a háromszög területével tér vissza.
def derekszogu_haromszog_terulet(a,b):
    return (a*b) /2




#  18
# Feladat: Derékszögü háromszög átfogója: 
# Írj egy "derekszogu_haromszog_atfogo" nevü függvényt , amely bemenetként megkapja a befogók hosszát és az átló hosszával tér vissza.
def derekszogu_haromszog_atfogo(a,b):
    return (a**2+b**2)**0.5
    




#  19
# Feladat: Négyzet átlója:  
# Írj egy "negyzet_atloja" nevü függvényt , amely bemenetként megkapja a négyzet oldalának hosszát és az átló hosszával tér vissza.
def negyzet_atloja(a):
    return (2**0.5)*a




#  20
# Feladat: Téglalap átlója: 
# Írj egy "teglalap_atloja" nevü függvényt , amely bemenetként megkapja az oldalak hosszát és az átló hosszával tér vissza.
def teglalap_atloja(a,b):
    return (a ** 2 + b ** 2) ** 0.5





#  21
# Feladat: Abszolútérték: 
# Írj egy "abszolut" nevü függvényt , amely a bemenő paraméterként kapott szám abszolút értékével tér vissza.
def abszolut(a):
    if a > 0 :
        return a
    else:
        return -a
        



#  01

#  Feladat: Első karakter 
#  Írj egy függvényt elso_karakter néven amely visszatér az adott string első karakterével! 
def elso_karakter(lista):
    return lista[0]



#  02 

#  Feladat: Utolsó karakter 
#  Írj egy függvényt utolso_karakter néven  amely visszatér az adott string utolso karakterével! 
def utolso_karakter(lista):
    return lista[-1]


#  03 

#  Feladat: Legkisebb szám a listában. [Programozási tétel: Minimum kiválasztás] 
#  Készíts függvényt legkisebb néven,  amely visszatér egy számokat tartalmazó lista legkisebb számával. 
#  Figyelem! A feladat megoldása során nem használhatod a min függvényt! 
def legkisebb(lista):
    legk = lista[0]
    for i in lista:
        if i < legk:
            legk = i
    return legk

#  04 

#  Feladat: Legnagyobb szám a listában. [Programozási tétel: Maximum kiválasztás] 
#  Készíts függvényt legnagyobb néven,  amely visszatér egy számokat tartalmazó lista legnagyobb számával. 
#  Figyelem! A feladat megoldása során nem használhatod a max függvényt! 
def legnagyobb(lista):
    legn = lista[0]
    for i in lista:
        if i > legn:
            legn = i
    return legn

#  05 

#  Feladat: Listaban levő számok összege. [Programozási tétel: Összegzés] 
#  Készíts függvényt osszeg néven,  amely visszatér egy számokat tartalmazó lista számainak összegével. 
#  Figyelem! A feladat megoldása során nem használhatod a sum függvényt! 
def osszeg(lista):
    ossz = 0
    for i in lista:
        ossz = ossz + i
    return ossz

#  06 
       
#  Feladat: Listában levő számok szorzata. 
#  Készíts függvényt szorzat néven,  amely visszatér egy számokat tartalmazó lista számainak szorzatával. 
def szorzat(lista):
    szor = 1
    for i in lista:
        szor = szor * i
    return szor
    
#  07 
    
#  Feladat: Páros számok száma a listában. [Programozási tétel: Megszámolás] 
#  Készíts függvényt parosok_szama néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával. 
def parosok_szama(lista):
    par = 0
    for i in lista:
        if i % 2 == 0:
            par += 1
    return par

#  08 

#  Feladat: Páratlan számok száma a listában. [Programozási tétel: Megszámolás] 
#  Készíts függvényt paratlanok_szama néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával. 
def paratlanok_szama(lista):
    par = 0
    for i in lista:
        if i % 2 == 1:
            par += 1
    return par

#  09 

#  Feladat: Pozitív számok száma a listában. [Programozási tétel: Megszámolás] 
#  Készíts függvényt pozitivok_szama néven,  amely visszatér egy számokat tartalmazó lista pozitív számainak számával. 
def pozitivok_szama(lista):
    poz = 0
    for i in lista:
        if i > 0:
            poz += 1
    return poz


#  10 

#  Feladat: Negatív számok száma a listában. [Programozási tétel: Megszámolás] 
#  Készíts függvényt negativok_szama néven,  amely visszatér egy számokat tartalmazó lista negativ számainak számával.
def negativok_szama(lista):
    poz = 0
    for i in lista:
        if i < 0:
            poz += 1
    return poz


#  11 
#  Feladat: Benne van a szám a listában? [Programozási tétel: Eldöntés] 
#  Készíts függvényt benne_van_a_listaban néven,  amelynek első paramétere egy számokat tartalmazó lista, a második paramétere egy szám. 
#  A visszatérési érték True, ha  a szám benne van a listában. 
#  A visszatérési érték False, ha  a szám nics benne a listában. 
def  benne_van_a_listaban(lista, nemtudom):
    return  nemtudom in lista
    


#  12 
#  Feladat: Benne van a betü a stringben? [Programozási tétel: Eldöntés] 
#  Készíts függvényt benne_van_a_stringben néven,  amelynek első paramétere egy string, a második paramétere egy betü. 
#  A visszatérési érték True, ha  a betü benne van a stringben. 
#  A visszatérési érték False, ha  a betü nics benne a stringben.
def benne_van_a_stringben(lista, szoveg):
    return szoveg in lista
    


#  13 

#  Feladat: Hányadik a listában? [Programozási tétel: Kiválasztás] 
#           A listában a szám garantáltan megtalálható, nem kell vizsgálni a meglétét. 
#  Készíts függvényt hanyadik_a_listaban néven,  amelynek első paramétere egy számokat tartalmazó lista, a második paramétere egy szám. 
#  A visszatérési érték a paraméterként megadott szám első előfordulási helye a listában.
def hanyadik_a_listában(lista, szam):
    return lista.index(szam)




#  14 
#  Feladat: Hányadik a stringben? [Programozási tétel: Kiválasztás] 
#           A betü garantáltan megtalálható a stringben, nem kell vizsgálnunk a meglétét. 
#  Készíts függvényt hanyadik_a_stringben néven, amelynek első paramétere egy string, a második paramétere egy betü. 
#  A visszatérési érték a paraméterként megadott betü első előfordulási helye a stringben.
def hanyadik_a_stringben(lista, betu):
    return lista.index(betu)


#  15 
#  Feladat: Benne van-e a listában és hanyadik helyen? [Programozási tétel: Keresés] 
#  Készíts függvényt kereses_a_listaban néven,  amelynek első paramétere egy számokat tartalmazó lista, a második paramétere egy szám. 
#  Ha a szám benne van a listában, akkor a visszatérési érték a paraméterként megadott szám első előfordulási helye a listában. 
#  A visszatérési érték None, ha  a szám nics benne a listában. 
def  kereses_a_listaban(lista, szam):
    if szam in lista:
        return lista.index(int(szam)) 
    


#  16 
#  Feladat: Hányadik a stringben? [Programozási tétel: Keresés] 
#  Készíts függvényt kereses_a_stringben néven, amelynek első paramétere egy string, a második paramétere egy betü. 
#  A visszatérési érték a paraméterként megadott betü első előfordulási helye a stringben. 
#  A visszatérési érték None, ha  a betü nics benne a stringben. 
def kereses_a_stringben(sztring, betu):
    if betu in sztring:
        return sztring.index(betu)
    
    


#  17 
    
#  Feladat: Páros számok kiválogatása egy listából. [Programozási tétel: Kiválogatás] 
#  Készíts függvényt parosok_kivalogatasa néven,  amely visszatér egy listával amely a paraméterként átadott számokat tartalmazó lista páros számait tartalmazza. 
def parosok_kivalogatasa(lista):
    par = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
    return par

#  18 

#  Feladat: Páratlan számok számok kiválogatása egy listából. [Programozási tétel: Kiválogatás] 
#  Készíts függvényt paratlanok_kivalogatasa néven,  amely visszatér egy listával amely a paraméterként átadott számokat tartalmazó lista páratlan számait tartalmazza. 
def paratlanok_kivalogatasa(lista):
    par = []
    for i in lista:
        if i % 2 == 1:
            par.append(i)
    return par

#  19 
    
#  Feladat: Pozitív számok kiválogatása egy listából. [Programozási tétel: Kiválogatás] 
#  Készíts függvényt pozitivok_kivalogatasa néven,  amely visszatér egy listával amely a paraméterként átadott számokat tartalmazó lista pozitiv számait tartalmazza. 
def pozitivok_kivalogatasa(lista):
    poz = []
    for i in lista:
        if i > 0:
           poz.append(i)
    return poz

#  20 

#  Feladat: Negatív számok számok kiválogatása egy listából. [Programozási tétel: Kiválogatás] 
#  Készíts függvényt negatívok_kivalogatasa néven,  amely visszatér egy listával amely a paraméterként átadott számokat tartalmazó lista negatív számait tartalmazza. 
def negativok_kivalogatasa(lista):
    poz = []
    for i in lista:
        if i < 0:
           poz.append(i)
    return poz


#  21 

#  Feladat: Két halmaz metszete. [Programozási tétel: Metszet] 
#  Készíts függvényt halmazok_metszete néven, amely két paraméterként átadott halmaz azonos elemeivel mint halmazzal tér vissza. 
def halmazok_metszete(elso, ketto):
    return elso & ketto

#  22 

#  Feladat: Két lista metszete. [Programozási tétel: Metszet] 
#  Készíts függvényt listak_metszete néven, amely két paraméterként átadott lista azonos elemeivel mint listával tér vissza. 
def listak_metszete(elso, ketto):
    return list(set(elso) & set(ketto))

#  23 

#  Feladat: Két halmaz uniója. [Programozási tétel: Unió] 
#  Készíts függvényt halmazok_unioja néven, amely két paraméterként átadott halmaz minden elemeivel mint halmazzal tér vissza. 
def halmazok_unioja(elso, ketto):
    return elso | ketto



#  24 

#  Feladat: Listaban levő számok átlaga (számtani közepe). 
#  Készíts függvényt lista_atlag néven,  amely visszatér egy számokat tartalmazó lista számainak átlagával.
def lista_atlag(lista):
    atlag = sum(lista)
    szamlalo = len(lista)
    return atlag / szamlalo




#  25 

#  Feladat: Faktoriális. 
#  Készíts függvényt faktorialis néven,  amely visszatér a paraméterként megkapott szám faktoriálisával.
def faktorialis(szam):
    fakto = 1
    for i in range(1,szam + 1):
        fakto *= i
    return fakto



# Python_3.
# Az assert előtt levő eltávolításával egyenként, szelektíven tesztelni tudod a megoldásodat.
# A feladat kezdetekor, majd minden feladat során futtatni kell a unit teszteket.
#    (pipa a baloldali menüsávon, majd a kék Run tests gomb megnyomása)
# A feladat beadásához a képernyő jobb felső részén a SUBMIT gombot kell megnyomni.
# 01
# Feladat: Karakterek száma a fájlban.
# Írj egy függvényt karakterek_szama néven amely paraméterként egy fájlnevet kap és visszatér a fájlban levő karakterek számával. ('\n karakterekkel együtt')


def karakterek_szama(fajlnev):
    with open(fajlnev, "r") as f:
        return len(f.read())


# 02    
# Feladat: Szavak száma a fájlban.
# Írj egy függvényt szavak_szama néven amely paraméterként egy fájlnevet kap és visszatér a fájlban levő szavak számával.


def szavak_szama(fajlnev):
    with open(fajlnev, 'r') as fajl:
        return len(fajl.read().split())


# 03  
# Feladat: Sorok száma a fájlban. 
# A sorok_szama(fname) függvény visszatér a  fájlban levő sorok számával.   


def sorok_szama(fajlnev):
    with open(fajlnev, "r") as f:
        return f.read().count("\n") + 1


# 04
# Feladat: r betük száma a fájlban. 
# Az r_betuk_szama(fname) függvény visszatér a  fájlban levő 'r' betük számával.


def r_betuk_szama(fajlnev):
    with open(fajlnev, 'r') as f:
        return f.read().count("r")


# 05        
# Feladat: lorem szavak száma a fájlban. 
# 5. A lorem_szavak_szama(fname) függvény visszatér a  fájlban levő "lorem" szavak számával.


def lorem_szavak_szama(fajlnev):
    with open(fajlnev, 'r') as f:
        return f.read().count("lorem")


# 06    
# Feladat: A leggyakoribb karakter a fájlban. 
# A leggyakoribb_karakter(fname) függvény visszatér a  fájlban leggyakrabban előforduló karakterrel.


def leggyakoribb_karakter(fajl):
    with open(fajl, "r") as f:
        szotar = {}
        for i in f.read():
            szotar[i] = szotar.get(i, 0) + 1
        return max(szotar, key=szotar.get)




# 07 
# Feladat: A leghosszabb sor hossza a fájlban. 
# A leghosszabb_sor_hossza(fname) függvény visszatér a  fájlban levő leghosszabb sor hosszával.
def leghosszabb_sor_hossza(fajlnev):
    with open(fajlnev, "r") as f:
        lista = []
        for i in f.readlines():
            lista.append(len(i))
        return max(lista)
        print(lista)



# 08
# Feladat: Téglalap osztály definiálása. [Objektumorientált programozás]
# Hozz létre egy osztályt Teglalap néven.
# A Teglalap osztály lehetővé teszi a téglalap oldalhosszúságainak tárolását.
# A Teglalap osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
# A Teglalap osztály rendelkezik egy terulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum területét.


class Teglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kerulet(self):
        return 2 * (self.a + self.b)

    def terulet(self):
        return self.a * self.b



# 09
# Feladat: Négyzet osztály definiálása. [Objektumorientált programozás]
# Hozz létre egy osztályt Negyzet néven.
# A Negyzet osztály lehetővé teszi a negyzet oldalhosszúságának tárolását.
# A Negyzet osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
# A Negyzet osztály rendelkezik egy terulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum területét.


class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def kerulet(self):
        return 4 * self.oldalhossz

    def terulet(self):
        return self.oldalhossz * self.oldalhossz



# 10
# Feladat: Kocka osztály definiálása. [Objektumorientált programozás]
# Hozz létre egy osztályt Kocka néven.
# A Kocka osztály lehetővé teszi a kocka oldalhosszúságának tárolását.
# A Kocka osztály rendelkezik egy terfogat() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum térfogatát.
# A Kocka osztály rendelkezik egy felszin() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum felszínét.


class Kocka:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz

    def terfogat(self):
        return self.oldalhossz**3

    def felszin(self):
        return (self.oldalhossz**2) * 6



# 11
# Feladat: String fájlba írása
# Készíts függvényt string_fajlba néven, amely az első paraméterként kapott sztringet fájlba írja.
# A fájl nevét második paraméterként kapja meg a függvény.


def string_fajlba(string, fajlnev):
    with open(fajlnev, "w") as f:
        f.write(string)




# Feladat: Számtani sorozat fájlba írása
# Készíts függvényt szaz_szam_fajlba néven, amely 1-tól 100-ig egyesével kiírja a számokat egy fájlba.
# Minden szám kerüljön új sorba.
# A fájl nevét paraméterként kapja meg a függvény.


def szaz_szam_fajlba(fajlnev):
    with open(fajlnev, "w") as f:
        for i in range(1, 101):
            f.write(str(i) + "\n")



# 13
# Feladat: Első karakter a szövegfájlban
# Írj egy függvényt elso_karakter_a_fajlban néven, amely visszatér egy szövegfájl első karakterével.
# A függvény bemenő paramétere a fájl neve.


def elso_karakter_a_fajlban(fajlnev):
    with open(fajlnev, "r") as f:
        for i in f.read():
            return i


# 14--------------------------------------------------------------------------------------------
# Feladat: Utolsó karakter a szövegfájlban
# Írj egy függvényt utolso_karakter_a_fajlban néven, amely visszatér egy szövegfájl utolsó karakterével.
# A függvény bemenő paramétere a fájl neve.


def utolso_karakter_a_fajlban(fajlnev):
    with open(fajlnev, "r") as f:
        return list(f.read())[-1]


# 15
# Feladat: Számok összege egy szövegfájlban.
# Írj egy függvényt szamok_osszege_a_fajlban néven amely visszatér egy szövegfájlban levő számok összegével.
# A függvény bemenő paramétere a fájl neve.
def szamok_osszege_a_fajlban(lista):
    ossz = 0
    with open(lista, "r") as lista:
        for i in lista:
            ossz += 1
    return ossz

# 16
# Feladat: Számok átlaga egy szövegfájlban.
# Írj egy függvényt szamok_atlaga_a_fajlban néven, amely visszatér egy szövegfájlban levő számok átlagával.
# A függvény bemenő paramétere a fájl neve.
def szamok_atlaga_a_fajlban(lista):
    list = []
    with open(lista, "r") as lista:
      for i in lista.read().split():
          list.append(int(i))
    return sum(list) / len(list)
assert szamok_atlaga_a_fajlban("szamok1.txt") == 1.0

# 17
# Feladat: Páros számok száma egy szövegfájlban.
# Írj egy függvényt paros_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páros számok számával.
# A függvény bemenő paramétere a fájl neve.


def paros_szamok_szama_a_fajlban(lista):
    par = []
    with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) % 2 == 0:
                par.append(i)
        return len(par)
    

assert paros_szamok_szama_a_fajlban("szamok1.txt") == 10

# 18
# Feladat: Páratlan számok száma egy szövegfájlban.
# Írj egy függvényt paratlan_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páratlan számok számával.
# A függvény bemenő paramétere a fájl neve.


def paratlan_szamok_szama_a_fajlban(lista):
    par = []
    with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) % 2 == 1:
                par.append(i)
        return len(par)


assert paratlan_szamok_szama_a_fajlban("szamok1.txt") == 6

# 19
# Feladat: Pozitív számok száma egy szövegfájlban.
# Írj egy függvényt pozitiv_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő pozitiv számok számával.
# A függvény bemenő paramétere a fájl neve.


def pozitiv_szamok_szama_a_fajlban(lista):
    poz = []
    with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) > 0:
                poz.append(i)
        return len(poz)



# 20
# Feladat: Negatív számok száma egy szövegfájlban.
# Írj egy függvényt negativ_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő negativ számok számával.
# A függvény bemenő paramétere a fájl neve.


def negativ_szamok_szama_a_fajlban(lista):
    with open(lista, "r") as lista:
        poz = []
        for i in lista.read().split():
            if int(i) < 0:
                poz.append(i)
        return len(poz)



# 21
# Feladat: Legkisebb szám egy szövegfájlban.
# Írj egy függvényt legkisebb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő lekisebb számmal.
# A függvény bemenő paramétere a fájl neve.
def legkisebb_szam_a_fajlban(lista):
    with open(lista, "r") as lista:
        legk = []
        for i in lista.read().split():
            legk.append(int(i))
        return min(legk)


# 22
# Feladat: Legnagyobb szám egy szövegfájlban.
# Írj egy függvényt legnagyobb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő legnagyobb számmal.
# A függvény bemenő paramétere a fájl neve.
def legnagyobb_szam_a_fajlban(lista):
    with open(lista, "r") as lista:
        legn = []
        for i in lista.read().split():
            legn.append(int(i))
        return max(legn)

# 23
# Feladat: Párosok egy szövegfájlból.
# Írj egy függvényt parosok_a_fajlbol néven, amely visszatér a szövegfájlban levő páros számokkal mint listával.
# A függvény bemenő paramétere a fájl neve.
def parosok_a_fajlbol(lista):
    par = []
    with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) % 2 == 0:
                par.append(int(i))
        return par

# 24
# Feladat: Páratlanok egy szövegfájlból.
# Írj egy függvényt paratlanok_a_fajlbol néven, amely visszatér a szövegfájlban levő páratlan számokkal mint listával.
# A függvény bemenő paramétere a fájl neve.
def paratlanok_a_fajlbol(lista):
     par = []
     with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) % 2 == 1:
                par.append(int(i))
        return par
         

# 25
# Feladat: Pozitívok egy szövegfájlból.
# Írj egy függvényt pozitiv_a_fajlbol néven, amely visszatér a szövegfájlban levő pozitiv számokkal mint listával.
# A függvény bemenő paramétere a fájl neve.
def pozitivok_a_fajlbol(lista):
    poz = []
    with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) > 0:
                poz.append(int(i))
        return poz

# 26
# Feladat: Negatívok egy szövegfájlból.
# Írj egy függvényt negativok_a_fajlbol néven, amely visszatér a szövegfájlban levő negativ számokkal mint listával.
# A függvény bemenő paramétere a fájl neve.
def negativok_a_fajlbol(lista):
    poz = []
    with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) < 0:
                poz.append(int(i))
        return poz


# 27
# Feladat: Leggyakoribb szám a szövegfájlban.
# Írj egy függvényt leggyakoribb_szam_a_fajlban néven, amely visszatér a szövegfájlban levő leggyakoribb számmal.
# A függvény bemenő paramétere a fájl neve.
def leggyakoribb_szam_a_fajlban(lista):
    with open(lista, "r") as lista:
        szotar = {}
        for i in lista.read().split():
            szotar[i] = szotar.get(i, 0) + 1
        return int(max(szotar, key=szotar.get))

# 28
# Feladat: Hárommal osztható számok a szövegfájlban.
# Írj egy függvényt harommal_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő hárommal osztható számok listájával.
# A függvény bemenő paramétere a fájl neve.
def harommal_oszthato_szamok_a_fajlban(lista):
    par = []
    with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) % 3 == 0:
                par.append(int(i))
        return par
# 29
# Feladat: Neggyel osztható számok a szövegfájlban.
# Írj egy függvényt neggyel_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő neggyel osztható számok listájával.
# A függvény bemenő paramétere a fájl neve.
def neggyel_oszthato_szamok_a_fajlban(lista):
    par = []
    with open(lista, "r") as lista:
        for i in lista.read().split():
            if int(i) % 4 == 0:
                par.append(int(i))
        return par
