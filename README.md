# Operadoras API 📡

API desenvolvida em FastAPI para busca de operadoras de saúde com base no **Registro ANS**.

## 🚀 Funcionalidades

- 🔍 **Buscar operadoras** pelo **Registro ANS**
- 📂 **Importação automática** de um arquivo CSV com os dados das operadoras
- ⚡ **Rápida e eficiente** usando FastAPI

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.11**
- ⚡ **FastAPI**
- 📦 **Pandas**
- 🔥 **Uvicorn**

## 🚀 Como Executar


1. **Clone o repositório**:
   ```sh
   git clone https://github.com/seu-usuario/operadoras-api.git
   cd operadoras-api
   
   python -m venv venv
   venv\Scripts\activate   
   3. Instale as dependências:
   
   4. Inicie a API:
   uvicorn backend.main:app --reload
   5. Acesse a API via Swagger UI:
   👉 http://127.0.0.1:8000/docs

2. **Crie um ambiente virtual e ative:**:
```sh
    python -m venv venv
    venv\Scripts\activate
```
3. **Instale as dependências:**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Inicie a API:**:
   ```sh
   uvicorn backend.main:app --reload
5. **Acesse a API via Swagger UI: **:
   ```sh
    👉 http://127.0.0.1:8000/docs
   
📜 Endpoints

🔍 Buscar Operadora

GET /buscar?registro_ans=<ANS>

Exemplo de resposta:
[
  {
    "Registro_ANS": "12345",
    "CNPJ": "12.345.678/0001-90",
    "Razao_Social": "Operadora X",
    "DDD": "11",
    "Telefone": "4002-8922",
    "Representante": "Fulano de Tal"
  }
]

Desenvolvido por Victor Hugo
