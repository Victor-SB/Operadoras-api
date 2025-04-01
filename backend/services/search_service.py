import pandas as pd

class SearchService:
    def __init__(self, csv_file="operadoras.csv"):
        self.df = pd.read_csv(csv_file)

    def buscar_operadora(self, nome: str):
        resultado = self.df[self.df["nome"].str.contains(nome, case=False, na=False)]
        return resultado.to_dict(orient="records")