# Este projeto foi desenvolvido para fins didáticos

# O que ele faz?
Utilizando o framwork Scrapy, o programa permite acessar a url de ofertas do dia do Magazine Luiza e persistir as informações em banco mongoDB.

# Dependências:
    * Python 3.5+ (Recomendo o uso de virtualenv)
    * pip
    * mongoDB server

# Como executa-lo?
    - Inicialmente clone o repositório para o local de sua preferência;
    - Crie um ambiente de desenvolvimento do python com uma versão 3.5+ (virtualenv);
    - Através do pip instale as dependências do requirements.txt EX: "pip install -r requirements.txt";
    - Insira as credênciais de seu mongodb server no arquivo .env (subistitua a informação do .env atual por suas informações);

    - Atualize as váriaveis de ambiente "set -a; source .env; set +a"; (rode este comando no mesmo diretório do arquivo .env);
    - Acesse o diretório: 'luizaScraper/';
    - Execute o comando 'scrapy crawl MagaluScraper'.

    Ao realizar as etapas acima o script realizará a consulta no site e irá gravar no mongoDB.

# Futuras implementações:
    - Preços de produtos;
    - Integração com API;
    - Mapeamento de outros endpoints;
    - Testes (pytest).