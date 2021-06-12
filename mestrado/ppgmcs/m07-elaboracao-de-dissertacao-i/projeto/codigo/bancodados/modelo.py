from bancodados.db import _executar


class Turmas:

    def __init__(self, nome, turno, id=None):
        '''
        Base da dados tabela Turmas com os parâmetros\n
        nome: exemplo 6º4\n
        turno -> 1: matutino, 2: vespertino e 3: noturno\n
        id -> preenchido automaticamente
        '''
        self.id = id
        self.nome = nome
        self.turno = turno
        '''# ativo = 1, inativo = 0'''
        self.status = 1

        # se a tabela Turmas não existir, crie-a.
        # id: autoincrement, nome: exemplo 6º4
        # turno: 1: matutino, 2: vespertino e 3: noturno
        query = "CREATE TABLE IF NOT EXISTS turmas (id INTEGER PRIMARY KEY \
             AUTOINCREMENT, nome TEXT, turno int, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO turmas (nome, turno, status) VALUES\
             ('{self.nome}', {int(self.turno)}, {self.status})"
        _executar(query)

    def atualizar(self):
        query = f"UPDATE turmas SET status={int(self.status)} WHERE\
             id={int(self.id)}"
        _executar(query)

    def deletar(self):
        query = f"DELETE FROM turmas WHERE id={int(self.id)}"
        _executar(query)

    @staticmethod
    def get_turmas():
        query = "SELECT * FROM turmas"
        produtos = _executar(query)
        return produtos

    @staticmethod
    def get_turma(id):
        query = f"SELECT id, nome, turno FROM turmas WHERE id={int(id)}"
        turma = _executar(query)[0]
        turma = Turmas(id=turma[0], nome=turma[1], turno=turma[2])

        return turma
