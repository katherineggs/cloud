# Dockerización de una app python
!!! Tuve un problema con mi docker local y no lo pude probar. Me hicieron el favor de probar en otra compu con la imagen que subí a mi DockerHub y no se podía porque venía de una arquitectura ARM. Entonces, subí mi trabajo en otro repositorio desde la computadora de un compañero. este es el comando 2. 
---------
## En docker hub
- [Link a mi repositorio de Docker](https://hub.docker.com/r/katherinegg/crazyapp)

### Para obtener la imagen - correr el comando 

``` docker pull katherinegg/crazyapp ```
``` docker pull fabricio2000gjuarez/katherinecrazyapp:latest ```

### Para correr la app 

``` docker run -p 8080:8080 katherinegg/crazyapp```
``` docker run -p 8080:8080 fabricio2000gjuarez/katherinecrazyapp```
- -p es para especificar el puerto direccion del puerto -> mi máquina : del contenedor 
- -d -> es para que el container corra en el background "detached"
- -it -> "ejecutalo de manera interactiva"

### Observar la app
En el navegador ir a localhost:8080 
*o el puerto colocado en el comando anterior