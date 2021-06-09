import numpy as np


def newgrade(h, d, t, p):
    grade = np.arange(len(h)*len(d)*len(t)).reshape(len(d), len(h), len(t))
    for i in range(len(d)):
        for j in range(len(h)):
            for k in range(len(t)):
                aleatorio = np.random.choice(p)
                grade[i][j][k] = int(aleatorio)
    return grade
