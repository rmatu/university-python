import hashlib, binascii
import shelve
import numpy as np

def hash_password(password):
    """Hash a password for storing."""
    # Ponieważ nie możemy dodać osobnego pliku do jupyter notebooka z którego zczytywalibyśmy
    # ziarno, dodajemy je od razu tutaj
    salt = b'bd63843e66ddd780bfe991f9583c9202f71036698aee15762df7d9ef999aebca25ba67716dc53cc78355c66e5'
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


mockUsers = [
    {'login': "Ryszard", 'password': 'bd63843e66ddd780bfe991f9583c9202f71036698aee15762df7d9ef999aebca25ba67716dc53cc78355c66e5513db32cb66aa13c3122a9acba84c3d11c8954d41dc7ba2641d02582ac5aeb0d3faafa54b5daadb669faf1560fdfe305399cadbeba0b71c8598981fce4c691c3'},
    {'login': "Damian", 'password': 'bd63843e66ddd780bfe991f9583c9202f71036698aee15762df7d9ef999aebca25ba67716dc53cc78355c66e59aee6e65f33487327fbebf82d81e0159e1ffa7ffd5ad88c66d1c93668b1ac10f689e9496e694d5a17ce403226666132a6a7a65444b3a49b9d294bc23005e09d3'},
    {'login': "Przemek", 'password': 'bd63843e66ddd780bfe991f9583c9202f71036698aee15762df7d9ef999aebca25ba67716dc53cc78355c66e5eae31aefc17ea9b06c06564a7a64c2f30bb9432dfdb93e7322fa6020987c2782a5374e6a32c93a889b2ba4c1d25edeedf3ac2bc05e4997d8a96c3e0158bfc24e'},
    {'login': "Monika", 'password': 'bd63843e66ddd780bfe991f9583c9202f71036698aee15762df7d9ef999aebca25ba67716dc53cc78355c66e51d4971600ecb21c4dd05b30e3348bf38e3809cc44400cc8ff90be2dce672ccc16a41bd994fcd20bf1d9a401823c15af6c4e6acff0c75b0871b40c478e4d280e9'}

]

def saveUsers(users):
    with shelve.open('user.db') as shelf:
        for id, user in enumerate(users):
            shelf[str(id)] = user


saveUsers(mockUsers)


def zadanie1(func):
    def wrapper(login, password):
        with shelve.open('user.db') as shelf:
            for item in shelf.items():
                if item[1]['login'] == login:
                    if hash_password(password) == item[1]['password']:
                        func(login, password)
                    else:
                        print('Błąd')

    return wrapper


@zadanie1
def log_in(login, password):
    print(f'Użytkownik {login} zalogowany pomyślnie')


log_in('Przemek', 'herbata')


def zadanie2(func):
    def wrapper(value, min_v, max_v):
        if min_v <= value <= max_v:
            func(value, min_v, max_v)
        else:
            print('error')
    return wrapper


@zadanie2
def check(value, min_v, max_v):
    print(f'{value} mieści się w przedziale [{min_v}, {max_v}]')


check(10, 1, 11)


def fun_gen(p, min_v, max_v):
    for i in range(len(p)):
        if min_v <= p[i] <= max_v:
            yield i


def zadanie3(poly, min_v, max_v):
    r = np.roots(poly)
    p = r[np.isreal(r)]
    for i in fun_gen(p, min_v, max_v):
        print(round(p[i], 5), 'odp')


zadanie3([1, 6, 5, -12], -10, 0)  #x^3 + 6x^2 + 5x - 12

