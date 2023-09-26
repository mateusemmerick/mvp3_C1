import sys
sys.path.append('meu_app_api\model')
from pydantic import BaseModel
from typing import Optional, List
from model.estoque import EstoqueProduto


class EstoqueSchema(BaseModel):
    """ Define como uma nova entrada no estoque deve ser representada
    """   
    id: int = 1
    modelo: str = "11"
    memoria: int = 128
    saude: int = 95
    estado_uso: str = "Excelente"
    cabo: bool = False
    cabo_original: bool = True
    carregador: bool = False
    carregador_original: bool = True
    fone: bool = True
    capinha: int = 1
    cep: str = "89258000"
    cidade: str = "Jaraguá do Sul"
    estado: str = "Santa Catarina"    
    preco: float = 2200.00
  

class EstoqueBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca, que será
        feita apenas com base no id do produto
    """
    id: int = 1


class ListagemEstoqueSchema(BaseModel):
    """ Define como uma listagem de estoque será retornada.
    """
    estoque:List[EstoqueSchema]


def apresenta_estoque(estoque: List[EstoqueSchema]):
    """ Retorna uma representação do estoque seguindo o schema definido em
        EstoqueSchema.
    """
    result = []
    for prod in estoque:
        result.append({
            "id": prod.id,
            "modelo": prod.modelo,
            "memoria": prod.memoria,
            "estado_uso": prod.estado_uso,
            "saude": prod.saude,
            "cabo": prod.cabo,
            "cabo_original": prod.cabo_original,
            "carregador": prod.carregador,
            "carregador_original": prod.carregador_original,
            "fone": prod.fone,
            "capinha": prod.capinha,
            "cep": prod.cep,
            "cidade": prod.cidade,
            "estado": prod.estado,            
            "preco": prod.preco
        })

    return {"estoque": result}


class ProdutoViewSchema(BaseModel):
    """ Define como uma entrada de um produto será retornada
    """   
    id: int = 1
    modelo: str = "11"
    memoria: int = 128
    saude: int = 95
    estado_uso: str = "Excelente"
    cabo: bool = False
    cabo_original: bool = True
    carregador: bool = False
    carregador_original: bool = True
    fone: bool = True
    capinha: int = 1
    cep: str = "89258000"
    cidade: str = "Jaraguá do Sul"
    estado: str = "Santa Catarina"    
    preco: float = 2200.00

class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_produto(prod: EstoqueProduto):
    """ Retorna uma representação da entrada do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": prod.id,
        "modelo": prod.modelo,
        "memoria": prod.memoria,
        "estado_uso": prod.estado_uso,
        "saude": prod.saude,
        "cabo": prod.cabo,
        "cabo_original": prod.cabo_original,
        "carregador": prod.carregador,
        "carregador_original": prod.carregador_original,
        "fone": prod.fone,
        "capinha": prod.capinha,
        "cep": prod.cep,
        "cidade": prod.cidade,
        "estado": prod.estado,        
        "preco": prod.preco
    }