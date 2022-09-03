# Dockerizacio4n de una app python

---------
## En docker hub
- [Link a mi repositorio de Docker](https://hub.docker.com/r/katherinegg/crazyapp)

### Para obtener la imagen - correr el comando 

``` docker pull katherinegg/crazyapp ```

### Para correr la app 

``` docker run -p 8080:8080 ```
- -p es para especificar el puerto direccion del puerto -> mi máquina : del contenedor 
- -d -> es para que el container corra en el background "detached"
- -it -> "ejecutalo de manera interactiva"

### Observar la app
En el navegador ir a localhost:8080 
*o el puerto colocadoen el comando anterior