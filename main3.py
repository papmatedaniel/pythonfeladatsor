# Python_3.

# Az assert előtt levő # eltávolításával egyenként, szelektíven tesztelni tudod a megoldásodat.
# A feladat kezdetekor, majd minden feladat során futtatni kell a unit teszteket.
#    (pipa a baloldali menüsávon, majd a kék Run tests gomb megnyomása)
# A feladat beadásához a képernyő jobb felső részén a SUBMIT gombot kell megnyomni.


#01===================================================================================
# Feladat: Karakterek száma a fájlban.
# Írj egy függvényt karakterek_szama néven amely paraméterként egy fájlnevet kap és visszatér a fájlban levő karakterek számával. ('\n karakterekkel együtt')
def karakterek_szama(file):
    return len(open(file).read())


assert karakterek_szama("lorem.txt") == 18047


#02-------------------------------------------------------------
# Feladat: Szavak száma a fájlban.
# Írj egy függvényt szavak_szama néven amely paraméterként egy fájlnevet kap és visszatér a fájlban levő szavak számával.
def szavak_szama(file):
    return len(open(file).read().split())


assert szavak_szama("lorem.txt") == 2304


#03-------------------------------------------------------------
# Feladat: Sorok száma a fájlban.
# A sorok_szama(fname) függvény visszatér a  fájlban levő sorok számával.
def sorok_szama(file):
    return len(open(file).readlines())


assert sorok_szama("lorem.txt") == 82


#04-------------------------------------------------------------
# Feladat: r betük száma a fájlban.
# Az r_betuk_szama(fname) függvény visszatér a  fájlban levő 'r' betük számával.
def r_betuk_szama(file):
    return open(file).read().count("r")


assert r_betuk_szama("lorem.txt") == 790


#05.-------------------------------------------------------------
# Feladat: lorem szavak száma a fájlban.
# 5. A lorem_szavak_szama(fname) függvény visszatér a  fájlban levő "lorem" szavak számával.
def lorem_szavak_szama(file):
    return open(file).read().count("lorem")


assert lorem_szavak_szama("lorem.txt") == 27


#06-------------------------------------------------------------
# Feladat: A leggyakoribb karakter a fájlban.
# A leggyakoribb_karakter(fname) függvény visszatér a  fájlban leggyakrabban előforduló karakterrel.
def leggyakoribb_karakter(fname):
    karakter = list(open(fname).read())
    return max(set(karakter), key=karakter.count)
    # szotar = {i: open(fname).read().count(i) for i in open(fname).read()}
    # return max(szotar, key=szotar.get)


assert leggyakoribb_karakter("lorem.txt") == "i"


#07-------------------------------------------------------------
# Feladat: A leghosszabb sor hossza a fájlban.
# A leghosszabb_sor_hossza(fname) függvény visszatér a  fájlban levő leghosszabb sor hosszával.
def leghosszabb_sor_hossza(file):
    return max(len(i) for i in open(file).readlines())



assert leghosszabb_sor_hossza("lorem.txt") == 304


#08-------------------------------------------------------------
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
        return (self.a + self.b) * 2

    def terulet(self):
        return (self.a * self.b)


assert Teglalap(3, 4).kerulet() == 14
assert Teglalap(3, 4).terulet() == 12


#09-------------------------------------------------------------
# Feladat: Négyzet osztály definiálása. [Objektumorientált programozás]
# Hozz létre egy osztályt Negyzet néven.
# A Negyzet osztály lehetővé teszi a negyzet oldalhosszúságának tárolását.
# A Negyzet osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
# A Negyzet osztály rendelkezik egy terulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum területét.
class Negyzet:
    def __init__(self, a):
        self.a = a

    def kerulet(self):
        return self.a * 4

    def terulet(self):
        return self.a**2


assert Negyzet(3).kerulet() == 12
assert Negyzet(3).terulet() == 9


#10-------------------------------------------------------------
# Feladat: Kocka osztály definiálása. [Objektumorientált programozás]
# Hozz létre egy osztályt Kocka néven.
# A Kocka osztály lehetővé teszi a kocka oldalhosszúságának tárolását.
# A Kocka osztály rendelkezik egy tefogat() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum térfogatát.
# A Kocka osztály rendelkezik egy felszin() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum felszínét.
class Kocka:
    def __init__(self, a):
        self.a = a

    def terfogat(self):
        return self.a**3

    def felszin(self):
        return (self.a**2) * 6


assert Kocka(3).terfogat() == 27
assert Kocka(3).felszin() == 54


#11-------------------------------------------------------------
# Feladat: String fájlba írása
# Készíts függvényt string_fajlba néven, amely az első paraméterként kapott sztringet fájlba írja.
# A fájl nevét második paraméterként kapja meg a függvény.
def string_fajlba(szoveg, file):
    open(file, "w").write(szoveg)


