# Lida com input/output (interface com usuário)
# Responsável apenas pela interface: exibe mensagens, lê senha do usuário e apresenta feedback.
# Não implementa regras de validação.

from .messages import PROMPT_PASSWORD, MSG_VALID, MSG_INVALID
from .validator import validate_password

def run():
    password = input(PROMPT_PASSWORD)
    is_valid, reason = validate_password(password)
    if is_valid:
        print(MSG_VALID)
    else:
        print(MSG_INVALID.format(reason=reason))
