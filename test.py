import cv2

# Cargar el video
video = cv2.VideoCapture('video.mp4')

# Cargar la imagen
imagen = cv2.imread('output_images/FPqJAQtkcm.png', cv2.IMREAD_UNCHANGED)

# Obtener el ancho y alto de la imagen
imagen_alto, imagen_ancho, _ = imagen.shape

# Definir las coordenadas donde se colocará la imagen en el video
x = 100
y = 100

# Obtener el framerate del video
fps = video.get(cv2.CAP_PROP_FPS)

# Obtener el tamaño del video
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Crear objeto VideoWriter para escribir el video resultante
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('video_con_imagen.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    # Leer un frame del video
    ret, frame = video.read()
    if not ret:
        break

    # Superponer la imagen en el frame del video
    frame[y:y+imagen_alto, x:x+imagen_ancho] = imagen[:, :, :3] * (imagen[:, :, 3:] / 255.0) + frame[y:y+imagen_alto, x:x+imagen_ancho] * (1.0 - imagen[:, :, 3:] / 255.0)

    # Escribir el frame resultante en el video de salida
    out.write(frame)

    # Mostrar el frame resultante
    cv2.imshow('Video con imagen superpuesta', frame)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Liberar los recursos
video.release()
out.release()
cv2.destroyAllWindows()
