from parametros.cadastrarprofessores import cadastrar_professores
from parametros.cadastrarturmas import cadastrar_turmas
from bancodados.modelo import Turma, Professor


# from parametros.param import tm, pm, dsm, hm
# from parametros.dias import dias
# from parametros.horarios import horarios
# from parametros.turmas import turmas
# from parametros.professores import professores
# from funcoes.fx1 import hca
# from grade.grade import newgrade
# from grade.visualiza import exibe_gradefx1

'''Formatação local'''
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")


if __name__ == '__main__':

    # h = horarios(hm)  # Lista numérica dos horários
    # d = dias(dsm)  # Lista numérica dos dias de aula
    # t = turmas(tm)  # Lista numérica das turmas
    # p = professores(pm)  # Lista numérica dos professores

    # gr = newgrade(h, d, t, p)

    # # Penalidade da restrição: 1a
    # hca = hca(gr, d, h, t)
    # # print(f'{gr} e {hca}')

    # exibe_gradefx1(t, d, h, gr, hca)

    # print(f'{3854.56:n}')

    ''' CADASTRAR TURMAS '''
    # add_turmas = cadastrar_turmas()

    ''' CADASTRAR PROFESSORES '''
    # add_professores = cadastrar_professores()

    view_turmas = Turma().get_turmas()
    print(" ID\t   NOME\t NÍVEL\t\t\t  TURNO\t  H.Aula\t Status")
    print("-------------------------------------------------------")
    for t in view_turmas:
        for i in range(len(t)):
            if i == 0:
                print(f'{t[0]:^5}', end="")
            elif i == 1:
                print(f'{t[1]:^8}', end="")
            elif i == 2:
                if(t[2] < 20):
                    print('Fundamental', end="")
                elif(t[2] < 30):
                    print('Médio      ', end="")
                print("\t", end="")
            elif i == 3:
                if(t[3] == 1):
                    print('Matutino  ', end="")
                elif(t[3] == 2):
                    print('Vespertino', end="")
                elif(t[3] == 3):
                    print('Noturno   ', end="")
                else:
                    print('Erro...')
            elif i == 4:
                print(f'{t[4]:^6}', end="")
                print("\t ", end="")
            elif i == 5:
                if(t[5] == 1):
                    print('Ativo', end="")
                else:
                    print('Inativo', end="")

            # print(f'{i:^5}', end="\t")
        print("\n", end="")
    print("-------------------------------------------------------")

    print("\n")
    view_professores = Professor().get_professores()
    print(" ID\t NOME DO PROFESSOR\t\t\t\
        ABREVIAÇÃO\t C.HOR/S\t Status")
    print("-------------------------------\
----------------------------------------")
    for p in view_professores:
        for i in range(len(p)):
            if i == 0:
                print(f'{p[0]:^5}', end="")
            elif i == 1:
                print(f'{p[1]:35}', end="")
            elif i == 2:
                print(f'{p[2]:10}', end="")
            elif i == 3:
                print(f'{p[3]:8}', end="\t\t  ")
            elif i == 4:
                if p[4] == 1:
                    print('Ativo', end="")
                else:
                    print('Inativo', end="")
            # print(f'{i:^5}', end="\t")
        print("\n", end="")
