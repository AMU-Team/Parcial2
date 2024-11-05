# Guía para jugar en consola 
### 1. Crear la Imagen de Cliente:
Desde el directorio Parcial2/Kingdom_Conquest/client, crea la imagen de Docker para el cliente:

``` bash
docker build -t kingdom_conquest_client .
```
### 2. Ejecutar el Contenedor de la Partida
En cualquier terminal, ejecuta el siguiente comando para iniciar un contenedor (la partida) basado en la imagen creada y entrar al juego:

``` bash
docker run --rm -it --network kingdom_conquest_default kingdom_conquest_client
```
### 3. Interactuar con la Consola
La consola nos permite crear reinos y realizar las acciones de los reinos por turnos (excepto construir_infraestructura). Actualmente, todas las acciones están implementadas, excepto construir_infraestructura.

#### Nota: Se puede observar los cambios de estado en la base de datos realizando las respectivas consultas.

#### Verificar el Estado en la Base de Datos
Encuentra el ID del contenedor con:

``` bash
docker ps
```

Accede al contenedor usando:
``` bash
docker exec -it <container_id> /bin/bash
``` 
Ingresa al cliente de PostgreSQL:

``` bash
psql -U kingdom_user -d kingdom_db
``` 
Realiza consultas para verificar los datos:

``` sql
select * from reinos;
select * from infraestructuras;
select * from eventos;
```
# Probar Kingdom Conquest
Probar los Endpoints con FastAPI
Para realizar pruebas adicionales y aprovechar funcionalidades aún no implementadas en la consola, utiliza la interfaz de FastAPI.

### Endpoints sin Parámetros
Puedes probar Listar o Reset (que no requieren parámetros) en la interfaz de FastAPI. Selecciona Try it out y luego Execute para ejecutar.

### Endpoints con Parámetros
Algunos endpoints requieren parámetros específicos:
1. Borrar Reino: Necesita el ID del reino.
2. Actualizar Reino: Necesita el ID del reino y el nuevo nombre como una cadena (String).
3. Para realizar una Acción, por ejemplo, Construir Infraestructura  utiliza el endpoint de Realizar Acción Reino con el ID del reino y un cuerpo JSON con los detalles de la infraestructura. Copia y pega el siguiente JSON de ejemplo:

``` json
{
  "accion": "construir_infraestructura",
  "params": {
    "nombre": "Granero",
    "costo_oro": 20,
    "costo_madera": 30,
    "aumento_produccion": 10,
    "aumento_estabilidad": 5
  }
}
```
Esto permitirá construir una infraestructura con los parámetros especificados en el reino correspondiente.
