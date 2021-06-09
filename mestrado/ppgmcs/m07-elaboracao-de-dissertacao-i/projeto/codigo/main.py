from parametros.param import tm, pm, dsm, hm
from parametros.dias import dias
from parametros.horarios import horarios
from parametros.turmas import turmas
from parametros.professores import professores
from funcoes.fx1 import hca
from grade.grade import newgrade
from grade.visualiza import exibe_gradefx1


'''Formatação local'''
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")


if __name__ == '__main__':

    h = horarios(hm)  # Lista numérica dos horários
    d = dias(dsm)  # Lista numérica dos dias de aula
    t = turmas(tm)  # Lista numérica das turmas
    p = professores(pm)  # Lista numérica dos professores

    gr = newgrade(h, d, t, p)

    # Penalidade da restrição: 1a
    hca = hca(gr, d, h, t)
    # print(f'{gr} e {hca}')

    exibe_gradefx1(t, d, h, gr, hca)

    print(f'{3854.56:n}')
