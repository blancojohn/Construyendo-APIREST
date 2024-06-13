from flask import Blueprint, request, jsonify
api = Blueprint('api', __name__)

from models import db, favorite_planet, favorite_people, People, Planet, User 

#OPERACIONES DE CHARACTERS

@api.route('/people', methods=['GET']) #Lista todos los personajes
def get_characters():
    characters= People.query.all()
    characters= list(map(lambda characters: characters.to_dict(), characters))
    return jsonify(characters), 200

@api.route('/people/<int:people_id>', methods=['GET']) #Muestra un solo personaje en un objeto
def get_people(people_id):
    people= People.query.filter_by(id= people_id).first()
    result= people.to_dict()
    return jsonify(result), 200


@api.route('/people', methods=['POST']) #Crea un personaje
def add_characters():
    datos = request.get_json()
    print(datos['name'])
    print(datos['url'])
    
    name = request.json.get('name')
    url = request.json.get('url')
    print(name)
    print(url)

    #A continuaciónd preparación del Insert
    people= People()
    people.name= name
    people.url= url

    #A continuación ejecuta el query (el insert de agregar un personaje a la base de datos)
    db.session.add(people)
    #Guarda los cambios en la tabla de la base de datos 
    db.session.commit()

    return jsonify(people.to_dict()), 201

@api.route('/favorite/people/<int:people_id>', methods=['POST']) #Agrega un personaje a un usuario del blog
def add_favorite_people(people_id):
    
    #A continuación preparación del Insert
    user_id= 1
    favorites_people= favorite_people()  
    favorites_people.user_id= user_id
    favorites_people.people_id= people_id

    #Agrega el personaje favorito agregado por el usuario
    db.session.add(favorites_people)
    #Guarda el personaje favorito por los ids asociados 
    db.session.commit()
    return jsonify(favorites_people.to_dict()), 200

@api.route('/favorite/people/<int:people_id>', methods= ['DELETE']) #Elimina un personaje de la tabla favorites_characters.
def delete_favorite_people(people_id, user_id):                              #No confundir con el campo people_id,
    people= People.query.get(people_id)
    user= User.query.get(user_id)
    

    if not people:
        return jsonify({"messagge": "Favorite people doesn't exist!"}), 404
    
    db.session.delete(people, user)
    db.session.commit()

    return jsonify({"messagge": "Favorite People was deleted!"}), 200

#OPERACIONES DE PLANETAS

@api.route('/planets', methods=['GET']) #lista todos los planetas
def get_planets():
    planets= Planet.query.all()
    planets= list(map(lambda planets: planets.to_dict(), planets))
    return jsonify(planets), 200

@api.route('/planets/<int:planet_id>', methods=['GET']) #Muestra un solo planeta
def get_planet(planet_id):
    planet= Planet.query.filter_by(id= planet_id).first()
    result= planet.to_dict()
    return jsonify(result), 200

@api.route('/planet', methods=['POST']) #Crea un planeta
def add_planets():
    datos = request.get_json()
    print(datos['name'])
    print(datos['url'])
    
    name = request.json.get('name')
    url = request.json.get('url')
    print(name)
    print(url)

    #A continuación preparación del Insert
    planet= Planet()
    planet.name= name
    planet.url= url

    #A continuación ejecuta el query (el insert de agregar un planeta a la base de datos)
    db.session.add(planet)
    #Guarda los cambios en la tabla de la base de datos
    db.session.commit()

    return jsonify(planet.to_dict()), 201

@api.route('/favorite/planet/<int:planet_id>', methods=['POST']) #Agrega un planeta a un usaurio del blog
def add_favorite_planet(planet_id):
    
    #A contnuación preparación del insert
    user_id= 1
    favorites_planets= favorite_planet()  
    favorites_planets.user_id= user_id
    favorites_planets.planet_id= planet_id

    db.session.add(favorites_planets) 
    db.session.commit()
    return jsonify(favorites_planets.to_dict()), 200
                                                             
                                                             #Elimina un planeta de la tabla favorites_planets.
@api.route('/favorite/planet/<int:planet_id>', methods= ['DELETE']) #No confundir con el campo planet_id,
def delete_favorite_planet(planet_id):                              #se pasa es el campo id de la tabla favorites_planets.

    planet= favorite_planet.query.get(planet_id)

    if not planet:
        return jsonify({"messagge": "Favorite planet doesn't exist!"}), 404
    
    db.session.delete(planet)
    db.session.commit()

    return jsonify({"messagge": "Planet was deleted!"}), 200



#OPERACIONES DE USUARIO

@api.route('/users', methods=['GET'])
def get_users():
    users= User.query.all() #Consulta a todos los usuarios del blog en la base de datos.
    users= list(map(lambda users: users.to_dict(), users)) #Lista todo los usuarios.
    return jsonify(users), 200

@api.route('/users/<username>/favorites', methods=['GET'])
def get_favorites_users(username):
    user= User.query.filter_by(username= username).first()
    result= user.to_dict()
    return jsonify(result), 200

@api.route('/user/favorites', methods=['GET'])
def user_favorites():
    user_id= 1
    favorites_planets= favorite_planet.query.filter_by(user_id= user_id)
    favorites_characters= favorite_people.query.filter_by(user_id= user_id)
    results_planets= favorites_planets.to_dict()
    results_characters= favorites_characters.to_dict()

    return jsonify(results_planets, results_characters), 200
