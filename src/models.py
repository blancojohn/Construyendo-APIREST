#En este archivo se crean las tablas que van a estar en la base de datos
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()    #Inicializa el archivo models para interactuar con la base de datos y crear 
                     #las tablas dentro de ellas.

class Planet(db.Model): #Contiene los planetas de StarWars.
    __tablename__= 'planets'
    uid= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(200), unique= True, nullable= False)
    url= db.Column(db.String(300), unique= True)
    favorites_p= db.relationship('Favorite_Planet', backref= 'planet')

    def to_dict(self):
        return{
            "uid": self.uid,
            "name": self.name,
            "url": self.url
        }

class Favorite_Planet(db.Model):
    __tablename__= 'favorites_planets'
    uid= db.Column(db.Integer, primary_key= True)
    favorite_planet_name= db.Column(db.String(600), unique= True)
    user_uid= db.Column(db.Integer, db.ForeignKey('users.uid'))
    planet_uid= db.column(db.Integer, db.ForeignKey('planets.uid'))

    def to_dict(self):
        return{
            "uid":self.uid,
            "favorite_planet_name": self. favorite_planet_name,
            "user_uid": self.user_uid,
            "planet_uid": self.planet_uid
        }


class People(db.Model): #Contiene los personajes de StarWars.
    __tablename__= 'characters'
    uid= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(200), unique= True, nullable= False)
    url= db.Column(db.String(300), unique= True,)
    favorites_c= db.relationship('Favorite_People', backref='people')#Un personaje puede ser favorito de mucho usuarios

    def to_dict(self):  #CONVIERTE EL OBJETO CLASE EN UN DICCIONARIO#
        return{
            "uid": self.uid,
            "name": self.name,
            "url": self.url
        }
        
class Favorite_People(db.Model): #Contiene los personajes favoritos seleccionados por los usuarios
    __tablename__= 'favorites characters'
    uid= db.Column(db.Integer, primary_key= True)
    favorite_people_name= db.Column(db.String(600), unique= True)
    user_uid= db.Column(db.Integer, db.ForeignKey('users.uid'))
    people_uid= db.Column(db.Integer, db.ForeignKey('characters.uid'))

    def to_dict(self):
        return{
            "uid": self.uid,
            "favorite_people_name": self.favorite_people_name,
            "user_uid": self.user_uid,
            "people_uid": self.people_uid
        }

class User(db.Model): #Contiene a los usuarios que se agregan al block
    __tablename__ = 'users'
    uid= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(120), nullable=False, unique=True)
    favorites_characters= db.relationship('Favorite_People', backref= 'user')
    favorites_characters= db.relationship('Favorite_Planet', backref= 'user')
    #A FUTURO SE AGREGARÁ EMAIL Y PASSWORD PARA IMPLEMENTAR JWT.

    def to_dict(self):
        return {
            "id": self.uid,
            "username": self.username
        }
   