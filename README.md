# Teste técnico ADDE Sistemas

Este projeto é parte do teste técnico proposto pela ADDE sistemas, no qual o objetivo era desenvolver um sistema contendo frontend
e backend capaz de mostrar o clima atual e a previsão do tempo a partir do input de um cidade e/ou localização do usuário.

## Exemplo de uso

![Sample frontend](https://raw.githubusercontent.com/williamguilhermesouza/ADDE-teste/master/TesteADDE.gif)

## Backend
No backend foi utilizada a tecnologia Python, na versão 3.9 com o framework Flask para: 
* Comunicação com a api externa OpenWeatherMap para pegar os dados de clima filtrado por cidade/região.
* Persistência dos dados recuperados da API por 15 minutos através de cache
* Filtragem dos dados moldando o objeto desejado a ser fornecido para o frontend
* Uso de uma rota exclusiva para recuperar os dados usando localização (latitude e longitude)
* Uso de rota exclusiva para recuperar os dados de previsão de 7 dias, utilizando o nome da Cidade desejada e Região.

O backend da aplicação pode ser testado em funcionamento através do endpoint:

`http://18.224.25.40/`

ou:

`http://addeweather.tk`

## Frontend
No Frontend foi utilizado Typescript junto ao framework Angular 11, com o objetivo de capturar entrada do usuário através de um input, 
e exibir dados recuperados do backend com base nessa entrada. Por padrão a previsão utilizada a localização atual do usuário, fornecida
pelo navegador.
* Foi criado um serviço weather que consome as informações do backend e é usado na aplicação para entregar a informação
* Foi utilizada a tipagem de dados do typescript, onde é recebido um objeto do tipo Weather do backend, que devve estar em conformidade
com os atributos esperados
* Após a consulta pelo backend é exibido para o usuário os dados através da temperatura atual, cidade, clima, e de um indicativo visual.

## Como utilizar

### Backend (Windows)

Ativar o ambiente virtual venv com as bibliotecas necessárias:

`venv\Scripts\activate`

Exportar a variável FLASK_APP, para ser usada pelo flask

`set FLASK_APP=APIController.py`

Iniciar o Flask

`flask run`

### Frontend (Windows)

Entrar na pasta de frontend e iniciar o angular (deve estar instalado) com o comando:

`ng serve -o`

## Testes

### Backend

Como biblioteca para os testes do backend foi usado o unittest (para mock da API externa) e o nose para os testes propriamente ditos
Para rodar os testes feitos para o APIService use:

`nosetests backend`

Os testes devem retornar "OK"
