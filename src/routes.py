from flask import Blueprint, request, jsonify
api = Blueprint('api', __name__)

from models import db, Favorite_Planet, Favorite_People, People, Planet, User 

#OPERACIONES DE CHARACTERS

@api.route('/people', methods=['GET']) #Lista todos los personajes.
def get_characters():
    characters= People.query.all()
    characters= list(map(lambda people: people.to_dict(), characters))
    return jsonify(characters), 200

@api.route('/people/<int:people_id>', methods=['GET']) #Muestra un solo personaje en un objeto.
def get_people(people_id):
    people= People.query.filter_by(id= people_id).first()
    result= people.to_dict()
    return jsonify(result), 200


@api.route('/people', methods=['POST']) #Crea un personaje.
def add_characters():
    #Accede por cada campo de la clase People.
    name = request.json.get('name')
    url = request.json.get('url')
    #Muestra los datos recibe por el POST.
    print(name)
    print(url)

    #A continuaciónd preparación del Insert
    people= People()
    people.name= name
    people.url= url

    #A continuación ejecuta el query (el insert de agregar un personaje a la base de datos).
    db.session.add(people)
    #Guarda los cambios en la tabla de la base de datos. 
    db.session.commit()

    return jsonify(people.to_dict()), 201

@api.route('/favorite/people/<int:people_id>', methods=['POST']) #Agrega un personaje a un usuario del blog.
def add_favorite_people(people_id):
    datos= request.get_json()
    print(datos['people_id'])
    print(datos['users_id'])

    #A continuación preparación del Insert
    user_id= 1
    favorites_people= Favorite_People()  
    favorites_people.people_id= people_id
    favorites_people.users_id= user_id

    #Agrega el personaje favorito agregado por el usuario.
    db.session.add(favorites_people)
    #Guarda el personaje favorito por los ids asociados.
    db.session.commit()
    return jsonify(favorites_people.to_dict()), 200

@api.route('/favorite/people/<int:people_id>', methods= ['DELETE']) #Elimina un personaje de la tabla favorites_characters del usuario.
def delete_favorite_people(people_id):
    user_id= 1                              
    favorite_people= Favorite_People.query.filter_by(people_id= people_id, users_id= user_id).first()
    
    if not favorite_people:
        return jsonify({"messagge": "Favorite people doesn't exist!"}), 404
    
    db.session.delete(favorite_people)
    db.session.commit()

    return jsonify({"messagge": "Favorite People was deleted!"}), 200

#OPERACIONES DE PLANETAS

@api.route('/planets', methods=['GET']) #lista todos los planetas.
def get_planets():
    planets= Planet.query.all()
    planets= list(map(lambda planet: planet.to_dict(), planets))
    return jsonify(planets), 200

@api.route('/planets/<int:planet_id>', methods=['GET']) #Muestra un solo planeta.
def get_planet(planet_id):
    planet= Planet.query.filter_by(id= planet_id).first()
    result= planet.to_dict()
    return jsonify(result), 200

@api.route('/planet', methods=['POST']) #Crea un planeta.
def add_planets():
    #Accede globalmente a los campos asociados a la clase Planet.
    datos = request.get_json()
    #Estos print muestran los datos recibidos por el POST.
    print(datos['name'])
    print(datos['url'])
    
    #A continuación preparación del Insert.
    planet= Planet()
    planet.name= datos['name']
    planet.url= datos['url']

    #A continuación ejecuta el query (el insert de agregar un planeta a la base de datos).
    db.session.add(planet)
    #Guarda los cambios en la tabla de la base de datos
    db.session.commit()

    return jsonify(planet.to_dict()), 201

@api.route('/favorite/planet/<int:planet_id>', methods=['POST']) #Agrega un planeta a un usaurio del blog.
def add_favorite_planet(planet_id):
    datos= request.get_json()
    print(datos['planets_id'])
    print(datos['users_id'])

    #A contnuación preparación del insert.
    user_id= 1
    favorites_planets= Favorite_Planet()  
    favorites_planets.planets_id= planet_id
    favorites_planets.users_id= user_id

    #Ejecuta el query y guarda el planeta en el usuario actual.
    db.session.add(favorites_planets) 
    db.session.commit()
    return jsonify(favorites_planets.to_dict()), 200
                                                             
                                                             
@api.route('/favorite/planet/<int:planet_id>', methods= ['DELETE']) #Elimina un planeta favorito de la tabla favorites_planets del usuario.
def delete_favorite_planet(planet_id):                              
    user_id= 1
    favorite_planet= Favorite_Planet.query.filter_by(planets_id= planet_id, users_id= user_id).first()

    if not favorite_planet:
        return jsonify({"messagge": "Favorite planet doesn't exist!"}), 404
    
    db.session.delete(favorite_planet)
    db.session.commit()

    return jsonify({"messagge": "Planet was deleted!"}), 200



#OPERACIONES DE USUARIO

@api.route('/users', methods=['GET'])
def get_users():
    users= User.query.all() #Consulta a todos los usuarios del blog en la base de datos.
    users= list(map(lambda user: user.to_dict(), users)) #Lista todo los usuarios.
    return jsonify(users), 200

@api.route('/users/<username>/favorites', methods=['GET'])
def get_favorites_users(username):
    user= User.query.filter_by(username= username).first()
    result= user.to_dict()
    return jsonify(result), 200

@api.route('/user/favorites', methods=['GET'])#Lista todos los favoritos que pertenecen al usuario actual.
def user_favorites():
    user_id= 1
    favorites_characters= Favorite_People.query.filter_by(people_id= user_id)#Filtra por el campo people_id de la clase.
    favorites_planets= Favorite_Planet.query.filter_by(planets_id= user_id)#Filtra por el campo planets_id de la clase.

    results_characters= list(map(lambda people: people.to_dict(), favorites_characters))#Accede el array del campo favorites_characters.
    results_planets= list(map(lambda planet: planet.to_dict(), favorites_planets))#Accede el array del campo favorites_planets.

    datos= {
        "favorites_characters": results_characters,
        "favorites_planets": results_planets
    }

    return jsonify(datos), 200
