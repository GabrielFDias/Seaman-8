from rh.classes.Departamento import Departamento
from datetime import date, timedelta


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento 01', 'Gabriel', 1, 1, 1990)

        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento 01', 'Gabriel', 1, 1, 1990)

        assert objeto.nome == 'Departamento 01'
        assert objeto.responsavel is 'Gabriel'

    def test_str_repr(self):
        objeto = Departamento('Departamento 01', 'Gabriel', 1, 1, 1990)

        assert str(objeto) == 'Departamento 01'
        assert repr(objeto) == 'Departamento = Departamento 01'

    def test_setters(self):
        objeto = Departamento('GoogleLia', 'Gabriel', 1, 1, 1990)
        assert objeto.nome == 'GoogleLia'

        objeto.nome = 'Client/ETL'
        assert objeto.nome == 'Client/ETL'

    def test_properties(self):
        objeto = Departamento('Departamento 01', 'Gabriel', 1, 1, 1990)

        assert objeto.nome == 'Departamento 01'

    def test_responsavel(self):
        departamento = Departamento('Departamento 01', 'Gabriel', 5, 2, 1990)
        assert departamento.responsavel is 'Gabriel'

        departamento.informar_responsavel('Gabriel', 1, 1, 1990)
        assert departamento.responsavel == 'Gabriel'

    def test_responsavel_substituido(self):
        departamento = Departamento('Departamento 01', 'Gabriel', 1, 1, 1990)
        assert departamento.responsavel is 'Gabriel'

        departamento.informar_responsavel('Gabriel', 1, 1, 1990)
        assert departamento.responsavel == 'Gabriel'

        departamento.informar_responsavel('João Oliveira', 1, 1, 1995)
        assert departamento.responsavel == 'João Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento('Departamento 01', 'Gabriel', 1, 1, 1990)
        departamento.informar_responsavel('Gabriel', 1, 1, 1990)
        departamento.add_colaborador('João Oliveira', 18, 3, 1995)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)

        assert len(departamento.colaboradores) == 2

    def test_verifica_aniversariantes(self):
        lista = [('João Oliveira', '1995-03-28', 'Departamento 01'),
                   ('Luis Fernando', '1998-03-28', 'Departamento 01'),
                   ('Gabriel', '1990-03-28', 'Departamento 01')]

        dt = date.today() - timedelta(days=4)
        today = date.today()

        departamento = Departamento('Departamento 01', 'Gabriel', 1, 1, 1990)
        departamento.informar_responsavel('Gabriel', today.day, today.month, 1990)
        departamento.add_colaborador('João Oliveira', today.day, today.month, 1995)
        departamento.add_colaborador('Pedro Mendonça', dt.day, dt.month, 1993)
        departamento.add_colaborador('Luis Fernando', today.day, today.month, 1998)
        departamento.add_colaborador('Maurício Souza', dt.day, dt.month, 1085)

        aniversariantes = departamento.verifica_aniversariantes()

        assert aniversariantes == lista
        assert len(aniversariantes) == 3
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list