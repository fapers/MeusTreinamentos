import numpy as np


def turmas(n):
    t = np.arange(n)
    return t


def turnos(n):
    t = np.arange(n)
    return t


if __name__ == '__main__':
    t = turmas(22)  # 14 matutino, 6 vespertino e 2 noturno
    print(t)
    print(type(t))

    t1 = turnos(3)  # Matutino, Vespertino e Noturno
    print(f'Turnos: {t1}')
