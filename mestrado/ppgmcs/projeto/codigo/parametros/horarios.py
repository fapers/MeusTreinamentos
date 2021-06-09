import numpy as np


def horarios(n):
    h = np.arange(n)
    return h


if __name__ == '__main__':
    h = horarios(5)
    print(h)
    print(type(h))
