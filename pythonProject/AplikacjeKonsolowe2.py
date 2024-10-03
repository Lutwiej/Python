class Osoba:
    liczba_instancji = 0

    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczba_instancji += 1

    @classmethod
    def kopiuj(cls, inna_osoba):
        return cls(inna_osoba.__id, inna_osoba.__imie)

    def przedstaw_sie(self, inne_imie):
        if self.__imie:
            print(f"Czesc {inne_imie}, mam na imię {self.__imie}")
        else:
            print("Brak danych")

if __name__ == "__main__":
    osoba1 = Osoba()
    osoba2 = Osoba(1, "Olek")
    osoba3 = Osoba.kopiuj(osoba2)
    print("Osoba 1:")
    osoba1.przedstaw_sie("Aleksander")
    print("Osoba 2:")
    osoba2.przedstaw_sie("Alek")
    print("Osoba 3:")
    osoba3.przedstaw_sie("Olo")

    print(f"Liczba utworzonych instancji klasy Osoba: {Osoba.liczba_instancji}")