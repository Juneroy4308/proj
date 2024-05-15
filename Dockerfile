FROM python:3.9

RUN pip install Flask requests jsonify Flask-SQLAlchemy

WORKDIR /appd
COPY . /appd

EXPOSE 5000

CMD ["python", "app.py"]
