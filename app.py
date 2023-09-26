from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError


from model import Session, EstoqueProduto
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)


CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Documentação em Swagger")
estoque_tag = Tag(name="Estoque ", description="Adição, visualização, edição e remoção de produtos a tabela de estoque")
api_externa_tag = Tag(name="API Externa ", description="Consulta de dados na API Externa.")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger, que é a documentação swagger.
    """
    return redirect('/openapi/swagger')


@app.get('/estoque', tags=[estoque_tag],
         responses={"200": ListagemEstoqueSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os produtos cadastrados no estoque.

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(EstoqueProduto).all()

    if not produtos:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d produtos encontrados" % len(produtos))
        # retorna a representação de produto
        print(produtos)
        return apresenta_estoque(produtos), 200

@app.get('/produto', tags=[estoque_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: EstoqueBuscaSchema):
    """Faz a busca por um produto do estoque a partir do id.

    Retorna uma representação do produto.
    """
    produto_id = query.id
    logger.debug(f"Coletando dados sobre produto #{produto_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produto = session.query(EstoqueProduto).filter(EstoqueProduto.id == produto_id).first()

    if not produto:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{produto.modelo}'")
        # retorna a representação de produto
        return apresenta_produto(produto), 200

@app.post('/produto', tags=[estoque_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: EstoqueSchema):
    """Adiciona um novo produto ao estoque.

    Retorna uma representação do produto.
    """    
    produto = EstoqueProduto(        
        modelo = form.modelo,
        memoria = form.memoria,
        saude = form.saude,
        estado_uso = form.estado_uso,
        cabo = form.cabo,
        cabo_original = form.cabo_original,
        carregador = form.carregador,
        carregador_original = form.carregador_original,
        fone = form.fone,
        capinha = form.capinha,
        cep = form.cep,
        cidade =  form.cidade,
        estado =  form.estado,        
        preco = form.preco)   
    
    logger.debug(f"Adicionando produto: '{produto.modelo}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado produto: '{produto.modelo}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        # como a duplicidade do código é a provável razão do IntegrityError
        error_msg = "Produto de mesmo código já salvo na base:/"
        logger.warning(f"Erro ao adicionar produto '{produto.modelo}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar o novo item:/"
        logger.warning(f"Erro ao adicionar produto '{produto.modelo}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.delete('/produto', tags=[estoque_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: EstoqueBuscaSchema):
    """Deleta um produto do estoque a partir do id informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    id_produto = query.id
    print(id_produto)
    logger.debug(f"Deletando dados sobre produto #{id_produto}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(EstoqueProduto).filter(EstoqueProduto.id == id_produto).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto de id {id_produto}")
        return {"mesage": "Produto removido", "id": id_produto}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base:/"
        logger.warning(f"Erro ao deletar produto código '{id_produto}', {error_msg}")
        return {"mesage": error_msg}, 404

@app.put('/produto/<string:id>', tags=[estoque_tag],
            responses={"200":ProdutoViewSchema, "404":ErrorSchema})
def merge_produto(path:EstoqueBuscaSchema, form:EstoqueSchema):
    """Edita um produto da base do estoque, com base no id.

    Retorna uma representação do produto.
    """    
    produto = EstoqueProduto(
        modelo = form.modelo,
        memoria = form.memoria,
        saude = form.saude,
        estado_uso = form.estado_uso,
        cabo = form.cabo,
        cabo_original = form.cabo_original,
        carregador = form.carregador,
        carregador_original = form.carregador_original,
        fone = form.fone,
        capinha = form.capinha,
        cep = form.cep,
        cidade =  form.cidade,
        estado =  form.estado,        
        preco = form.preco) 
    logger.debug(f"Editando produto: '{produto.modelo}'")
    try:
        # criando conexão com a base
        session = Session()
        produtoUpdate = session.query(EstoqueProduto).get(path.id) 
        produtoUpdate.modelo = form.modelo
        produtoUpdate.memoria = form.memoria
        produtoUpdate.saude = form.saude
        produtoUpdate.estado_uso = form.estado_uso
        produtoUpdate.cabo = form.cabo
        produtoUpdate.cabo_original = form.cabo_original
        produtoUpdate.carregador = form.carregador
        produtoUpdate.carregador_original = form.carregador_original
        produtoUpdate.fone = form.fone
        produtoUpdate.capinha = form.capinha
        produtoUpdate.cep = form.cep
        produtoUpdate.cidade =  form.cidade
        produtoUpdate.estado =  form.estado        
        produtoUpdate.preco = form.preco     
        # atualizando produto  
        print(produtoUpdate)     
        session.commit()
        logger.debug(f"Atualizado produto: '{produto.modelo}'")
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        # como a duplicidade do código é a provável razão do IntegrityError
        error_msg = "Produto de mesmo código já salvo na base:/"
        logger.warning(f"Erro ao adicionar produto '{produto.modelo}', {error_msg}")
        return {"mesage": 'error_msg'}, 409

    except Exception as e:
        # # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item:/"
        # logger.warning(f"Erro ao adicionar produto '{produto.modelo}', {error_msg}")
        logger.warning(f"Erro: {e} \n")
        return {"mesage": error_msg}, 400
