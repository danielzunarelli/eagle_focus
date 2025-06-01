![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Terminal](https://img.shields.io/badge/terminal-%23000000.svg?style=for-the-badge&logo=gnubash&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

# Projeto: Eagle Focus

## Aplicativo de gerenciamento de foco em Python

O **Eagle Focus** é um aplicativo construído em Python que permite registrar e controlar o tempo dedicado a diferentes atividades com foco total. Ele funciona diretamente via terminal e salva todas as sessões em um banco de dados SQLite local.

Seu diferencial está na simplicidade: um sistema de navegação intuitivo em texto, sem interface gráfica, com foco absoluto em produtividade. Ideal para desenvolvedores, estudantes e profissionais que desejam acompanhar quanto tempo realmente focaram em cada tarefa.

---

## Funcionalidades

- Cadastro, listagem, exclusão e reset de "Focus" (atividades)
- Cronômetro com opções de `Iniciar`, `Pausar`, `Retomar` e `Parar`
- Armazenamento automático em banco de dados local SQLite
- Registro de sessões com `timestamp`
- Acúmulo de tempo por atividade
- Spinner animado no terminal durante execução do tempo

---

## Como configurar

Para que o banco de dados fique salvo em um local de sua preferência, edite o caminho no arquivo `db.py`:

```python
def connect():
    return sqlite3.connect("/Users/seu_usuario/data/eagle_focus.db")
```

---

## Estrutura do projeto

```
eagle_focus/
├── db.py
├── main.py
├── menu.py
├── start_menu.py
├── focus_menu.py
├── focus_timer.py
└── README.md
```

---

## Como executar o projeto

```bash
python3 main.py
```

Ou, se preferir, crie um alias no terminal para facilitar:

```bash
alias eaglefocus="python3 /caminho/para/o/main.py"
```

---

## Prints do App:

<img width="254" alt="Screenshot 2025-05-31 at 21 56 31" src="https://github.com/user-attachments/assets/b8680d79-bc1c-4874-8ea4-f3a06b257934" />
<img width="209" alt="Screenshot 2025-05-31 at 21 56 53" src="https://github.com/user-attachments/assets/9aecb043-b430-4040-a07f-d9819b0c3871" />

---

## Próximas atualizações

- Dashboard de sessões (tempo total por foco)
- Filtros por mês, semana ou datas personalizadas
- Front-end para visualização e controle
- Exportação de sessões em CSV ou PDF
- Modo pomodoro

---

**Simples. Direto. Foco total.**

---
