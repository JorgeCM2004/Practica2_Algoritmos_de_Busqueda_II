# Jorge Camacho Mejías - Práctica 2 - Python

## Tutorial Configuración del Entorno

Si no tienes el entorno creado para poder ejecutar el proyecto en python, sigue el tutorial leyendo el archivo "README.md" en el siguiente enlace: <https://github.com/JorgeCM2004/Practica1_Algoritmos_de_Busqueda_II>

## Archivos a Ejecutar

En este apartado, te explicaré que archivos puedes ejecutar y cual es su funcionamiento.
Aunque el código está realizado para que se pueda ejecutar desde cualquier parte, se recomienda encarecidamente que se ejecute desde el directorio raiz o desde las subcarpetas donde se encuentran los archivos ejecutables.

❗La primera ejecución es más lenta al no haber incluido los archivos "\_\_pycache__" en el repositorio.❗

### F_P2_Main

El archivo main es el más sencillo de todos pero, a la vez, con el que el usuario más puede interactuar.
El archivo main usa la clase "Runner" (Experiment), esta es la que se encarga de lanzar los algoritmos por lo que si alguien quiere cambiar los parametros (alpha, cross_probability, ...) debe configurarlo desde esta clase. Main es un archivo para el usuario común que solo quiere lanzar el programa sin preocupaciones. Por ello desde main solo se pueden configurar:

- Tipo de algoritmo a utilizar: Puede usar "Algorithm_1" o "Algorithm_2".
- Tiempo por instancia: Utilizar tiempos muy pequeños por instancia puede dar a que este se pase del tiempo maximo (unidades -> segundos).
- Guardar ejecución.

### F_P2_Test_Runner

Este archivo se encuentra en la carpeta de tests y se debe ejecutar con el siguiente comando:

```bash
pytest .\\F_P2_Test_Runner.py
```

Si quieres añadir más tests debes incluirlos en "F_P2_Tests.py" con el nombre de la instancia y el valor mínimo que se espera, además de incluir la instancia en la carpeta de instancias.
