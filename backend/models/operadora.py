from pydantic import BaseModel

class Operadora(BaseModel):
    id: int
    nome: str
    cnpj: str
    cidade: str