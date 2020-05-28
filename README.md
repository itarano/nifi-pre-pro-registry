# nifi-pre-pro-registry

![Index Management](/assets/arquitecture.png)

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
- Script *start.bat* para desplegar el entorno en windows.
- Script [*start.py*](https://gist.github.com/itarano/bcfbc671072635acdce6e4fa444d65af) para desplegar entorno (linux+python3). Se hace uso de un [CLI general](https://gist.github.com/itarano/bcfbc671072635acdce6e4fa444d65af) para docker compose en el que se puede implementar lógica antes de iniciar los contenedores. Por ejemplo, si la variable *REGISTRY_DB_URL* que hace referencia a la base de datos para guardar las transacciones de nifi-registry no es postgresql, no se inicia dicho servicio.
- El directorio *volumes/nifi-registry* que comparte con el contenedor *registry* los drivers de PostgreSQL (necesarios en caso de configurar postgres en vez de h2 en el fichero *.env*).
- El directorio donde se clona el repositorio en el que se almacenan las versiones de los flujos (en caso de elegir *git* en vez de *file* en el fichero *.env*). Dicho directorio está incluido en *.gitignore* y se creará de forma local clonando el repositorio donde queramos almacenar los flujos.

## Deployment
- Linux o Windows ([WSL 2](https://devblogs.microsoft.com/commandline/announcing-wsl-2/)) &rarr; [**start.py**](https://gist.github.com/itarano/bcfbc671072635acdce6e4fa444d65af)
