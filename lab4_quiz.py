# Zadanie 1:
# Napisz funkcję `max_min_difference`, która przyjmuje dowolną liczbę argumentów (liczby) 
# i zwraca różnicę między największą a najmniejszą wartością. Jeśli funkcja otrzyma mniej niż dwa argumenty, 
# powinna zwrócić 0. Pamiętaj o odpowiednim zastosowaniu składni *args.
#
# Przykładowe użycie:
# max_min_difference(1, 3, 5, 9) zwraca 8 (bo 9 - 1 = 8)

# Twoja odpowiedź:

def max_min_difference(*args):
    # tutaj wpisz swoje rozwiązanie
    pass

# Zadanie 2:
# Napisz funkcję `next_prime`, która będzie generatorem zwracającym
# kolejne liczby pierwsze, zaczynając od podanej liczby startowej.
# Jeśli podana liczba startowa jest liczbą pierwszą, generator powinien też ją zwrócić.
#
# Przykładowe użycie:
# prime_gen = next_prime(10)
# next(prime_gen) zwraca 11

def is_prime(num):
    # tutaj wpisz swoje rozwiązanie
    pass

def next_prime(start):
    # tutaj wpisz swoje rozwiązanie
    pass


# Zadanie 3:
# Napisz funkcję `filter_kwargs` która przyjmuje funkcję `func` oraz dowolną liczbę argumentów 
# nazwanych (keyword arguments) i stosuje `func` tylko do tych argumentów, które mają klucz 
# zaczynający się na literę 'a'. Funkcja `filter_kwargs` powinna zwracać słownik zawierający oryginalne 
# klucze i przetworzone wartości.
#
# Przykładowe użycie:
# def double(x):
#     return x * 2
#
# print(filter_kwargs(double, apple=2, banana=4, avocado=6))
# Powinno zwrócić: {'apple': 4, 'avocado': 12}
#
# Uwaga: Zakładamy, że `func` jest funkcją przyjmującą jeden argument pozycyjny.

# Twoja odpowiedź:

def filter_kwargs(func, **kwargs):
    # tutaj wpisz swoje rozwiązanie
    pass
