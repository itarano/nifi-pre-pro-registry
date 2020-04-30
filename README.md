# nifi-test-pro-registry

**Completar**

## Software
1. Docker and Docker Compose
2. Git local host client

## Estructura del proyecto
1. Fichero .env donde se recogen variables que después lee el fichero docker-compose.
2. Fichero docker-compose.yml para desplegar el entorno.
3. El directorio *volumes/nifi-refistry* que comparte con el contenedor *registry* los drivers de PostgreSQL (en caso de configurar postgres en vez de h2 en el fichero .env), y el directorio donde se clona el repositorio en el que se almacenan las versiones de los flujos (en caso de elegir git en vez de file en el fichero .env).