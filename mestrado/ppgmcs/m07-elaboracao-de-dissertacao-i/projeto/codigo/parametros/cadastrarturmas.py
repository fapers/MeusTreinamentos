from bancodados.modelo import Turma


# Cadastrar todas as turma da escola
# Nome, Nível, Turno, Número de aulas por semana
# Nível 16 é o 6º ano do ensino fundamental
# Nível 17 é o 7º ano do ensino fundamental
# Nível 18 é o 8º ano do ensino fundamental
# Nível 19 é o 97º ano do ensino fundamental
# Nível 21 é o 1º ano do ensino médio
# Nível 22 é o 2º ano do ensino médio
# Nível 23 é o 3º ano do ensino médio

def cadastrar_turmas():
    turma = Turma('6º4', 16, 1, 25)
    turma.salvar()

    turma = Turma('7º4', 17, 1, 25)
    turma.salvar()

    turma = Turma('8º4', 18, 1, 25)
    turma.salvar()

    turma = Turma('9º4', 19, 1, 25)
    turma.salvar()

    turma = Turma('1º6', 21, 1, 25)
    turma.salvar()

    turma = Turma('1º7', 21, 1, 25)
    turma.salvar()

    turma = Turma('1º8', 21, 1, 25)
    turma.salvar()

    turma = Turma('1º10', 21, 1, 25)
    turma.salvar()

    turma = Turma('2º6', 22, 1, 25)
    turma.salvar()

    turma = Turma('2º7', 22, 1, 25)
    turma.salvar()

    turma = Turma('2º8', 22, 1, 25)
    turma.salvar()

    turma = Turma('3º5', 23, 1, 25)
    turma.salvar()

    turma = Turma('3º6', 23, 1, 25)
    turma.salvar()

    turma = Turma('3º7', 23, 1, 25)
    turma.salvar()

    turma = Turma('6º3', 16, 2, 25)
    turma.salvar()

    turma = Turma('7º3', 17, 2, 25)
    turma.salvar()

    turma = Turma('8º3', 18, 2, 25)
    turma.salvar()

    turma = Turma('9º3', 19, 2, 25)
    turma.salvar()

    turma = Turma('1º9', 21, 2, 25)
    turma.salvar()

    turma = Turma('2º5', 22, 2, 25)
    turma.salvar()

    turma = Turma('1ºEJA', 21, 3, 20)
    turma.salvar()

    turma = Turma('3ºEJA', 23, 3, 20)
    turma.salvar()

    return turma.get_turmas()
