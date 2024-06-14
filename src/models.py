from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class People(db.Model): #Contiene los personajes de StarWars.
    __tablename__= 'characters'
    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(200), nullable= False)
    url= db.Column(db.String(300), nullable= False)
    favorites_users= db.relationship('Favorite_People', backref='people')#El backref permite saber cuale planetas fueron seleccionados como favoritos por un usuario.

    def to_dict(self):  #CONVIERTE EL OBJETO CLASE EN UN DICCIONARIO#
        return{
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "favorites_users": list(map(lambda user: user.id, self.favorites_users))#crea lista con los id de los usuarios que agregaron personajes favoritos.
        }
    
class Favorite_People(db.Model):
    __tablename__= 'favorites_characters'
    id= db.Column(db.Integer, primary_key= True)
    people_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    users_id= db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "people_id": self.people_id,
            "users_id": self.users_id
        }
    
class Planet(db.Model): #Contiene los planetas de StarWars.
    __tablename__= 'planets'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable= False)
    url= db.Column(db.String(300), nullable= False)
    favorites_users= db.relationship('Favorite_Planet', backref= 'planet')#El backref permite saber cuale planetas fueron seleccionados como favoritos por un usuario.
                                                                                         
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "favorites_users": list(map(lambda user: user.id, self.favorites_users))#crea lista con los id de los usuarios que agregaron planetas favoritos.
        }
    
class Favorite_Planet(db.Model):
    __tablename__= 'favorites_planets'
    id= db.Column(db.Integer, primary_key= True)
    planets_id= db.Column(db.Integer, db.ForeignKey('planets.id'))
    users_id= db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "planets_id": self.planets_id,
            "users_id": self.users_id
        }

class User(db.Model): #Contiene los usuarios agragdos al block
    __tablename__ = 'users'
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(120), nullable=False, unique=True)
    favorites_characters= db.relationship('Favorite_People', backref= 'user')#Devuelve una lista de los personajes agregados.
    favorites_planets= db.relationship('Favorite_Planet', backref= 'user')#Devuelve una lista de los planetas agregados.
    #A FUTURO SE AGREGARÁ EMAIL Y PASSWORD PARA IMPLEMENTAR JWT.

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }
   
   






        
