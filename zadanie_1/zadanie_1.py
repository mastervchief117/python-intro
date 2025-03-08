#3.3
#A
#Funkcja enumerate; Dokumentacja: https://docs.python.org/3/library/functions.html#enumerate , https://bigglo.pl/python/enumerate/
#Funkcja enumerate() służu do iteracji przez listę (lub inny obiekt iterowalny) i zwraca obiekt typu enumerate, który jest iterowalny, 
#po przekształceniu do listy otrzymujemy listę krotek, które składają się z par (indeks, wartość).
#Indeks reprezentuje pozycję elementu w oryginalnym obiekcie, a wartość to sam element.
#Przykład:
#my_list = ["a", "b", "c"]
#for i, value in enumerate(my_list):
#    print(f"Indeks: {i}, Wartość: {value}")
#Wynik: Indeks: 0, Wartość: a, Indeks: 1, Wartość: b, Indeks: 2, Wartość: c

#B
#Moduł math; Dokumentacja: https://docs.python.org/3/library/math.html#module-math , https://py4e.pl/html3/04-functions.php
#Moduł math zawiera funkcje do obliczeń matematycznych (podobnie jak kalkulator) oraz niektóre stałe matemayczne. Trzeba go zaimportować za pomocą import math. 
#Instrukcja ta tworzy obiekt modułu, z którego później korzystamy.
#Przykład:
#import math
#wynik = math.sqrt(16)
#print(wynik)
#Wynik: 4.0

#C
#Wyjątek ValueError; Dokumentacja: https://docs.python.org/3/library/exceptions.html#Exception
#Obsługa błędu, podczas gdy operacja lub funkcja otrzymuje argument o właściwym typie, ale niewłaściwej wartości.
#Przykład: int('abc') - nie powiedzie się, ponieważ 'abc' nie jest liczbą. W takim przypadku Python wyrzuci ValueError.


#3.4
import random #generowanie liczb losowych

#A - 2 listy i łączenie za pomocą funkcji zip()
name = ["Patrycja", "Aleksander", "Jagoda", "Mariusz"]
age = ["24", "25", "8", "31"]

#Łączenie list za pomocą funkcji zip; zip() łączy listy/iterables w krotki;  Dokumentacja: https://www.freecodecamp.org/news/python-zip-function-explained-with-examples/
combined = list(zip(name,age))
print(f"Połączone listy: {combined}")

#B - Jedna funkcja z modułu random
#random.choice() zwraca losowy element z listy; Dokumentacja: https://docs.python.org/3/library/random.html
random_person = random.choice(combined)
print(f"Losowa osoba: {random_person}")

#C - Obsługa wyjątku try-except; służy do obsługi wyjątków(błędów); Dokumentacja: https://docs.python.org/3/tutorial/errors.html
try:
    number = int(input("Podaj liczbę: "))
    result = 100 / number
    print(f"Wynik dzielenia: {result}")
except ValueError: #Obsługa błędu gdy wpisany tekst nie jest liczbą
    print("Błąd: Podana wartość nie jest liczbą.")
except ZeroDivisionError: #Obsługa błędu podczas dzielenia przez 0
    print("Błąd: Nie można dzielić przez zero.")

print("Program zakończony.")