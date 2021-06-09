import numpy as np


def hca(grade, d, h, t):
    '''
    Cálculo dos conflitos da restrição
    Hard Constraint: Sobreposição de horários de aula
    hca(solução, número de dias, número de horários e números de turmas)
    hca: Restrição Hard a) Sobreposição de horários de aula
    i: percorre os dias da semana
    j: percorre os horários do dia
    t: percorre as turmas
    '''

    nota = np.arange(len(d)*len(h)).reshape(len(d), len(h))
    for i in range(len(d)):
        for j in range(len(h)):
            auxiliar = 0
            for k in range(len(t) - 1):
                for w in range(k+1, len(t)):
                    if(grade[i][j][k] == grade[i][j][w]):
                        auxiliar += 1
            nota[i][j] = auxiliar
    return nota
