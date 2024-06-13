from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

favorite_planet= db.Table(
    'favorites_planets',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable= False, primary_key= True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'), nullable= False, primary_key= True)
)

favorite_people= db.Table( #Contiene los personajes favoritos seleccionados por los usuarios
    'favorites_characters',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable= False, primary_key= True),
    db.Column('people_id', db.Integer, db.ForeignKey('characters.id'), nullable= False, primary_key= True)
)


class Planet(db.Model): #Contiene los planetas de StarWars.
    __tablename__= 'planets'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable= False)
    url= db.Column(db.String(300), nullable= False)
    favorites= db.relationship('Favorite_Planet', secondary= 'favorites_planets', backref= 'planet')

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "favorites": list(map(lambda favorite: favorite.id, self.favorites))
        }

class People(db.Model): #Contiene los personajes de StarWars.
    __tablename__= 'characters'
    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(200), nullable= False)
    url= db.Column(db.String(300), nullable= False)
    favorites= db.relationship('Favorite_People', secondary='favorites_characters', backref='people')#Un personaje puede ser favorito de mucho usuarios

    def to_dict(self):  #CONVIERTE EL OBJETO CLASE EN UN DICCIONARIO#
        return{
            "id": self.id,
            "name": self.name,
            "url": self.url
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
   
   