string_fajlba("csacska macska", "szoveg.txt")
assert open("szoveg.txt").read().strip() == "csacska macska"


#12-------------------------------------------------------------
# Feladat: Számtani sorozat fájlba írása
# Készíts függvényt szaz_szam_fajlba néven, amely 1-tól 100-ig egyesével kiírja a számokat egy fájlba.
# Minden szám kerüljön új sorba.
# A fájl nevét paraméterként kapja meg a függvény.
def szaz_szam_fajlba(file):
    open(file, "w").writelines(str(i) + "\n" for i in range(1, 101))
    # valt = open(file, "w")
    # for i in range(1, 101):
    #     valt.write(str(i) + "\n")

szaz_szam_fajlba("szazas.txt")
assert len(open("szazas.txt").read())
szaz_szam_fajlba("szazas.txt")
assert sum([int(i) for i in open("szazas.txt")]) == 5050

#13--------------------------------------------------------------------------------------------


# Feladat: Első karakter a szövegfájlban
# Írj egy függvényt elso_karakter_a_fajlban néven, amely visszatér egy szövegfájl első karakterével.
# A függvény bemenő paramétere a fájl neve.
def elso_karakter_a_fajlban(file):
    return open(file).read()[0]


assert elso_karakter_a_fajlban("lorem.txt") == "L"

#14--------------------------------------------------------------------------------------------


# Feladat: Utolsó karakter a szövegfájlban
# Írj egy függvényt utolso_karakter_a_fajlban néven, amely visszatér egy szövegfájl utolsó karakterével.
# A függvény bemenő paramétere a fájl neve.
def utolso_karakter_a_fajlban(file):
    return open(file).read()[-1]


assert utolso_karakter_a_fajlban("lorem.txt") == "."

#15--------------------------------------------------------------------------------------------

# Feladat: Számok összege egy szövegfájlban.
# Írj egy függvényt szamok_osszege_a_fajlban néven amely visszatér egy szövegfájlban levő számok összegével.
# A függvény bemenő paramétere a fájl neve.


#szamok_osszege_a_fajlban
def szamok_osszege_a_fajlban(file):
    return sum(int(i) for i in open(file).read().split())



assert szamok_osszege_a_fajlban("szamok1.txt") == 16


#16--------------------------------------------------------------------------------------------
# Feladat: Számok átlaga egy szövegfájlban.
# Írj egy függvényt szamok_atlaga_a_fajlban néven, amely visszatér egy szövegfájlban levő számok átlagával.
# A függvény bemenő paramétere a fájl neve.
def szamok_atlaga_a_fajlban(file):
    return sum(lista := [int(i) for i in open(file).read().split()]) / len(lista)
    # lista = []
    # for i in open(file).read().split():
    #     lista.append(int(i))
    # return sum(lista) / len(lista)

assert szamok_atlaga_a_fajlban("szamok1.txt") == 1.0

#17--------------------------------------------------------------------------------------------


# Feladat: Páros számok száma egy szövegfájlban.
# Írj egy függvényt paros_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páros számok számával.
# A függvény bemenő paramétere a fájl neve.
def paros_szamok_szama_a_fajlban(file):
    # return len([int(i) for i in open(file).read().split() if int(i) % 2 == 0])
    return sum(1 for i in open(file).read().split() if int(i) % 2 == 0)

assert paros_szamok_szama_a_fajlban("szamok1.txt") == 10

#18--------------------------------------------------------------------------------------------


# Feladat: Páratlan számok száma egy szövegfájlban.
# Írj egy függvényt paratlan_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páratlan számok számával.
# A függvény bemenő paramétere a fájl neve.
def paratlan_szamok_szama_a_fajlban(file):
    # return len([int(i) for i in open(file).read().split() if int(i) % 2 == 1])
    return sum(1 for i in open(file).read().split() if int(i) % 2 == 1)



assert paratlan_szamok_szama_a_fajlban("szamok1.txt") == 6

#19--------------------------------------------------------------------------------------------


# Feladat: Pozitív számok száma egy szövegfájlban.
# Írj egy függvényt pozitiv_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő pozitiv számok számával.
# A függvény bemenő paramétere a fájl neve.
def pozitiv_szamok_szama_a_fajlban(file):
    # return len([int(i) for i in open(file).read().split() if int(i) > 0])
    return sum(1 for i in open(file).read().split() if int(i) > 0)


assert pozitiv_szamok_szama_a_fajlban("szamok1.txt") == 10

#20--------------------------------------------------------------------------------------------


# Feladat: Negatív számok száma egy szövegfájlban.
# Írj egy függvényt negativ_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő negativ számok számával.
# A függvény bemenő paramétere a fájl neve.
def negativ_szamok_szama_a_fajlban(file):
    # return len([int(i) for i in open(file).read().split() if int(i) < 0])
    return sum(1 for i in open(file).read().split() if int(i) < 0)


