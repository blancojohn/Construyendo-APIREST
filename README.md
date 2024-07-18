# Blog de Star Wars (Solo backend).

### Consiste en una API conectada a una base de datos, ambas creadas por mí, e implemente los siguientes endpoints:
<ul>
  <li>[GET] /people .Listar todos los registros de people en la base de datos.</li>
  <li>[GET] /people/<int:people_id> .Muestra la información de un solo personaje según su id.</li>
  <li>[GET] /planets Listar todos los .registros de planets en la base de datos.</li>
  <li>[GET] /planets/<int:planet_id> .Muestra la información de un solo planeta según su id.</li>
  <li>[GET] /users .Listar todos los usuarios del blog.</li>
  <li>[GET] /users/favorites .Listar todos los favoritos que pertenecen al usuario actual.</li>
  <li>[POST] /favorite/planet/<int:planet_id> .Añade un nuevo planet favorito al usuario actual con el id = planet_id.</li>
  <li>[POST] /favorite/people/<int:people_id> .Añade un nuevo people favorito al usuario actual con el id = people_id.</li>
  <li>[DELETE] /favorite/planet/<int:planet_id> .Elimina un planet favorito con el id = planet_id.</li>
  <li>[DELETE] /favorite/people/<int:people_id> .Elimina un people favorito con el id = people_id.</li>
</ul>
Para acceder a un usuario de la base de datos debe ser hard-code.
