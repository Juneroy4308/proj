FROM python:3.9

RUN pip install Flask requests jsonify Flask-SQLAlchemy

WORKDIR /appd
COPY . /appd

EXPOSE 5050

CMD ["python", "app.py"]
