class Film:
    def __init__(self):
        self._tytul = ''
        self._lista_wypozyczen = 0

    def set_tytul(self, tytul):
        if len(tytul) <= 20:
            self._tytul = tytul
        else:
            print("Tytuł nie może mieć więcej niż 20 znaków")

    def get_tytul(self):
        return self._tytul

    def get_lista_wypozyczen(self):
        return self._lista_wypozyczen

    def increment_lista_wypozyczen(self):
        self._lista_wypozyczen += 1

film = Film()
print("początkowy tytuł:", film.get_tytul())
print("początkowa liczba wypożyczeń:", film.get_lista_wypozyczen())

film.set_tytul("Fight Club")
print("tytul po zmianie:", film.get_tytul())

tytul = film.get_tytul()
print("tytuł filmu", tytul)

liczba_wypozyczen_przed = film.get_lista_wypozyczen()
print("przed inkrementacja", liczba_wypozyczen_przed)

film.increment_lista_wypozyczen()

liczba_wypozyczen_po = film.get_lista_wypozyczen()
print("po inkrementacji", liczba_wypozyczen_po)