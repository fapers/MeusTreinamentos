from data.db import _executar


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


class MatrizCurricular:
    '''
    Áreas do Conhecimento, Componente Curricular, Nivel, Aulas/Semana
    '''
    def __init__(self, area="", componente="", nivel=None,
                 naula=None, id=None):
        self.id = id
        self.area = area
        self.componente = componente
        self.nivel = nivel
        self.naula = naula
        self.status = 1

        query = "CREATE TABLE IF NOT EXISTS matrizcurricular (\
        id INTEGER PRIMARY KEY AUTOINCREMENT, area TEXT, componente TEXT, \
        nivel INTEGER, naula INTEGER, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO matrizcurricular (area, componente, nivel, naula, status) VALUES\
        ('{self.area}', '{self.componente}', {int(self.nivel)},\
          {int(self.naula)}, {self.status})"
        _executar(query)

    def atualizar(self):
        query = f"UPDATE matrizcurricular SET status={int(self.status)} WHERE\
             id={int(self.id)}"
        _executar(query)

    def deletar(self):
        query = f"DELETE FROM matrizcurricular WHERE id={int(self.id)}"
        _executar(query)

    @staticmethod
    def get_matrizcurricular():
        query = "SELECT * FROM matrizcurricular"
        matrizcurricular = _executar(query)
        return matrizcurricular

    @staticmethod
    def get_matrizid(id):
        query = f"SELECT id, area, componente, nivel, naula, status FROM\
                  matrizcurricular WHERE id={int(id)}"
        matriz = _executar(query)[0]
        matriz = MatrizCurricular(id=matriz[0],
                                  area=matriz[1],
                                  componente=matriz[2],
                                  nivel=matriz[3],
                                  naula=matriz[4],
                                  status=matriz[5])
        return matriz

    @staticmethod
    def get_matriznivel(nivel):
        query = f"SELECT * FROM matrizcurricular WHERE nivel={int(nivel)}"
        matriznivel = _executar(query)
        return matriznivel


class Area:

    def __init__(self, nome="", id=None):
        self.id = id
        self.nome = nome
        self.status = 1

        query = "CREATE TABLE IF NOT EXISTS areas (id INTEGER PRIMARY KEY \
             AUTOINCREMENT, nome TEXT, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO areas (nome, status) VALUES\
             ('{self.nome}', {self.status})"
        _executar(query)

    def atualizar(self):
        query = f"UPDATE areas SET status={int(self.status)} WHERE\
             id={int(self.id)}"
        _executar(query)

    def deletar(self):
        query = f"DELETE FROM areas WHERE id={int(self.id)}"
        _executar(query)

    @staticmethod
    def get_areas():
        query = "SELECT * FROM areas"
        areas = _executar(query)
        return areas

    @staticmethod
    def get_area(id):
        query = f"SELECT id, nome, status FROM areas WHERE id={int(id)}"
        area = _executar(query)[0]
        area = Area(id=area[0], nome=area[1], status=area[2])

        return area


class Componente:

    def __init__(self, nome="", id=None):
        self.id = id
        self.nome = nome
        self.status = 1

        query = "CREATE TABLE IF NOT EXISTS componentes (id INTEGER PRIMARY KEY \
             AUTOINCREMENT, nome TEXT, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO componentes (nome, status) VALUES\
             ('{self.nome}', {self.status})"
        _executar(query)

    def atualizar(self):
        query = f"UPDATE componentes SET status={int(self.status)} WHERE\
             id={int(self.id)}"
        _executar(query)

    def deletar(self):
        query = f"DELETE FROM componentes WHERE id={int(self.id)}"
        _executar(query)

    @staticmethod
    def get_areas():
        query = "SELECT * FROM componentes"
        componentes = _executar(query)
        return componentes

    @staticmethod
    def get_area(id):
        query = f"SELECT id, nome, status FROM componentes WHERE id={int(id)}"
        componente = _executar(query)[0]
        componente = Componente(id=componente[0], nome=componente[1],
                                status=componente[2])

        return componente
