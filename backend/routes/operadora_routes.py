from fastapi import APIRouter, Query
from services.search_service import SearchService

router = APIRouter()
search_service = SearchService()

@router.get("/buscar")
def buscar_operadora(nome: str = Query(..., description="Nome da operadora")):
    return search_service.buscar_operadora(nome)