import os
import random
import pygame
import mutagen
from mutagen.mp3 import MP3
import clases as c
import funciones as f


if __name__ == "__main__":
    pygame.init()

    screen_size = (1280, 720)
    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))

    dark_grey = (30, 30, 30)
    pygame.display.set_caption('Not Spotify')

    title = "Not Spotify"
    title_font_size = int(screen_size[1] * 0.12)

    title_y = screen_size[1] * 0.1
    title_font = pygame.font.SysFont(
        "Comic Sans MS", title_font_size, bold=True)
    text_surface = title_font.render(title, True, [255, 255, 255])
    text_rect = text_surface.get_rect(center=(screen_size[0] / 2, title_y))
    screen.blit(text_surface, text_rect)

    playing_label_font_size = int(screen_size[1] * 0.05)
    playing_label_font = pygame.font.SysFont(
        "Comic Sans MS", playing_label_font_size)
    playing_label_y = screen_size[1] * 0.4

    buttons_font_size = int(screen_size[1] * 0.05)
    button_width = int(screen_size[0] * 0.16)
    button_height = int(screen_size[1] * 0.08)

    button_x = screen_size[0] * 0.05
    play_button_y = screen_size[1] * 0.42
    quit_button_y = screen_size[1] * 0.55

    buttons_font = pygame.font.SysFont("Comic Sans MS", buttons_font_size)

    PlayBoton = c.Button((screen_size[0]*0.475, screen_size[1]*0.805),
                         (screen_size[0]*0.049, screen_size[1]*0.065), 0, "", "white")
    SiguienteCancionBoton = c.Button((screen_size[0]*0.603, screen_size[1]*0.805),
                                     (screen_size[0]*0.047, screen_size[1]*0.065), 0, "", "white")
    AnteriorCancionBoton = c.Button((screen_size[0]*0.343, screen_size[1]*0.805),
                                    (screen_size[0]*0.046, screen_size[1]*0.065), 0, "", "white")
    RepetirBoton = c.Button((screen_size[0]*0.731, screen_size[1]*0.805),
                            (screen_size[0]*0.047, screen_size[1]*0.065), 0, "", "white")
    ShuffleBoton = c.Button((screen_size[0]*0.211, screen_size[1]*0.805),
                            (screen_size[0]*0.046, screen_size[1]*0.065), 0, "", "white")
    VolumeBoton = c.Button((screen_size[0]*0.822, screen_size[1]*0.875),
                           (screen_size[0]*0.03, screen_size[1]*0.05), 1, "v", "white")

    PBPos = PlayBoton.position
    PBSize = PlayBoton.size
    SCBPos = SiguienteCancionBoton.position
    SCBSize = SiguienteCancionBoton.size
    ACBPos = AnteriorCancionBoton.position
    ACBSize = AnteriorCancionBoton.size
    RBPos = RepetirBoton.position
    RBSize = RepetirBoton.size
    SBPos = ShuffleBoton.position
    SBSize = ShuffleBoton.size
    VBPos = VolumeBoton.position
    VBSize = VolumeBoton.size

    anterior = pygame.image.load("./assets/anterior.png")
    anterior = pygame.transform.scale(
        anterior, (screen_size[0]*0.05, screen_size[1]*0.07))
    siguiente = pygame.image.load("./assets/siguiente.png")
    siguiente = pygame.transform.scale(
        siguiente, (screen_size[0]*0.05, screen_size[1]*0.07))
    anterior_nohover = pygame.image.load("./assets/anterior_nohover.png")
    anterior_nohover = pygame.transform.scale(
        anterior_nohover, (screen_size[0]*0.05, screen_size[1]*0.07))
    siguiente_nohover = pygame.image.load("./assets/siguiente_nohover.png")
    siguiente_nohover = pygame.transform.scale(
        siguiente_nohover, (screen_size[0]*0.05, screen_size[1]*0.07))
    play = pygame.image.load("./assets/play.png")
    play = pygame.transform.scale(
        play, (screen_size[0]*0.06, screen_size[1]*0.08))
    play_nohover = pygame.image.load("./assets/play_nohover.png")
    play_nohover = pygame.transform.scale(
        play_nohover, (screen_size[0]*0.06, screen_size[1]*0.08))
    pause = pygame.image.load("./assets/pause.png")
    pause = pygame.transform.scale(
        pause, (screen_size[0]*0.06, screen_size[1]*0.08))
    pause_nohover = pygame.image.load("./assets/pause_nohover.png")
    pause_nohover = pygame.transform.scale(
        pause_nohover, (screen_size[0]*0.06, screen_size[1]*0.08))
    shuffle_icon = pygame.image.load("./assets/shuffle.png")
    shuffle_icon = pygame.transform.scale(
        shuffle_icon, (screen_size[0]*0.06, screen_size[1]*0.08))
    shuffle_nohover = pygame.image.load("./assets/shuffle_nohover.png")
    shuffle_nohover = pygame.transform.scale(
        shuffle_nohover, (screen_size[0]*0.06, screen_size[1]*0.08))
    repeat = pygame.image.load("./assets/repeat.png")
    repeat = pygame.transform.scale(
        repeat, (screen_size[0]*0.06, screen_size[1]*0.08))
    repeat_nohover = pygame.image.load("./assets/repeat_nohover.png")
    repeat_nohover = pygame.transform.scale(
        repeat_nohover, (screen_size[0]*0.06, screen_size[1]*0.08))
    shuffle_on = pygame.image.load("./assets/shuffle_on.png")
    shuffle_on = pygame.transform.scale(
        shuffle_on, (screen_size[0]*0.06, screen_size[1]*0.08))
    shuffle_on_nohover = pygame.image.load("./assets/shuffle_on_nohover.png")
    shuffle_on_nohover = pygame.transform.scale(
        shuffle_on_nohover, (screen_size[0]*0.06, screen_size[1]*0.08))
    repeat_on = pygame.image.load("./assets/repeat_on.png")
    repeat_on = pygame.transform.scale(
        repeat_on, (screen_size[0]*0.06, screen_size[1]*0.08))
    repeat_on_nohover = pygame.image.load("./assets/repeat_on_nohover.png")
    repeat_on_nohover = pygame.transform.scale(
        repeat_on_nohover, (screen_size[0]*0.06, screen_size[1]*0.08))
    volume_on = pygame.image.load("./assets/volume_on.png")
    volume_on = pygame.transform.scale(
        volume_on, (screen_size[0]*0.03, screen_size[1]*0.05))
    volume_on_nohover = pygame.image.load("./assets/volume_on_nohover.png")
    volume_on_nohover = pygame.transform.scale(
        volume_on_nohover, (screen_size[0]*0.03, screen_size[1]*0.05))
    volume_off = pygame.image.load("./assets/volume_off.png")
    volume_off = pygame.transform.scale(
        volume_off, (screen_size[0]*0.03, screen_size[1]*0.05))
    volume_off_nohover = pygame.image.load("./assets/volume_off_nohover.png")
    volume_off_nohover = pygame.transform.scale(
        volume_off_nohover, (screen_size[0]*0.03, screen_size[1]*0.05))

    lmb_pressed = False
    pos = (0, 0)
    shuffle = False
    created = False
    pausa = False
    repetir = False
    primera_playlist = True
    volume = True

    slider_x, slider_y = screen_size[0]*0.86, screen_size[1]*0.89
    slider_length, slider_height = 150, 10
    handle_radius = 12
    volume_level = 0.5
    handle_x = slider_x + volume_level * slider_length
    dragging = False
    volume_antiguo = 0.5
    volume_muted = False

    path = './Mp3/'
    files = os.listdir(path)
    queue_x = screen_size[0]*0.82
    queue_y = screen_size[1]*0.59
    queue_speed = 0.3
    queue_delay = 2000
    queue_reset_time = pygame.time.get_ticks() + queue_delay

    progress_bar_x = screen_size[0]*0.25
    progress_bar_y = screen_size[1]*0.92
    progress_bar_length = screen_size[0]*0.5
    progress_bar_height = 20
    progress_color = (70, 130, 180)

    current_time = 0
    total_length = 0

    pygame.mixer.init()
    playing = False
    cancion_actual = None
    reproduciendo_actual = False

    # Comienzo main loop

    running = True
    while running:

        # Eventos de pygame

        pos = (0, 0)
        hover_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            lmb_pressed = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and lmb_pressed:
                pos = pygame.mouse.get_pos()
                lmb_pressed = False
                dragging = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if abs(event.pos[0] - handle_x) <= handle_radius and abs(event.pos[1] - (slider_y + slider_height // 2)) <= handle_radius:
                    dragging = True
            elif event.type == pygame.MOUSEMOTION and dragging:
                handle_x = max(slider_x, min(
                    event.pos[0], slider_x + slider_length))
                volume_level = (handle_x - slider_x) / slider_length
                pygame.mixer.music.set_volume(volume_level)
                volume_muted = (volume_level == 0)

        # Crea las listas de reproducción

        if shuffle and not created:
            lista = f.reproduccion_random()
            created = True
        elif not shuffle and not created:
            lista = f.reproduccion_normal()
            created = True

        # Carga todo la primera vez o actualiza el tiempo de la canción

        if not playing:
            pygame.mixer.music.load(lista.head.archivo)
            total_length = lista.head.segundos
            current_time = 0
            playing = True
            pausa = True
            primera_vez = True
        else:
            if primera_vez:
                current_time = 0
            else:
                current_time = pygame.mixer.music.get_pos() / 1000.0

        # Eventos de los botones

        # Botón de Play
        if (pos[0] >= PBPos[0]) and (pos[0] <= PBPos[0] + PBSize[0]) and (pos[1] >= PBPos[1]) and (pos[1] <= PBPos[1] + PBSize[1]):
            if not pausa:
                pausa = True
                pygame.mixer.music.pause()
            elif primera_vez:
                pygame.mixer.music.play()
                primera_vez = False
                pausa = False
            else:
                pausa = False
                pygame.mixer.music.unpause()

        # Botón de Siguiente Canción
        elif (pos[0] >= SCBPos[0]) and (pos[0] <= SCBPos[0] + SCBSize[0]) and (pos[1] >= SCBPos[1]) and (pos[1] <= SCBPos[1] + SCBSize[1]):
            if lista.head.get_siguiente() == lista.primero and not repetir:
                pygame.mixer.music.stop()
                current_time = 0
                pausa = True
                playing = False
            else:
                if primera_playlist and lista.head.get_siguiente() == lista.primero:
                    primera_playlist = False
                lista.skip_cancion()
                current_time = 0
                reproduciendo_actual = False
                pygame.mixer.music.load(lista.head.archivo)
                total_length = lista.head.segundos
                primera_vez = False
                pygame.mixer.music.play()
                pausa = False

        # Botón de Canción Anterior
        elif (pos[0] >= ACBPos[0]) and (pos[0] <= ACBPos[0] + ACBSize[0]) and (pos[1] >= ACBPos[1]) and (pos[1] <= ACBPos[1] + ACBSize[1]):
            if lista.head != lista.primero or not primera_playlist:
                lista.anterior_cancion()
                pygame.mixer.music.load(lista.head.archivo)
                current_time = 0
                pygame.mixer.music.play()
                pausa = False
                playing = True

        # Botón de Repetir la lista de reproducción
        elif (pos[0] >= RBPos[0]) and (pos[0] <= RBPos[0] + RBSize[0]) and (pos[1] >= RBPos[1]) and (pos[1] <= RBPos[1] + RBSize[1]):
            repetir = not repetir

        # Botón de Shuffle (Aleatorio) On/Off
        elif (pos[0] >= SBPos[0]) and (pos[0] <= SBPos[0] + SBSize[0]) and (pos[1] >= SBPos[1]) and (pos[1] <= SBPos[1] + SBSize[1]):
            shuffle = not shuffle
            cancion_actual = lista.head.nombre
            reproduciendo_actual = True
            created = False

        # Botón de Volumen On/Off
        elif (pos[0] >= VBPos[0]) and (pos[0] <= VBPos[0] + VBSize[0]) and (pos[1] >= VBPos[1]) and (pos[1] <= VBPos[1] + VBSize[1]):
            if volume_muted or pygame.mixer.music.get_volume() == 0:
                pygame.mixer.music.set_volume(
                    volume_antiguo if volume_antiguo > 0 else 0.5)
                volume_muted = False
            else:
                volume_antiguo = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(0)
                volume_muted = True

        # Actualiza la posición del ratón

        SiguienteCancionBoton.update_hover(hover_pos)
        AnteriorCancionBoton.update_hover(hover_pos)
        PlayBoton.update_hover(hover_pos)
        ShuffleBoton.update_hover(hover_pos)
        RepetirBoton.update_hover(hover_pos)
        VolumeBoton.update_hover(hover_pos)

        # Dibuja la barra de progreso de la canción

        screen.fill(dark_grey)
        screen.blit(text_surface, text_rect)
        pygame.draw.rect(screen, (100, 100, 100), (progress_bar_x,
                         progress_bar_y, progress_bar_length, progress_bar_height))

        # Canción en reproducción actualmente

        if reproduciendo_actual:
            if cancion_actual != None:
                playing_label_surface = playing_label_font.render(
                    f"En reproducción: {cancion_actual}", True, (255, 255, 255))
            else:
                playing_label_surface = playing_label_font.render(
                    f"En reproducción: {lista.head.nombre}", True, (255, 255, 255))
        else:
            playing_label_surface = playing_label_font.render(
                f"En reproducción: {lista.head.nombre}", True, (255, 255, 255))
        playing_label_rect = playing_label_surface.get_rect(
            center=(screen_size[0] / 2, playing_label_y))
        screen.blit(playing_label_surface, playing_label_rect)

        # Mira si los botones están hovereados o no

        if PlayBoton.hovered:
            if pausa:
                screen.blit(play, (screen_size[0]*0.47, screen_size[1]*0.795))
            else:
                screen.blit(pause, (screen_size[0]*0.47, screen_size[1]*0.795))
        else:
            if pausa:
                screen.blit(
                    play_nohover, (screen_size[0]*0.47, screen_size[1]*0.795))
            else:
                screen.blit(pause_nohover,
                            (screen_size[0]*0.47, screen_size[1]*0.795))

        if SiguienteCancionBoton.hovered:
            screen.blit(siguiente, (screen_size[0]*0.6, screen_size[1]*0.8))
        else:
            screen.blit(siguiente_nohover,
                        (screen_size[0]*0.6, screen_size[1]*0.8))

        if AnteriorCancionBoton.hovered:
            screen.blit(anterior, (screen_size[0]*0.34, screen_size[1]*0.8))
        else:
            screen.blit(anterior_nohover,
                        (screen_size[0]*0.34, screen_size[1]*0.8))

        if RepetirBoton.hovered:
            if repetir:
                screen.blit(
                    repeat_on, (screen_size[0]*0.725, screen_size[1]*0.79))
            else:
                screen.blit(
                    repeat, (screen_size[0]*0.725, screen_size[1]*0.79))
        else:
            if repetir:
                screen.blit(repeat_on_nohover,
                            (screen_size[0]*0.725, screen_size[1]*0.79))
            else:
                screen.blit(repeat_nohover,
                            (screen_size[0]*0.725, screen_size[1]*0.79))

        if ShuffleBoton.hovered:
            if shuffle:
                screen.blit(
                    shuffle_on, (screen_size[0]*0.205, screen_size[1]*0.79))
            else:
                screen.blit(
                    shuffle_icon, (screen_size[0]*0.205, screen_size[1]*0.79))
        else:
            if shuffle:
                screen.blit(shuffle_on_nohover,
                            (screen_size[0]*0.205, screen_size[1]*0.79))
            else:
                screen.blit(shuffle_nohover,
                            (screen_size[0]*0.205, screen_size[1]*0.79))

        if VolumeBoton.hovered:
            if volume_muted or volume_level == 0:
                screen.blit(
                    volume_off, (screen_size[0]*0.822, screen_size[1]*0.876))
            else:
                screen.blit(
                    volume_on, (screen_size[0]*0.822, screen_size[1]*0.876))
        else:
            if volume_muted or volume_level == 0:
                screen.blit(volume_off_nohover,
                            (screen_size[0]*0.822, screen_size[1]*0.876))
            else:
                screen.blit(volume_on_nohover,
                            (screen_size[0]*0.822, screen_size[1]*0.876))

        # Cálculos para barra de tiempo de reproducción

        if total_length > 0:
            filled_length = (current_time / total_length) * progress_bar_length
            pygame.draw.rect(screen, progress_color, (progress_bar_x,
                             progress_bar_y, filled_length, progress_bar_height))

        formatted_current_time = f.format_time(current_time)
        formatted_total_length = f.format_time(total_length)

        current_time_label = pygame.font.SysFont("Comic Sans MS", 20).render(
            formatted_current_time, True, (255, 255, 255))
        total_time_label = pygame.font.SysFont("Comic Sans MS", 20).render(
            formatted_total_length, True, (255, 255, 255))

        screen.blit(current_time_label, (progress_bar_x - current_time_label.get_width() - 10,
                    progress_bar_y + (progress_bar_height / 2) - (current_time_label.get_height() / 2)))
        screen.blit(total_time_label, (progress_bar_x + progress_bar_length + 10,
                    progress_bar_y + (progress_bar_height / 2) - (total_time_label.get_height() / 2)))

        # Controla si debe parar la reproducción

        if current_time >= total_length and total_length > 0:
            if lista.head.get_siguiente() == lista.primero and not repetir:
                pygame.mixer.music.stop()
                current_time = 0
                pausa = True
                playing = False
                total_length = lista.head.segundos
            else:
                if primera_playlist and lista.head.get_siguiente() == lista.primero:
                    primera_playlist = False
                lista.skip_cancion()
                current_time = 0
                reproduciendo_actual = False
                pygame.mixer.music.load(lista.head.archivo)
                total_length = lista.head.segundos
                pygame.mixer.music.play()
                pausa = False

        # Muestra la cola de reproducción

        current_time = pygame.time.get_ticks()
        if current_time > queue_reset_time:
            queue_x -= queue_speed

            text_width, _ = buttons_font.size(queue_text)
            if queue_x + text_width < 0:
                queue_x = screen_size[0]
                queue_reset_time = current_time + queue_delay

        queue_box = pygame.Rect(
            screen_size[0]*0.195, screen_size[1]*0.6, screen_size[0]*0.61, 40)
        pygame.draw.rect(screen, (18, 18, 18), queue_box, 0)
        pygame.draw.rect(screen, (255, 255, 255), queue_box, 2)
        screen.set_clip(queue_box)
        queue_text = lista.texto_cola(repetir)
        queue_surface = buttons_font.render(queue_text, True, (255, 255, 255))
        screen.blit(queue_surface, (queue_x, queue_y))

        screen.set_clip(None)

        # Dibuja slider de volumen

        f.draw_volume_slider(screen, slider_x, slider_y, slider_length,
                             slider_height, handle_x, handle_radius)

        pygame.display.flip()

    pygame.quit()
