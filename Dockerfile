FROM python:3.6.8

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000
#CMD [ "uvicorn", "app.ApiServer:app", "--host","0.0.0.0","--port","8000","--reload"]