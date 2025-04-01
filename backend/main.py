from fastapi import FastAPI, Query
import os
import pandas as pd

app = FastAPI()

# Obtém o caminho absoluto do arquivo CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "operadoras.csv")

# Verifica se o arquivo existe antes de tentar carregar
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"Arquivo CSV não encontrado: {CSV_PATH}")

# Carregar o CSV ao iniciar a API, incluindo apenas as colunas necessárias
colunas_necessarias = ["Registro_ANS", "CNPJ", "Razao_Social", "DDD", "Telefone", "Representante"]
df = pd.read_csv(CSV_PATH, delimiter=";", usecols=colunas_necessarias, encoding="utf-8", on_bad_lines="skip")

@app.get("/buscar")
def buscar_operadora(registro_ans: str = Query(..., description="Registro ANS da operadora")):
    """Busca operadoras pelo Registro ANS informado na query."""
    
    # Verifica se a coluna 'Registro_ANS' existe no CSV
    if "Registro_ANS" not in df.columns:
        return {"error": "Coluna 'Registro_ANS' não encontrada no arquivo CSV"}
    
    # Realiza a busca pelo Registro ANS
    resultado = df[df["Registro_ANS"].astype(str) == registro_ans]

    # Retorno amigável caso nada seja encontrado
    if resultado.empty:
        return {"message": "Nenhuma operadora encontrada com esse Registro ANS."}

    return resultado.to_dict(orient="records")