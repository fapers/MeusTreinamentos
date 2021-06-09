import numpy as np


def professores(n):
    p = np.arange(n)
    return p


if __name__ == '__main__':
    p = professores(35)
    print(p)
    print(type(p))
