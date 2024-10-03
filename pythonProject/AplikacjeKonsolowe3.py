class Notatka:
    __licznik_notatek = 0

    def __init__(self, tytul, tresc):
        Notatka.__licznik_notatek += 1
        self.__identyfikator = Notatka.__licznik_notatek
        self._tytul = tytul
        self._tresc = tresc

    def wyswietl_notatke(self):
        print(f"Tytul: {self._tytul}\nTreść: {self._tresc}")

    def diagnostyka(self):
        print(f"ID: {self.__identyfikator}; Tytul: {self._tytul}; Tresc: {self._tresc}")

if __name__ == "__main__":
    notatka1 = Notatka("Zakupy", "Kupić piwko")
    notatka2 = Notatka("Spotkanie", "Spotkać się na rzeczone piwko")

    print("Notatka 1:")
    notatka1.wyswietl_notatke()
    print("Diagnostyka:")
    notatka1.diagnostyka()

    print("Notatka 2:")
    notatka2.wyswietl_notatke()
    print("Diagnostyka:")
    notatka2.diagnostyka()