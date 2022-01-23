from setup_db import db
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")
    # genre = relationship("Genre", foreign_keys=[genre_id])
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))
    director = db.relationship("Director")
    # director = relationship("Director", foreign_keys=[director_id])

class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    director_id = fields.Int()
    genre_id = fields.Int()

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)



class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)




class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)



# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)

# Пример
# from setup_db import db
#
# class Book(db.Model):
#     __tablename__ = ‘book’
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     author = db.Column(db.String)
#     year = db.Column(db.Integer)