# 🧠 P.I.T.E.R – Backend API

> **Plataforma de Integração e Transparência em Educação e Recursos (P.I.T.E.R)**  
> Backend desenvolvido em **FastAPI**, responsável por integrar dados externos, processar informações e servir o frontend da aplicação.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI** – Framework moderno e performático para APIs REST.
- **Uvicorn** – Servidor ASGI de alta performance.
- **Pydantic Settings** – Gerenciamento de variáveis de ambiente.
- **Python Dotenv** – Carregamento de variáveis via `.env`.

---

## 🏗️ Estrutura de Pastasbackend/
│
├── app/
│ ├── core/ # Configurações principais (logging, settings)
│ ├── integration/ # Serviços e integrações externas
│ │ ├── api/
│ │ │ └── clients/ # Clientes HTTP externos (ex: Querido Diário)
│ │ └── piter_api_orchestrator.py
│ ├── main.py # Ponto de entrada da aplicação
│ └── init.py
│
├── requirements.txt # Dependências do projeto
├── .env.example # Variáveis de ambiente de exemplo
└── README.md # Documentação do backend

## 🧪 Testes Automatizados

Este backend utiliza **pytest** para testes automatizados de endpoints.

### ▶️ Como rodar os testes

Ative o ambiente virtual:
```bash
venv\Scripts\activate
Execute todos os testes:

bash
Copiar código
pytest -v
🧠 Testes implementados
/health → Verifica se o servidor está online e respondendo corretamente.

Resultado esperado:

arduino
Copiar código
tests/test_health.py::test_health_endpoint PASSED
sql
Copiar código

Depois, no terminal:
```bash
git add README.md
git commit -m "docs: adicionar instruções de teste automatizado ao README"
git push origin adaptar_arquitetura
---

## ⚙️ Configuração do Ambiente

### 1️⃣ Crie o ambiente virtual

```bash
python -m venv venv


Ative o ambiente:

Windows (PowerShell):
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

2️⃣ Instale as dependências
pip install -r requirements.txt

3️⃣ Execute a aplicação
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000


Acesse no navegador:

🌐 http://127.0.0.1:8000/
 → status da API

🧩 http://127.0.0.1:8000/docs
 → documentação interativa (Swagger UI)

🩺 http://127.0.0.1:8000/health
 → endpoint de verificação de saúde



