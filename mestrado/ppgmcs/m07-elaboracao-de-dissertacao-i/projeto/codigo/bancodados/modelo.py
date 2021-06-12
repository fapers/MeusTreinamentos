from bancodados.db import _executar


class Turma:

    def __init__(self, nome="", nivel=None, turno=None, has=None, id=None):
        '''
        Base da dados tabela Turmas com os parâmetros\n
        nome: exemplo 6º4\n
        turno -> 1: matutino, 2: vespertino e 3: noturno\n
        id -> preenchido automaticamente
        has -> hora aula semanal
        '''

        self.id = id
        self.nome = nome
        self.nivel = nivel
        self.turno = turno
        self.has = has
        '''# ativo = 1, inativo = 0'''
        self.status = 1

        # se a tabela Turmas não existir, crie-a.
        # id: autoincrement, nome: exemplo 6º4
        # turno: 1: matutino, 2: vespertino e 3: noturno
        query = "CREATE TABLE IF NOT EXISTS turmas (id INTEGER PRIMARY KEY \
             AUTOINCREMENT, nome TEXT, nivel INTEGER, turno INTEGER, \
             has INTEGER, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO turmas (nome, nivel, turno, has, status) VALUES\
             ('{self.nome}', {int(self.nivel)}, {int(self.turno)},\
               {int(self.has)}, {self.status})"
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
        turmas = _executar(query)
        return turmas

    @staticmethod
    def get_turma(id):
        query = f"SELECT id, nome, nivel, turno, has FROM\
                  turmas WHERE id={int(id)}"
        turma = _executar(query)[0]
        turma = Turma(id=turma[0], nome=turma[1], nivel=[2], turno=turma[3],
                      has=[4])

        return turma


class Professor:

    # chs: Carga horária de aula semanal do professor
    def __init__(self, nome="", abreviacao="", cargahoraria=None, id=None):
        '''
        Base da dados tabela Turmas com os parâmetros\n
        nome: exemplo 6º4\n
        turno -> 1: matutino, 2: vespertino e 3: noturno\n
        id -> preenchido automaticamente
        '''
        self.id = id
        self.nome = nome
        self.abreviacao = abreviacao
        self.cargahoraria = cargahoraria
        '''# ativo = 1, inativo = 0'''
        self.status = 1

        # se a tabela Turmas não existir, crie-a.
        # id: autoincrement, nome: exemplo 6º4
        # turno: 1: matutino, 2: vespertino e 3: noturno
        query = "CREATE TABLE IF NOT EXISTS professores (id INTEGER PRIMARY KEY \
                 AUTOINCREMENT, nome TEXT, abreviacao TEXT, \
                 cargahoraria int, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO professores (nome, abreviacao, cargahoraria, status) VALUES\
             ('{self.nome}', '{self.abreviacao}', {int(self.cargahoraria)}, \
                 {int(self.status)})"
        _executar(query)

    def atualizar(self):
        query = f"UPDATE professores SET status={int(self.status)} WHERE\
             id={int(self.id)}"
        _executar(query)

    def deletar(self):
        query = f"DELETE FROM professores WHERE id={int(self.id)}"
        _executar(query)

    @staticmethod
    def get_professores():
        query = "SELECT * FROM professores"
        professores = _executar(query)
        return professores

    @staticmethod
    def get_professor(id):
        query = f"SELECT id, nome, abreviacao, cargahoraria \
                  FROM professores WHERE id={int(id)}"
        professor = _executar(query)[0]
        professor = Professor(id=professor[0], nome=professor[1],
                              abreviacao=professor[2],
                              cargahoraria=professor[3])

        return professor
