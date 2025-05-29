# Tarea_09-filtro_comic
Este es un programa que lo que hace es cambiar el filtro de una imagen a un tipo de filtro llamado "comic"

**Lenguaje de programación:**
- Python

**Libreria que se utulizó:**
- openCv

Este código en Python le pone un filtro tipo cómic a una imagen usando OpenCV. Lo primero que hace es cargar una imagen que debe estar en la misma carpeta que el archivo del programa, y revisa que se haya cargado bien. Después convierte la imagen a blanco y negro y le aplica un desenfoque para quitarle un poco el ruido y ayudar a que se vean mejor los bordes. Luego detecta esos bordes, dándole ese look como de líneas dibujadas a mano, tipo cómic. Al mismo tiempo, le pasa un filtro que suaviza los colores pero sin perder los detalles de los bordes, lo que hace que la imagen se vea como más plana, como si fuera una ilustración. Al final, junta esos bordes con la imagen suavizada, le pone un texto que dice que es un filtro cómic, muestra la imagen original y la modificada, y guarda el resultado en un nuevo archivo. Solo se necesita tener instalada la librería OpenCV y tener la imagen dentro de la carpeta de el proyecto.
