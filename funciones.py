import random
import os
import clases as c
import mutagen
import pygame
from mutagen.mp3 import MP3


def reproduccion_normal():
    lista_normal = c.ListaEnlazada()
    path = './Mp3/'
    files = os.listdir(path)
    for file in files:
        cancion_cargada = MP3(f"{path+file}")
        informacion_cancion = cancion_cargada.info
        duracion = int(informacion_cancion.length)
        horas, mins, segundos = calcular_duracion(duracion-6)
        if int(segundos) < 10:
            segundos = f"0{segundos}"
        if int(horas) > 0:
            if int(mins) < 10:
                mins = f"0{mins}"
            lista_normal.anadir_cancion(c.Cancion(
                path+file, file.rsplit('.mp3', 1)[0], (f"{horas}:{mins}:{segundos}"), duracion-6))
        else:
            lista_normal.anadir_cancion(
                c.Cancion(path+file, file.rsplit('.mp3', 1)[0], (f"{mins}:{segundos}"), duracion-6))
    return lista_normal


def reproduccion_random():
    lista_random = c.ListaEnlazada()
    path = './Mp3/'
    files = os.listdir(path)
    shuffled = []
    while len(shuffled) < len(files):
        file = random.choice(files)
        if file not in shuffled:
            shuffled.append(file)
    for cancion in shuffled:
        cancion_cargada = MP3(f"{path+cancion}")
        informacion_cancion = cancion_cargada.info
        duracion = int(informacion_cancion.length)
        horas, mins, segundos = calcular_duracion(duracion-7)
        if int(segundos) < 10:
            segundos = f"0{segundos}"
        if int(horas) > 0:
            if int(mins) < 10:
                mins = f"0{mins}"
            lista_random.anadir_cancion(
                c.Cancion(path+cancion, cancion.rsplit('.mp3', 1)[0], (f"{horas}:{mins}:{segundos}"), duracion-7))
        else:
            lista_random.anadir_cancion(
                c.Cancion(path+cancion, cancion.rsplit('.mp3', 1)[0], (f"{mins}:{segundos}"), duracion-7))
    return lista_random


def calcular_duracion(duracion):
    horas = duracion // 3600
    duracion %= 3600
    mins = duracion // 60
    duracion %= 60
    segundos = duracion
    return horas, mins, segundos


def format_time(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    if hours > 0:
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    else:
        return f"{int(minutes):02}:{int(seconds):02}"


def draw_volume_slider(screen, slider_x, slider_y, slider_length, slider_height, handle_x, handle_radius):
    pygame.draw.rect(screen, (60, 60, 60), (slider_x,
                     slider_y, slider_length, slider_height))
    pygame.draw.rect(screen, (255, 255, 255), (slider_x,
                     slider_y, handle_x-slider_x, slider_height))
    pygame.draw.circle(screen, (11, 151, 41), (int(handle_x),
                       slider_y + slider_height // 2), handle_radius)
