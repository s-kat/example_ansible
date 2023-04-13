FROM python:alpine3.17

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /app/
COPY . /app/
WORKDIR /app/

EXPOSE 8000
ARG app_version
ENV APP_VERSION=$app_version
CMD ["gunicorn", "hello:app", "--bind", "0.0.0.0:8000", "--workers", "3"]
