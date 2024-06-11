from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa


db = SQLAlchemy()

class Planet(db.Model): #Contiene los planetas de StarWars.
    __tablename__= 'planets'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable= False)
    url= db.Column(db.String(300), nullable= False)
    favorites_p= db.relationship('Favorite_Planet', backref= 'planet')

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "url": self.url
        }

class Favorite_Planet(db.Model):
    __tablename__= 'favorites_planets'
    id= db.Column(db.Integer, primary_key= True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    planet_id= db.Column(db.Integer, db.ForeignKey('planets.id'))

    def to_dict(self):
        return{
            "id":self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }


class People(db.Model): #Contiene los personajes de StarWars.
    __tablename__= 'characters'
    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(200), nullable= False)
    url= db.Column(db.String(300), nullable= False)
    favorites_c= db.relationship('Favorite_People', backref='people')#Un personaje puede ser favorito de mucho usuarios

    def to_dict(self):  #CONVIERTE EL OBJETO CLASE EN UN DICCIONARIO#
        return{
            "id": self.id,
            "name": self.name,
            "url": self.url
        }
        
class Favorite_People(db.Model): #Contiene los personajes favoritos seleccionados por los usuarios
    __tablename__= 'favorites_characters'
    id= db.Column(db.Integer, primary_key= True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    people_id= db.Column(db.Integer, db.ForeignKey('characters.id'))

    def to_dict(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }

class User(db.Model): #Contiene a los usuarios que se agregan al block
    __tablename__ = 'users'
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(120), nullable=False, unique=True)
    favorites_characters= db.relationship('Favorite_People', backref= 'user')
    favorites_planets= db.relationship('Favorite_Planet', backref= 'user')
    #A FUTURO SE AGREGARÁ EMAIL Y PASSWORD PARA IMPLEMENTAR JWT.

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }
   