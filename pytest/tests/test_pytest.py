#pip install pytest

from pytest import mark, fixture
from codigo.jogo import brincadeira

import sys

def test_meu_primeiro_teste():
    assert True

#para rodar os testes, execute o comando:
# $ pytest -v -x

#modo debug
# $ pytest --pdb 
#vai abrir no terminal o (Pdb), voce pode digitar o nome das variaveis e ver o valor.
#para sair, digite q

#gerar report ao final do teste
# $ pytest --junitxml resultado.xml

#para rodar todos os testes que contém no nome da função um determinado texto, execute o comando:
# $ pytest -k "goiabada"

#grupos de testes
# $ pytest -m "goiabada" -v




"""
O teste é formado por 3 etapas (GWT - AAA):
- Given - Dado
- When - Quando
- Then - Então

- Arrange
- Act
-Assert
"""

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    """
    - Brincadeira - SUT - System Under Test
    """
    entrada = 1 #dado
    esperado = 1 #dado
    resultado = brincadeira(entrada) #quando
    assert resultado == esperado #então

def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2

@mark.smoke
def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'

@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

@mark.skip(reason="nao quero rodar esse teste")
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

@mark.smoke
@mark.goiabada
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'

# $ pytest -m parametrizado
#@mark.parametrizado
@mark.parametrize(
    'entrada', [5,10,20,25,35]
)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    assert brincadeira(entrada) == 'goiabada'

@mark.parametrizado
@mark.parametrize(
    'entrada, esperado', 
    [(1,1),(2,2), (3,"queijo"), (4,4), (5,"goiabada")]
)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada,esperado):
    assert brincadeira(entrada) == esperado


@mark.xfail
def test_xfail2():
    assert brincadeira(20) == 'goiabada'

@mark.xfail
def test_xfail1():
    assert brincadeira(20) != 'goiabada'

@mark.xfail(sys.platform == 'win32')
def test_xfail_windows():
    assert brincadeira(20) != 'goiabada'

@mark.skipif(sys.platform == 'win32')
def test_xfail_windows():
    assert brincadeira(20) != 'goiabada'

@mark.stdout
def test_brincadeira_deve_escrever_entrei_na_brincadeira_na_tela(capsys):
    brincadeira(0)
    resultado = capsys.readouterr()
    assert resultado.out == 'entrei na brincadeira!\n'

@fixture
def minha_fixture():
    print("executando minha fixture")
    yield
    print("finalizando minha fixture")

@mark.exemplo_fixture
def test_minha_fixture_em_acao(minha_fixture):
    print(minha_fixture)