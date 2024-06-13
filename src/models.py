from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

#Tabla asociativa
favorite_planet= db.Table(
    'favorites_planets',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable= False, primary_key= True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'), nullable= False, primary_key= True)
)

#Tabla asociativa
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
    favorites= db.relationship('User', secondary= 'favorites_planets', backref= 'planet')#El backref permite saber cuale planetas fueron seleccionados como favoritos por un usuario.
                                                                                         
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "favorites": list(map(lambda favorite: favorite.id, self.favorites))#crea lista con los id de los usuarios que agregaron planetas favoritos.
        }

class People(db.Model): #Contiene los personajes de StarWars.
    __tablename__= 'characters'
    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(200), nullable= False)
    url= db.Column(db.String(300), nullable= False)
    favorites= db.relationship('User', secondary='favorites_characters', backref='people')#El backref permite saber cuale planetas fueron seleccionados como favoritos por un usuario.

    def to_dict(self):  #CONVIERTE EL OBJETO CLASE EN UN DICCIONARIO#
        return{
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "favorites": list(map(lambda favorite: favorite.id, self.favorites))#crea lista con los id de los usuarios que agregaron personajes favoritos.
        }
        


class User(db.Model): #Contiene los usuarios agragdos al block
    __tablename__ = 'users'
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(120), nullable=False, unique=True)
    favorites_characters= db.relationship('People', secondary= 'favorites_characters', backref= 'user')#Devuelve una lista de los personajes agregados.
    favorites_planets= db.relationship('Planet', secondary= 'favorites_planets', backref= 'user')#Devuelve una lista de los planetas agregados.
    #A FUTURO SE AGREGARÁ EMAIL Y PASSWORD PARA IMPLEMENTAR JWT.

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }
   
   

