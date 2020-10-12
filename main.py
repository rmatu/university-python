import time
from datetime import datetime, timedelta
from random import Random
rand = Random()

# Zadanie 1
# Prześledź szybkość dodawania elementów do tablicy.

def exercise1():
    tab = []
    t1 = time.time()
    for i in range(100000):
        tab.append(i)
    t2 = time.time()
    print(t2 - t1)


exercise1()


# Zadanie 2
# Stwórz kalkulator do obliczenia aktualnej godziny w konkretnej strefie czasowej.
# Do zadania wystarczy utworzyć słownik z przesunięciami czasowymi z i od UTC.

def exercise2():
    d = ""
    for i in range(-12, 14):
        d = {"UTC" + str(i): i}

    choice = input('Wprowadź liczbę z zakresu [-12, 14], aby obliczyć strefę czasową: ')
    key = "UTC" + choice

    user_time = 0
    if key in d:
        user_time = d[key]

    actual_time = datetime.now()
    new_time = actual_time + timedelta(hours=user_time)
    print(new_time)


exercise2()


# Zadanie 3
# Zmodyfikuj kod związany z losowaniem liczb z przedziału od 1 do 10, tak aby obliczał przybliżoną wartość oczekiwaną
# obliczoną jako średnią (z prób). Uśrednienie ma nastąpić 1m razy (milion razy).

def exercise3():
    tab = []
    try_count = 1
    while True:
        t1 = time.time()
        if rand.randint(0, 10) >= 10:  # random [0,10]
            t2 = time.time()
            tab.append(t2-t1)
            break
        else:
            try_count += 1
            continue

    sum1 = 0
    for i in range(len(tab)):
        sum1 += tab[i]
    avg = sum1 / len(tab)

    print(f"Found in {try_count} tries")
    print (f"Avg time: {avg}")


exercise3()


# Zadanie 4
# Napisz algorytm obliczający kolejne liczby pierwsze dla zadanych wartości.

def exercise4():
    prime_numbers = {1}
    user_down = int(input("Podaj zakres dolny: "))
    user_up = int(input("Podaj zakres górny: "))

    for i in range(user_down, user_up + 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
            else:
                prime_numbers.add(i)

    print(prime_numbers)


exercise4()
# Zadanie 5
# Napisz program wyznaczający ciąg Fibonacciego dla 93 elementu (lub 93 iteracji) w najszybszym możliwym czasie.

def exercise5(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        sub = exercise5(n - 1)
        return sub + [sub[-1] + sub[-2]]


# Najszybszy program (znaleziony w internecie)
# link - https://stackoverflow.com/questions/42552897/fibonacci-sequence-calculator-python

def internet_fib(n):
    a = b = 1
    yield a
    yield b
    while n > 2:
        n -= 1
        a, b = b, a + b
        yield b


# Zadanie 6
# Napisz program, który wyznacza odległość Levenshteina dla dwóch zadanych łańcuchów znaków.


def exercise6(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([exercise6(s[:-1], t) + 1,
               exercise6(s, t[:-1]) + 1,
               exercise6(s[:-1], t[:-1]) + cost])

    return res


print(exercise6('test', 'AtestAB'))
