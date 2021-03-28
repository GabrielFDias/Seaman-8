from rh.classes.Departamento import Departamento
from datetime import date, timedelta

dt1 = date.today() - timedelta(days=4)
hoje = date.today()

departamento = Departamento('Departamento 01')
departamento.informar_responsavel('Gabriel Dias', dt1.day, dt1.month, 1990)
departamento.add_colaborador('João Oliveira', hoje.day, hoje.month, 1995)
departamento.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
departamento.add_colaborador('Luis Fernando', hoje.day, hoje.month, 1998)
departamento.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1985)

aniversariantes = departamento.verifica_aniversariantes()

for aniversariante in aniversariantes:
    print('Parabéns ' + aniversariante[0] + ' pelo seu dia')
