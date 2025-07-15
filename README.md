# 🏆 Golden Raspberry Awards API (outsera)

API RESTful para leitura e análise da categoria **Pior Filme** do Golden Raspberry Awards, com base em um arquivo CSV de filmes vencedores.

---

## 📌 Descrição

A API permite consultar os produtores com:

- ✅ Menor intervalo entre duas vitórias consecutivas
- ✅ Maior intervalo entre duas vitórias consecutivas

> ℹ️ Este README foi gerado com auxílio de inteligência artificial (ChatGPT).

---

## 🚀 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) – Web framework moderno
- [SQLModel](https://sqlmodel.tiangolo.com/) – ORM baseado em SQLAlchemy + Pydantic
- [SQLite](https://www.sqlite.org/index.html) – Banco local em arquivo
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI leve
- [Pytest](https://docs.pytest.org/) – Testes de integração

---

## 🗂 Estrutura do Projeto

```
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── services.py
│   └── routers.py
├── tests/
│   └── test_awards.py
├── Movielist.csv
├── database.db           # Gerado automaticamente
├── requirements.txt
└── README.md
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/Pilonetto/avaliacao-backend-outsera.git
cd avaliacao-backend-outsera
```

### 2. Crie e ative um ambiente virtual:

#### Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

---

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

### 4. Inicie a API:

```bash
uvicorn app.main:app --reload
```

Acesse a documentação interativa em:

```
http://localhost:8000/docs
```

---

## 🧪 Rodando os testes

Os testes são de integração e verificam se a API responde corretamente.

### ⚠️ Passo único:

```bash
pytest
```

> 💡 A estrutura já ajusta o caminho automaticamente para importar `app.main`.

---

## 📥 Requisitos atendidos

- [x] Leitura do CSV ao iniciar
- [x] Armazenamento em banco local (SQLite)
- [x] Endpoint `/producers/interval-awards`
- [x] Resposta no formato especificado
- [x] Testes de integração cobrindo estrutura e tipos
- [x] FastAPI nível 2 da maturidade de Richardson

---

## ✍️ Autor

Desenvolvido como parte de um teste técnico.
