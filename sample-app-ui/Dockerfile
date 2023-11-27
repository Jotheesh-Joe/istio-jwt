FROM python:3.9-slim

LABEL maintainer="JotheeswaranLakshmanan"

WORKDIR /app

COPY . /app

RUN pip install -r ./requirements.txt

RUN useradd -r -u 5577 appuser

RUN chown -R appuser:appuser /app

USER 5577

CMD ["python", "-u", "./app.py"]