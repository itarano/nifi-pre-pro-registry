# nifi-test-pro-registry

**Completar**

## Local Software
- Docker and Docker Compose
- Git local host client (en caso de querer utilizar git como repositorio para versionar los flujos)

## Docker Environment Software
- Apache NiFi &rarr; 1.11.4
- Apache Zookeeper &rarr; latest
- PostgreSQL &rarr; latest
- Apache NiFi Registry &rarr; latest
- pgadmin &rarr; latest

## Estructura del proyecto
- Fichero .env donde se recogen variables que después lee el fichero docker-compose.
- Fichero docker-compose.yml para desplegar el entorno.
- El directorio *volumes/nifi-registry* que comparte con el contenedor *registry* los drivers de PostgreSQL (necesarios en caso de configurar postgres en vez de h2 en el fichero .env)
- El directorio donde se clona el repositorio en el que se almacenan las versiones de los flujos (en caso de elegir *git* en vez de *file* en el fichero .env). Dicho directorio está incluido en *.gitignore* y se creará de forma local clonando el repositorio donde queramos almacenar los flujos.