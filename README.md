# Password Validator

Validador de senha simples, modular e profissional em Python.

---

## 📋 Descrição

Este projeto implementa um validador de senha por linha de comando (CLI), com código limpo, modular, testável e fácil de expandir. Desenvolvido como referência de boas práticas de Engenharia de Software.

---

## 🚀 Funcionalidades

- Validação de senha seguindo duas regras:
    - Mínimo de 8 caracteres
    - Não pode ser igual a "12345678"
- Mensagens de feedback centralizadas
- Pronto para receber novas regras de validação
- Estrutura para testes automatizados com pytest

---

## 🏗️ Estrutura do Projeto

```bash
password_validator/
├── src/
│ ├── main.py # Entrada da aplicação (CLI)
│ ├── cli.py # Interface com usuário
│ ├── validator.py # Lógica das regras de validação
│ ├── messages.py # Mensagens centralizadas
│ └── init.py
├── tests/
│ ├── test_validator.py
│ └── init.py
├── README.md
└── .gitignore
```
---

## ⚙️ Como Executar

1. Clone este repositório e acesse a pasta do projeto:

    ```bash
    git clone https://github.com/SamuelASantos/password_validator.git
    cd password_validator
    ```

2. Execute a aplicação pelo terminal:

    ```bash
    python -m src.main
    ```

3. Digite uma senha e veja o resultado da validação.

---

## 🧪 Como Rodar os Testes

1. Instale o pytest (caso não tenha):

    ```bash
    pip install pytest
    ```

2. Execute os testes a partir da raiz do projeto:

    ```bash
    pytest
    ```

---

## ✨ Boas Práticas Aplicadas

- Código modular e separado por responsabilidades
- Mensagens centralizadas para manutenção fácil
- Estrutura pronta para testes automatizados
- Pronto para expansão com novas regras
- README detalhado para fácil entendimento

---

## 📈 Evolução sugerida

- Novas regras de validação (ex: letras maiúsculas, caracteres especiais, blacklist)
- Interface gráfica (GUI) ou web
- Internacionalização das mensagens
- Integração com sistemas maiores

---

## 👨‍💻 Autor

Samuel Santos  
Estudante de Engenharia de Software

---

Sinta-se à vontade para contribuir, sugerir melhorias ou reportar problemas!
