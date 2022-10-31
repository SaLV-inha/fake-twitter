# fake-twitter
Conociendo FastAPI y desarrollo con Python

Practica proyecto fake_twitter

CRUD en Users y tweets, aun sin base de datos, pero con el uso de archivos .json donde guardo estos datos.

Al correr la app con uvicorn main:app --reload.

Este comando te dira donde esta corriendo este server como Uvicorn running on http://127.0.0.1:....

Vas a esta dirección en el navegador, pero el navegador solo te responderá con un json asi que para ver la utilidades de la aplicación debes ingresar al interface de Swagger UI. Este te permitirá interactuar una interface mas intuitiva y amigable donde podrás ver el uso de la app, para ingresar a esta interface, debes agregarle 

El path **docs** a tu link y te quedara así:

- http://127.0.0.1:..../ **docs**
