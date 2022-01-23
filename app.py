from flask import Flask
from flask_restx import Api

from config import Config
from models import Movie, Director
from setup_db import db
from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()

    return app

def configure_app(app : Flask):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)

# def load_data():
#     m1 = Movie(id=1, description="Хорошее кино", director_id=1)
#     m2 = Movie(id=2, description="О любви", director_id=2)
#     m3 = Movie(id=3, description="Кто-то мимо ходил", director_id=3)
#     m4 = Movie(id=4, description="Прекрасные пейзажи", director_id=4)

    # d1 = Director(id=1, name="Гарри Поттер и Тайная Комната")
    # d2 = Director(id=2, name="Граф Монте-Кристо")
    # d3 = Director(id=3, name="Гарри Поттер и Орден Феникса")
    # d4 = Director(id=4, name="Гарри Поттер и Кубок Огня")
    db.create_all()
    # with db.session.begin():
        # db.session.add_all([d1, d2, d3, d4])
        # db.session.add_all([m1, m2, m3, m4])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    # load_data()
    app.run(host="localhost", port=10001, debug=True)



# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

# from flask import Flask
# from flask_restx import Api
#
# from config import Config
# from models import Review, Book
# from setup_db import db
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app
# def create_app(config_object):
#     app = Flask(__name__)
#     app.config.from_object(config_object)
#     register_extensions(app)
#     return app
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
# def register_extensions(app):
#     db.init_app(app)
#     api = Api(app)
#     api.add_namespace(...)
#     create_data(app, db)
#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)