assert negativ_szamok_szama_a_fajlban("szamok1.txt") == 4

#21--------------------------------------------------------------------------------------------


# Feladat: Legkisebb szám egy szövegfájlban.
# Írj egy függvényt legkisebb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő lekisebb számmal.
# A függvény bemenő paramétere a fájl neve.
def legkisebb_szam_a_fajlban(file):
    return min(int(i) for i in open(file).read().split())


assert legkisebb_szam_a_fajlban("szamok1.txt") == -6

#22--------------------------------------------------------------------------------------------


# Feladat: Legnagyobb szám egy szövegfájlban.
# Írj egy függvényt legnagyobb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő legnagyobb számmal.
# A függvény bemenő paramétere a fájl neve.
def legnagyobb_szam_a_fajlban(file):
    return max(int(i) for i in open(file).read().split())


assert legnagyobb_szam_a_fajlban("szamok1.txt") == 4

#23--------------------------------------------------------------------------------------------


# Feladat: Párosok egy szövegfájlból.
# Írj egy függvényt parosok_a_fajlbol néven, amely visszatér a szövegfájlban levő páros számokkal mint listával.
# A függvény bemenő paramétere a fájl neve.
def parosok_a_fajlbol(file):
    return [int(i) for i in open(file).read().split() if int(i) % 2 == 0]

    

assert parosok_a_fajlbol("szamok1.txt") == [4, 2, 4, 2, 0, -4, -6, 0, 4, 4]

#24--------------------------------------------------------------------------------------------


# Feladat: Páratlanok egy szövegfájlból.
# Írj egy függvényt paratlanok_a_fajlbol néven, amely visszatér a szövegfájlban levő páratlan számokkal mint listával.
# A függvény bemenő paramétere a fájl neve.
def paratlanok_a_fajlbol(file):
    return [int(i) for i in open(file).read().split() if int(i) % 2 == 1]


assert paratlanok_a_fajlbol("szamok1.txt") == [3, 1, 3, 1, -1, -1]

#25--------------------------------------------------------------------------------------------


# Feladat: Pozitívok egy szövegfájlból.
# Írj egy függvényt pozitiv_a_fajlbol néven, amely visszatér a szövegfájlban levő pozitiv számokkal mint listával.
# A függvény bemenő paramétere a fájl neve.
def pozitivok_a_fajlbol(file):
    return [int(i) for i in open(file).read().split() if int(i) > 0]



assert pozitivok_a_fajlbol("szamok1.txt") == [4, 3, 2, 1, 4, 3, 2, 1, 4, 4]

#26--------------------------------------------------------------------------------------------


# Feladat: Negatívok egy szövegfájlból.
# Írj egy függvényt negativok_a_fajlbol néven, amely visszatér a szövegfájlban levő negativ számokkal mint listával.
# A függvény bemenő paramétere a fájl neve.
def negativok_a_fajlbol(file):
    return [int(i) for i in open(file).read().split() if int(i) < 0]


assert negativok_a_fajlbol("szamok1.txt") == [-1, -1, -4, -6]

#27--------------------------------------------------------------------------------------------


# Feladat: Leggyakoribb szám a szövegfájlban.
# Írj egy függvényt leggyakoribb_szam_a_fajlban néven, amely visszatér a szövegfájlban levő leggyakoribb számmal.
# A függvény bemenő paramétere a fájl neve.
def leggyakoribb_szam_a_fajlban(file):
    # szotar = {i: open(file).read().count(i) for i in open(file).read().split()}
    # return int(max(szotar, key=szotar.get))
    szotar = {}
    for i in open(file).read().split():
        szotar[i] = szotar.get(i, 0) + 1
    return int(max(szotar, key=szotar.get))
    

assert leggyakoribb_szam_a_fajlban("szamok1.txt") == 4

#28--------------------------------------------------------------------------------------------


# Feladat: Hárommal osztható számok a szövegfájlban.
# Írj egy függvényt harommal_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő hárommal osztható számok listájával.
# A függvény bemenő paramétere a fájl neve.
def harommal_oszthato_szamok_a_fajlban(file):
    return [int(i) for i in open(file).read().split() if int(i) % 3 == 0]


assert harommal_oszthato_szamok_a_fajlban("szamok1.txt") == [3, 3, 0, -6, 0]

#29--------------------------------------------------------------------------------------------


# Feladat: Neggyel osztható számok a szövegfájlban.
# Írj egy függvényt neggyel_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő neggyel osztható számok listájával.
# A függvény bemenő paramétere a fájl neve.
def neggyel_oszthato_szamok_a_fajlban(file):
    return [int(i) for i in open(file).read().split() if int(i) % 4 == 0]


assert neggyel_oszthato_szamok_a_fajlban("szamok1.txt") == [
    4, 4, 0, -4, 0, 4, 4
]

#======================================================================================
