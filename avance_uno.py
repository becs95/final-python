# rebeca Soberanis Trujillo
# final project part 1

# Solicitamos al usuario su número de nómina
numero_nomina = input("Por favor, ingresa tu número de nómina: ")

# Solicitar al usuario su nombre
nombre_usuario = input("Ingresa tu nombre: ")

# Solicitar al usuario la cantidad de videos a subir
try:
    cantidad_videos = int(input("Cuántos videos deseas subir: "))
except ValueError:
    print("Error: Debes ingresar un número válido para la cantidad de videos.")
    exit()

# Mostrar mensaje de confirmación
print(f"Bienvenido, {nombre_usuario}, tu número de nómina es {numero_nomina} y estás intentando subir {cantidad_videos} videos.")
confirmacion = input("¿Es correcta la información? (Sí/No): ")

if confirmacion.lower() == "sí":
    print("Información confirmada. ¡Continuemos con la carga de videos!")
    
    # Crear una lista para almacenar los detalles de los videos
    videos = []
    
    # Solicitar detalles para cada video
    for i in range(cantidad_videos):
        print(f"\nIngresa los detalles para el video {i + 1}:")
        
        titulo = input("Título del video: ")
        nombre_video = input("Nombre del video: ")
        extension = input("Extensión del video (.mpg, .mov, etc.): ")
        
        # Solicitar el tamaño del video y verificar si no es mayor a 3 MB
        while True:
            try:
                tamaño = float(input("Tamaño del video en MB (no mayor a 3 MB): "))
                if tamaño <= 3:
                    break
                else:
                    print("El tamaño del video no puede ser mayor a 3 MB.")
            except ValueError:
                print("Debes ingresar un número válido para el tamaño del video.")
        
        # Agregar los detalles del video a la lista
        video = {
            "Título": titulo,
            "Nombre del Video": nombre_video,
            "Extensión": extension,
            "Tamaño (MB)": tamaño
        }
        videos.append(video)
    
    # Mostrar los detalles de los videos
    print("\nDetalles de los videos a subir:")
    for i, video in enumerate(videos):
        print(f"Video {i + 1}:")
        for key, value in video.items():
            print(f"{key}: {value}")
    
    # Mostrar los detalles de los videos
    print("\nDetalles de los videos a subir:")
    for i, video in enumerate(videos):
        print(f"Video {i + 1}:")
        for key, value in video.items():
            print(f"{key}: {value}")
    
    # Guardar la información en un archivo salida.txt
    with open("salida.txt", "w") as archivo:
        archivo.write(f"{numero_nomina} | {nombre_usuario} | {cantidad_videos} |")
        for video in videos:
            for key, value in video.items():
                archivo.write(f" {value} |")
        archivo.write("\n")
    print("Información guardada en el archivo 'salida.txt'.")

else:
    print(" Muchas gracias por haber usado nuestro sistema, hasta pronto.")




