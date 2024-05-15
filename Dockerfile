FROM python:3.9

RUN pip install Flask requests jsonify Flask-SQLAlchemy

WORKDIR /app
COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
