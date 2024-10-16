# Kingdom Conquest

Kingdom Conquest es un juego de estrategia donde los jugadores pueden gestionar recursos, construir infraestructuras y expandir sus territorios. Este proyecto está dividido en varias partes, incluyendo el cliente, el servidor y las pruebas.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `.github/`: Contiene configuraciones y plantillas para GitHub.
  - `ISSUE_TEMPLATE/`: Plantillas para la creación de issues.
    - `historia-de-usuario.md`: Template para crear historias de usuario.
  - `workflows/`: Configuraciones para GitHub Actions.
    - `ci.yml`: Configuración del pipeline de integración continua.

- `Kingdom_Conquest/`: Directorio principal del proyecto.
  - `client/`: Contiene el código y configuraciones del cliente.
    - `Dockerfile`: Archivo de configuración para Docker.
    - `README.md`: Documentación del cliente.
    - `requirements.txt`: Dependencias del cliente.
    - `src/`: Código fuente del cliente.
      - `console_ui.py`: Interfaz de consola del cliente.
      - `game_client.py`: Lógica del cliente del juego.
    - `tests/`: Pruebas unitarias del cliente.
  - `docker-compose.yml`: Archivo de configuración para Docker Compose.
  - `features/`: Contiene las pruebas de comportamiento.
    - `enviroment.py`: Configuración del entorno de pruebas.
    - `gestion_recursos.feature`: Pruebas de gestión de recursos.
    - `gestion_reinos.feature`: Pruebas de gestión de reinos.
    - `steps/`: Implementaciones de los pasos de las pruebas.
      - `gestion_recursos_steps.py`: Pasos para las pruebas de gestión de recursos.
      - `gestion_reinos_steps.py`: Pasos para las pruebas de gestión de reinos.
  - `prometheus.yml`: Configuración de Prometheus.
  - `server/`: Contiene el código y configuraciones del servidor.
    - `Dockerfile`: Archivo de configuración para Docker.
    - `README.md`: Documentación del servidor.
    - `requirements.txt`: Dependencias del servidor.
    - `src/`: Código fuente del servidor.
      - `__init__.py`: Inicialización del módulo.
      - `main.py`: Punto de entrada del servidor.
      - `utils.py`: Funciones utilitarias.
    - `tests/`: Pruebas unitarias del servidor.

## Contenerización

El proyecto utiliza Docker y Docker Compose para la contenerización. Los servicios definidos en `docker-compose.yml` incluyen:

- **db**: Servicio de base de datos PostgreSQL.
- **api**: Servicio de la API del servidor.
- **prometheus**: Servicio de monitoreo con Prometheus.
- **grafana**: Servicio de visualización con Grafana.

## Endpoints

El servidor expone los siguientes endpoints definidos en `routes.py`:

- `POST /reinos/`: Crea un nuevo reino. Recibe datos del reino y retorna la información del reino creado.
- `GET /reinos/`: Lista todos los reinos. Retorna una lista de reinos disponibles.
- `PUT /reinos/{reino_id}`: Actualiza un reino existente. Recibe datos del reino y actualiza el reino especificado por el ID.
- `DELETE /reinos/{reino_id}`: Elimina un reino existente. Elimina el reino especificado por el ID.
- `POST /reinos/{reino_id}/accion`: Realiza una acción en un reino específico. Recibe la acción y los parámetros, y actualiza el reino en consecuencia.
- `POST /reset`: Reinicia el juego. Elimina todos los datos de reinos, infraestructuras y eventos.

## Colaboradores

- Arbués Pérez V
- Ivan Urbano N