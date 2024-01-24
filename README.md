# macanix-chatbot
No Azure, o chat executa como container. Para executar deve ser criada uma aplicação para containers e colocar o link do docker.

## Treinar modelo
rasa train

## Executar com linha de comando
rasa shell

## Executar como serviço
rasa run --m ./models --endpoints endpoints.yml --port 5005 -vv --enable-api --cors "*"