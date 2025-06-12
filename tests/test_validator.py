# Testes unitários das funções de validação
# Testes unitários para cada regra de validação.
# Garante que modificações futuras não quebrem regras anteriores.

import sys
import os
import pytest

# Adiciona o diretório src ao sys.path para os imports funcionarem nos testes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from validator import check_length, check_common_password, validate_password

def test_check_length():
    assert check_length("1234567")[0] == False
    assert check_length("12345678")[0] == True

def test_check_common_password():
    assert check_common_password("12345678")[0] == False
    assert check_common_password("senhaSegura")[0] == True

def test_validate_password():
    assert validate_password("1234567")[0] == False
    assert validate_password("12345678")[0] == False
    assert validate_password("senhaSegura")[0] == True
