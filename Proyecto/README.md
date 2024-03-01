# BAR API - JUAN MANUEL HERRERA QUINTERO 2024

<p align="justify"><i>
Este proyecto no se puede utilizar con fines comerciales. No se permite la modificación de la obra ni la creación de obras derivadas sin el permiso expreso del autor. Ya que este proyecto será la base de futuras mejoras para intereses del autor.</i>
</p>

## Definición del proyecto:

<p align="justify">
Microproyecto para el manejo básico de catalogo de productos de un pequeño bar. Fue construido con el gestor de manejo de bases de datos SQLite y el framework para desarrollo Backend FastAPI de Python.
</p>
<p align="justify">
Se eligió el framework FastAPI de Python para el desarrollo de este proyecto con el objetivo de fortalecer y afianzar los conocimientos adquiridos a lo largo de las sesiones de los "TALLERES DE FORMACIÓN TÉCNICA INDUSTRIA TI 4.0 ". En conjunto al propio FastAPI se hizo uso de otras herramientas o librerías para Python que colaboran en la ejecución del servidor para la BAR API, en el archivo "requirements.txt" se encuentran todas las librerías y herramientas que deben ser instaladas para el perfecto funcionamiento de BAR API. Para más información sobre librerías en Python y cómo instalarlas ingrese en este enlace web [aquí](https://programminghistorian.org/es/lecciones/instalar-modulos-python-pip).
</p>

<p align="justify">
Esta aplicación esta construida siguiendo estándares de arquitectura por módulos para aplicaciones web, buscando separar las funciones que cada uno de estos cumple, por ejemplo, separar el CRUD, las utilidades, modelos y entre otros.
</p>

## Puesta en marcha de la aplicación:

<p align="justify">
En esta sección se mostrará paso a paso cómo ejecutar la aplicación para su correcto funcionamiento. Primero se debe tener instalado lo básico, siendo esto Python. También se deben instalar todas las librerías que están descritas en el archivo "requirements.txt". Para instalar más eficientemente las librerías ejecute el comando "pip install -r requirements.txt". Una vez instaladas las librerias, asegúrese de dirigirse por la terminal hasta la dirección donde reposa el código fuente de la API. Posteriormente, ejecute el comando "uvicorn main:app --host localhost --port 5000" para activar los servicios de la API. Las opciones "--host" y "--port" pueden utilizarse para modificar el puerto y el host en el despliegue de la aplicación.
</p>

<p align="justify">
Una vez se cumplan los pasos antes descritos correctamente, usted tendrá los servicios de la aplicación activos en la siguiente URL "http://localhost:5000".
</p>

<p align="justify">
Si tiene problemas para poner en funcionamiento la aplicación o cualquier otra inquietud, envíelas al siguiente correo: j.herrera5@utp.edu.co.
</p>
