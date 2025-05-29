import cv2

# Cargar la imagen
imagen = cv2.imread('persona.jpg')

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un desenfoque mediano para reducir el ruido
gris_suavizado = cv2.medianBlur(gris, 7)

# Detectar bordes usando el método adaptive threshold
bordes = cv2.adaptiveThreshold(gris_suavizado, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)

# Aplicar un filtro bilateral para reducir colores pero conservar bordes
color = cv2.bilateralFilter(imagen, d=9, sigmaColor=250, sigmaSpace=250)

# Combinar bordes y la imagen suavizada para dar efecto cómic
filtro_comic = cv2.bitwise_and(color, color, mask=bordes)

# Agregar texto sobre la imagen
cv2.putText(filtro_comic, 'Filtro: Comic', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)

# Mostrar imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen con Filtro Comic', filtro_comic)

# Guardar imagen
cv2.imwrite('person_filtro_comic.jpg', filtro_comic)
print("Su imagen fue guardada correctamente")

cv2.waitKey(0)
cv2.destroyAllWindows()
