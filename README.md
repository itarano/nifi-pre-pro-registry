# nifi-pre-pro-registry

![Index Management](/assets/arquitecture.png)

## Requisitos
- Docker Compose
- En caso de querer utilizar git como repositorio para versionar los flujos:
    1. Git CLI
    2. Git version Control (Github, Gitlab...)

## Docker Environment Software
- Apache NiFi &rarr; latest
- Apache Zookeeper &rarr; latest
- PostgreSQL &rarr; latest
- Apache NiFi Registry &rarr; latest
- pgAdmin &rarr; latest

## Estructura del proyecto
- Fichero *.env* donde se recogen variables utilizadas en el fichero *docker-compose.yml*.
- Fichero *docker-compose.yml* para definir el entorno.
- Script [*start.py*](https://github.com/itarano/nifi-pre-pro-registry/blob/master/start.py) para desplegar entorno (linux or windows wsl2). Se hace uso de un [CLI general](https://gist.github.com/itarano/bcfbc671072635acdce6e4fa444d65af) para docker compose en el que se puede implementar lógica antes de iniciar los contenedores. Por ejemplo, si la variable *REGISTRY_DB_URL* que hace referencia a la base de datos para guardar las transacciones de nifi-registry no es postgresql, no se inicia dicho servicio.
- El directorio *volumes/nifi-registry* que comparte con el contenedor *registry* los drivers de PostgreSQL (necesarios en caso de configurar postgres en vez de h2 en el fichero *.env*).
- El directorio donde se clona el repositorio en el que se almacenan las versiones de los flujos (en caso de elegir *git* en vez de *file* en el fichero *.env*). Dicho directorio está incluido en *.gitignore* y se creará de forma local clonando el repositorio donde queramos almacenar los flujos.

## Deployment
- Linux o Windows ([WSL 2](https://devblogs.microsoft.com/commandline/announcing-wsl-2/)) &rarr; [**start.py**](https://github.com/itarano/nifi-pre-pro-registry/blob/master/start.py)

```console
USER@HOSTNAME:~/projects/nifi-pre-pro-registry$ ./start.py -h
usage: start.py [-h] [-s services [services ...]] environment

Services: ['pgadmin', 'nifi-pro', 'nifi-pre', 'postgresql', 'zookeeper-pre', 'zookeeper-pro', 'registry']

positional arguments:
  environment           section environment to use

optional arguments:
  -h, --help            show this help message and exit
  -s services [services ...]
                        services (i.e. service1 service2 ...)
```