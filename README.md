# macanix-chatbot

## Treinar modelo
rasa train

## Executar com linha de comando
rasa shell

## Executar como serviço
rasa run --m ./models --endpoints endpoints.yml --port 5005 -vv --enable-api --cors "*"