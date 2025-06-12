# Lógica de validação de senha (funções de regras)
# Onde ficam as regras de validação: cada regra em uma função separada (check_length, check_common_password, etc).
# Uma função central (validate_password) pode combinar todas as regras e retornar resultado e mensagens.
# Pronto para expansão: novas regras podem ser adicionadas facilmente.

from .messages import MSG_MIN_LENGTH, MSG_COMMON

def check_length(password: str) -> (bool, str): # type: ignore
    if len(password) < 8:
        return False, MSG_MIN_LENGTH
    return True, ""

def check_common_password(password: str) -> (bool, str): # type: ignore
    if password == "12345678":
        return False, MSG_COMMON
    return True, ""

def validate_password(password: str) -> (bool, str): # type: ignore
    checks = [check_length, check_common_password]
    for check in checks:
        valid, reason = check(password)
        if not valid:
            return False, reason
    return True, ""
