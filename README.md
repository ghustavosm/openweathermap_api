# OpenWeatherMap API Project

## Descrição
Este projeto é uma API REST desenvolvida em Flask que se integra à API do OpenWeatherMap para fornecer informações meteorológicas de 5 dias. Ela permite que os usuários consultem previsões do tempo para diferentes cidades e registra o histórico de chamadas da API em um banco de dados MongoDB.

## Funcionalidades
- Consultar previsões do tempo por cidade.
- Visualizar o histórico de chamadas da API.

## Tecnologias Utilizadas
- Flask
- Python
- MongoDB
- Docker

## Obtenção da API Key do OpenWeatherMap
Para que a aplicação funcione corretamente, é necessário obter uma API Key do OpenWeatherMap.

1. Acesse [OpenWeatherMap](https://openweathermap.org/).
2. Crie uma conta ou faça login se já tiver uma.
3. Navegue até a seção de API Keys e gere uma nova chave.
4. Adicione essa chave à variável `OPENWEATHER_API_KEY` no seu arquivo `.env`.

## Rotas da API

### `GET /`
- **Descrição:** Rota de boas-vindas.
- **Resposta:** Uma mensagem de boas-vindas.

### `GET /weather?city={nome_da_cidade}`
- **Descrição:** Retorna a previsão do tempo para a cidade especificada.
- **Parâmetros:**
  - `city`: Nome da cidade (opcional, padrão é "Brasília").
- **Resposta:** Dados meteorológicos da cidade especificada.

### `GET /history`
- **Descrição:** Retorna o histórico de chamadas feitas para a rota `/weather`.
- **Resposta:** Uma lista de registros de chamadas de API, incluindo detalhes como cidade, data/hora e dados meteorológicos recebidos.

## Como Configurar

### Pré-requisitos
- Python 3.9+
- MongoDB
- Docker e Docker Compose

### Instalação
1. Clone o repositório:
```
git clone https://github.com/ghustavosm/openweathermap_api.git
```

2. Navegue até o diretório do projeto:
```
cd openweathermap-api
```

3. Construa e inicie os contêineres com Docker Compose:
```
docker-compose up --build
```

4. O MongoDB e o Mongo Express estarão rodando nos contêineres Docker.

5. O Mongo Express pode ser acessado através do navegador em `http://localhost:8081`.

6. Crie e ative um ambiente virtual:
```
python3 -m venv venv
source venv/bin/activate  
```
No Windows use:
```
python3 -m venv venv
source venv\Scripts\activate
```

1. Instale as dependências:
```
pip install -r requirements.txt
```

### Configuração do Ambiente
1. Renomeie o arquivo `.env.example` para `.env`.
2. Preencha as variáveis de ambiente no arquivo `.env`.

### Execução
- Para executar a aplicação localmente:
```
python3 run.py
```


## Testes
Para executar os testes unitários, use o seguinte comando:
```
python3 -m unittest discover tests
```

## Collection do Postman
A collection do postman utilizada está na raiz do projeto, com o nome `OPENWEATHERMAP_API.postman_collection.json`
