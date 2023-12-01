FROM python:3.9-slim

LABEL maintainer="Jotheeswaran Lakshmanan"

WORKDIR /app

COPY sample-app-ui/static /app/static

COPY sample-app-ui/templates /app/templates

COPY sample-app-ui/requirements.txt /app

COPY sample-app-ui/app.py /app

RUN pip install -r ./requirements.txt

RUN useradd -r -u 5577 appuser

RUN chown -R appuser:appuser /app

USER 5577

CMD ["python", "-u", "./app.py"]
