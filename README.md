# nifi-pre-pro-registry

## Requisitos
- Docker and Docker Compose
- En caso de querer utilizar git como repositorio para versionar los flujos:
    1. Cliente local git
    2. Cuenta en GitHub

## Docker Environment Software
- Apache NiFi &rarr; latest
- Apache Zookeeper &rarr; latest
- PostgreSQL &rarr; latest
- Apache NiFi Registry &rarr; latest
- pgAdmin &rarr; latest

## Estructura del proyecto
- Fichero *.env* donde se recogen variables utilizadas en el fichero *docker-compose.yml*.
- Fichero *docker-compose.yml* para definir el entorno.
- Script *start.bat* para desplegar el entorno.
- El directorio *volumes/nifi-registry* que comparte con el contenedor *registry* los drivers de PostgreSQL (necesarios en caso de configurar postgres en vez de h2 en el fichero *.env*).
- El directorio donde se clona el repositorio en el que se almacenan las versiones de los flujos (en caso de elegir *git* en vez de *file* en el fichero *.env*). Dicho directorio está incluido en *.gitignore* y se creará de forma local (manual) clonando el repositorio donde queramos almacenar los flujos.