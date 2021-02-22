FROM rasa/rasa-sdk:2.3.1

COPY actions /app/actions

USER root
RUN pip install --no-cache-dir -r /app/actions/requirements-actions.txt

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN rasa train --domain domain.yml --data data --out models

EXPOSE 5005

USER 1001
CMD ["run", "--enable-api" ]
