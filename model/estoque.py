from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, Float
from model.base import Base

class EstoqueProduto(Base):
    __tablename__ = 'estoque_produto'

    id = Column("pk_produto", Integer, primary_key=True)        
    modelo = Column(String(25))
    memoria = Column(Integer)
    saude = Column(Integer)
    estado_uso = Column(String(25))
    cabo = Column(Boolean) 
    cabo_original = Column(Boolean) 
    carregador = Column(Boolean)
    carregador_original = Column(Boolean)
    fone = Column(Boolean)
    capinha = Column(Integer)
    cep = Column(String(25))
    cidade = Column(String(25))
    estado =  Column(String(25))    
    preco = Column(Float)
        

    def __init__(self, modelo:str, memoria:int, saude:int, estado_uso:str, cabo:bool, cabo_original:bool,carregador:bool, carregador_original:bool, fone:bool,capinha:int, cep: str, cidade:str,estado:str, preco:float):    
        """
        Cadastra um novo produto ao estoque

        Argumentos:        
        modelo: modelo do iphone
        memoria: memória interna 
        saude: saude da bateria 
        estado_uso: estado de uso do iphone
        cabo: se possui cabo
        cabo_original: se possui cabo original
        carregador: se possui carregador
        carregador_original: se possui carregador original
        fone: se possui fone
        capinha: quantidade de capinhas
        cep: cep do vendedor
        cidade: cidade do vendedor
        estado: estado do vendedor
        preco: valor do iphone
        """        
        self.modelo = modelo
        self.memoria = memoria
        self.saude = saude
        self.estado_uso = estado_uso
        self.cabo = cabo
        self.cabo_original = cabo_original
        self.carregador = carregador
        self.carregador_original = carregador_original
        self.fone = fone
        self.capinha = capinha
        self.cep = cep
        self.cidade = cidade
        self.estado = estado        
        self.preco = preco