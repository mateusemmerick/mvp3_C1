# Minha API

Este pequeno projeto faz parte do mvp da Disciplina **Desenvolvimento Full Stack Avançado** 

O objetivo aqui é colocar em prática o conteúdo apresentado ao longo da disciplina, por meio de um projeto real.

## O Projeto

O projeto consiste em um site para comercialização de iPhones. Por meio dele é possível ofertar e comprar um iPhone.
Essa API específica, é referente ao estoque, ou seja, todos os produtos cadastrados no site.

---
### Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

Essa API também poderá ser executada via docker, utilizando os seguintes comandos (necessário possuir docker desktop instalado):

Criação da imagem
```
docker build . -t <Nome da imagem>
```
Execução da imagem
```
docker run -d -p 5000:5000 <Nome da imagem>
```
