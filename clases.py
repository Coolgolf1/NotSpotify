import pygame


class Cancion:
    def __init__(self, archivo, nombre, duracion, segundos):
        self.archivo = archivo
        self.nombre = nombre
        self.duracion = duracion
        self.segundos = segundos
        self.next = None
        self.back = None

    def __str__(self):
        return f"Nombre: {self.nombre}\nDuración: {self.duracion}"

    def set_siguiente(self, next):
        self.next = next

    def get_siguiente(self):
        return self.next

    def set_back(self, back):
        self.back = back

    def get_back(self):
        return self.back

    def get_nombre(self):
        return self.nombre

    def get_duracion(self):
        return self.duracion


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.primero = None
        self.cola = None

    def anadir_cancion(self, cancion):
        if self.head == None:
            self.primero = cancion
            self.head = cancion
            self.cola = cancion
        else:
            actual = self.cola
            actual.set_siguiente(cancion)
            cancion.set_back(actual)
            self.cola = cancion
            self.cola.set_siguiente(self.primero)
            self.primero.set_back(self.cola)

    def texto_cola(self, repetir):
        actual = self.head.get_siguiente()
        queue_text = "Cola de reproducción:"
        if not repetir:
            if self.head != self.cola:
                while actual.get_siguiente() != self.primero:
                    queue_text += f" {actual.nombre}   >  "
                    actual = actual.get_siguiente()
                queue_text += f" {actual.nombre}"
        else:
            count = 0
            while count < 6:
                queue_text += f" {actual.nombre}   >  "
                actual = actual.get_siguiente()
                count += 1
            queue_text += f" {actual.nombre}"
        return queue_text

    def skip_cancion(self):
        actual = self.head
        self.head = actual.get_siguiente()

    def anterior_cancion(self):
        actual = self.head
        self.head = actual.get_back()


class Button:
    def __init__(self, position: tuple[float, float], size: tuple[float, float], outline_width: int, text: str, colour: str):
        self.colour = colour
        self.position = position
        self.size = size
        self.outline_width = outline_width
        self.text = text
        self.original_size = size
        self.hovered = False

    def is_hovered(self, mouse_pos: tuple[int, int]) -> bool:
        """Chequea si el ratón está por encima del botón o no.

        Args:
            mouse_pos (tuple[int, int]): La posición del ratón.

        Returns:
            bool: Devuelve si el ratón está o no encima del botón.
        """
        if (self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and
                self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]):
            if not self.hovered:
                self.hovered = True
                return True
        else:
            self.hovered = False
        return False

    def update_hover(self, mouse_pos: tuple[int, int]) -> bool:
        """Mira si tras un movimiento de ratón, el ratón sigue encima del botón o no. 

        Args:
            mouse_pos (tuple[int, int]): La posición del ratón.

        Returns:
            bool: Devuelve la condición de si el ratón sigue encima o no del botón.
        """
        previously_hovered = self.hovered
        self.hovered = self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and \
            self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]
        return self.hovered != previously_hovered
