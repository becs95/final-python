# Rebeca Soberanis Trujillo 
# proyecto avance 2

# Definición de la clase Persona
class Persona:
    def __init__(self):
        self.nombre = ""
        self.id_nomina = ""

    def capturar_nombre(self):
        self.nombre = input("Ingresa el nombre de la persona: ")

    def capturar_id_nomina(self):
        self.id_nomina = input("Ingresa el número de nómina: ")

    def imprimir_nombre(self):
        print("Nombre de la persona:", self.nombre)

    def imprimir_id_nomina(self):
        print("Número de nómina:", self.id_nomina)

# Definición de la clase Videos
class Videos:
    def __init__(self):
        self.nombre_video = ""
        self.extension_video = ""
        self.tamaño_video = 0.0

    def capturar_nombre_video(self):
        self.nombre_video = input("Ingresa el nombre del video: ")

    def capturar_extension_video(self):
        self.extension_video = input("Ingresa la extensión del video (.mpg, .mov, etc.): ")

    def capturar_tamaño_video(self):
        while True:
            try:
                self.tamaño_video = float(input("Ingresa el tamaño del video en MB (no mayor a 3 MB): "))
                if 0 <= self.tamaño_video <= 3:
                    break
                else:
                    print("El tamaño del video no puede ser mayor a 3 MB.")
            except ValueError:
                print("Debes ingresar un número válido para el tamaño del video.")

    def imprimir_nombre_video(self):
        print("Nombre del video:", self.nombre_video)

    def imprimir_extension_video(self):
        print("Extensión del video:", self.extension_video)

    def imprimir_tamaño_video(self):
        print("Tamaño del video (MB):", self.tamaño_video)

# Crear objetos de las clases "Persona" y "Videos"
persona = Persona()
video = Videos()

# Etapa 1: Capturar información de la persona
persona.capturar_nombre()
persona.capturar_id_nomina()

# Etapa 2: Capturar información de los videos
cantidad_videos = int(input("Cuántos videos deseas subir: "))
videos = []

for i in range(cantidad_videos):
    video.capturar_nombre_video()
    video.capturar_extension_video()
    video.capturar_tamaño_video()
    videos.append(video.__dict__)  # Guardar la información del video como un diccionario

# Etapa 3: Mostrar información de la persona y los videos
persona.imprimir_nombre()
persona.imprimir_id_nomina()

print("Información de los videos:")
for i, v in enumerate(videos):
    print(f"Video {i + 1}:")
    for key, value in v.items():
        print(f"{key}: {value}")

# Etapa 4: Guardar la información en un archivo salida.txt
with open("salida.txt", "w") as archivo:
    archivo.write(f"{persona.id_nomina} | {persona.nombre} | {cantidad_videos} |")
    for video in videos:
        for key, value in video.items():
            archivo.write(f" {value} |")
    archivo.write("\n")

print("Información guardada en el archivo 'salida.txt'.")
