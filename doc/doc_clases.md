### Tenemos 2 clases
***Clase*** [usuario.py](/src/usuario.py), definimos las características que tendrán: nuestros usuarios:
- Nombre. 
- Contraseña.
- Número de cigarrillos que fumaba.
- La marca de tabaco.
- Tipo,liar o industrial.

#### Métodos principales
- `get_nombre`: Devuelve el nombre del usuario.
  
- `get_progreso` : Devuelve el progreso del usuario, que se ha definido como el número de días que lleva sin fumar, y el tiempo en minutos y segudos.

- `get_password`: Devuelve la contraseña del usuario.

- `get_marca`: Devuelve la marca de tabaco del usuario.

- `get_numUsuarios` : Devuelve el número de usuarios.

- `get_tipo`: Devuelve el tipo de tabaco, liar o industrial.
  
- `get_listaUsuarios`: Devuelve la lista de usuarios.

- `crea_usu`: crea al usuario a partid de los datos del json, que son el nombre, password, el número de cigarrillos, el tipo de tabaco y el progreso.

- `to_s`: Para imprimir, los datos del usuario, que son Nombre, password, numero de cigarrillos y Progreso .

#### Estos datos los obtendremos de:
Archivo [datos.json](/json/datos.json)

***Clase*** [principal.py](/src/principal.py), definimos las características que tendrá nuestro sistema:
- El dinero que ha ahorrado nuestro usuario.
- El tipo de marca de tabaco.
- El número de cigarrillos que fumaba.
- El precio del tabaco.
- El progreso del usuario.
- El tipo de moneda que use el usuario.
  
#### Métodos principales

- `get_day`: Devuelve el número de días dque el usuario lleva sin fumar.
 
- `get_dinAho`: Devuelve el dinero ahorrado en euros.

- `get_marca`: Devuelve la marca del tabaco.
 
- `get_Ncigar`: Devuelve el numero de cigarrillos.
 
- `get_logs`: Devuelve los logs de los usuarios.

- `get_numUsuarios`: Devuelve el número de usuarios.

- `get_moneda`: Devuelve el tipo de moneda,euro,libra,etc.

- `set_moneda`: modifica el tipo de moneda.
  
- `to_s`: imprime la lista de usuarios.

- `crea_sitema`: crea el sistema con el nombre, tipo, capacidad, precio, y moneda el archivo json.
- 
#### Estos datos los obtendremos de:


  
Archivo [datos_tabaco.json](/json/datos_tabaco.json)



***Nuestra app*** [proyecto_app.py](/src/proyecto_app.py), hacemos uso del framework Hug y tendremos acceso a los datos a través de peticiones HTTP como pueden ser GET,PUT,POST, actualmente se han definido peticiones GET y POST.

Nuestro sistema cuenta con las siguientes rutas:

- / con el resultado:
~~~
{"status": "OK"}
~~~
- /status  con el resultado: 
~~~
{"status": "OK"}
~~~
- /lista usuarios con el resultado:
~~~
"[{'name': 'Usuario 1', 'password': 'asdfj2323as', 'progres': '1995-11-06T23:20:50', 'marca': 'MarcaA', 'tipo': 'Industrial', 'n_cigar': 22}, {'name': 'Usuario 2', 'password': '#@45asfull', 'progres': '2019-04-05T10:15:26', 'marca': 'MarcaE', 'tipo': 'Liar', 'n_cigar': 10}, {'Nombre': 'Usuario 1', 'Password': 'asdfj2323as', 'Num. cigarillos': 22, 'Marca': 'MarcaA', 'Progreso': [8759, 'días', '242.47', 'minutos y', 14548, 'seg.']}, {'Nombre': 'Usuario 2', 'Password': '#@45asfull', 'Num. cigarillos': 10, 'Marca': 'MarcaE', 'Progreso': [208, 'días', '1027.87', 'minutos y', 61672, 'seg.']}]"
~~~
- /datos_calculados con el resultado:
~~~
[{"name": "MarcaA", "tipo": "Industrial", "capacidad": 20, "precio": 4.5, "moneda": "€"}, {"name": "MarcaB", "tipo": "Industrial", "capacidad": 20, "precio": 4.8, "moneda": "€"}, {"name": "Marcac", "tipo": "Industrial", "capacidad": 20, "precio": 5.0, "moneda": "€"}, {"name": "MarcaD", "tipo": "Liar", "capacidad": 30, "precio": 3.5, "moneda": "€"}, {"name": "MarcaE", "tipo": "Liar", "capacidad": 30, "precio": 3.75, "moneda": "€"}, {"Nombre": "Usuario 1", "Progreso": [8759, "días", "242.47", "minutos y", 14548, "seg."], "Dinero Ahorrado": "43357.05€"}, {"Nombre": "Usuario 2", "Progreso": [208, "días", "1027.87", "minutos y", 61672, "seg."], "Dinero Ahorrado": "260.0€"}]
~~~

- /moneda con el resultado:
~~~
"{'Euro', '€'}"
~~~
- /version con el resultado:
~~~
"{'Sistema': 'versión 0.5'}"
~~~
