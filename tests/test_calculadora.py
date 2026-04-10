import pytest
from src.calculadora import *

def test_soma():
    assert soma(2, 3) == 5

def test_divisao():
    assert divisao(6, 2) == 3

def test_divisao_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)

def test_soma_negativo():
    assert soma(-1, -1) == -2

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6

def test_subtracao():
    assert subtracao(5, 3) == 2

def test_zero():
    assert soma(0, 0) == 0

def test_grande():
    assert soma(1000, 2000) == 3000

def test_decimal():
    assert divisao(5, 2) == 2.5

def test_string():
    with pytest.raises(TypeError):
        soma("a", 2)

def test_none():
    with pytest.raises(TypeError):
        soma(None, 2)

def test_lista():
    with pytest.raises(TypeError):
        soma([1], 2)

def test_dict():
    with pytest.raises(TypeError):
        soma({}, 1)

def test_divisao_string():
    with pytest.raises(TypeError):
        divisao("a", 2)

def test_subtracao_string():
    with pytest.raises(TypeError):
        subtracao("a", 1)

def test_multiplicacao_string():
    with pytest.raises(TypeError):
        multiplicacao("a", "b")

def test_divisao_none():
    with pytest.raises(TypeError):
        divisao(None, 1)

def test_multiplicacao_none():
    with pytest.raises(TypeError):
        multiplicacao(None, 2)

def test_subtracao_negativo():
    assert subtracao(-5, -3) == -2

def test_multiplicacao_negativo():
    assert multiplicacao(-2, 3) == -6