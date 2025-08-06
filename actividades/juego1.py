import pygame
import random
import sys

pygame.init()

# Configuración pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Blackjack con Pygame - Créditos y Rondas")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 128, 0)
ROJO = (200, 0, 0)
GRIS = (200, 200, 200)
AZUL = (0, 0, 255)
FONDO = (34, 139, 34)

# Fuente
FUENTE = pygame.font.SysFont("arial", 24)

def crear_baraja():
    palos = ['♥', '♦', '♣', '♠']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [(v, p) for p in palos for v in valores]
    random.shuffle(baraja)
    return baraja

def valor_carta(carta):
    valor = carta[0]
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)

def valor_mano(mano):
    total = sum(valor_carta(c) for c in mano)
    ases = sum(1 for c in mano if c[0] == 'A')
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def dibujar_texto(texto, x, y, color=NEGRO):
    render = FUENTE.render(texto, True, color)
    pantalla.blit(render, (x, y))

def dibujar_mano(mano, x, y):
    for i, carta in enumerate(mano):
        texto = f"{carta[0]}{carta[1]}"
        dibujar_texto(texto, x + i*60, y)

class Boton:
    def __init__(self, texto, x, y, w, h, color, color_hover):
        self.texto = texto
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.color_hover = color_hover

    def dibujar(self, pantalla):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(pantalla, self.color_hover, self.rect, border_radius=5)
        else:
            pygame.draw.rect(pantalla, self.color, self.rect, border_radius=5)
        txt = FUENTE.render(self.texto, True, BLANCO)
        txt_rect = txt.get_rect(center=self.rect.center)
        pantalla.blit(txt, txt_rect)

    def clickeado(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                return True
        return False

def pedir_apuesta(creditos):
    apuesta = ""
    esperando = True
    reloj = pygame.time.Clock()
    while esperando:
        pantalla.fill(FONDO)
        dibujar_texto(f"Créditos disponibles: {creditos}", 50, 50, BLANCO)
        dibujar_texto("Ingresa tu apuesta y presiona Enter:", 50, 100, BLANCO)
        dibujar_texto(apuesta, 50, 150, AZUL)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    apuesta = apuesta[:-1]
                elif evento.key == pygame.K_RETURN:
                    if apuesta.isdigit():
                        val = int(apuesta)
                        if 1 <= val <= creditos:
                            return val
                        else:
                            apuesta = ""
                    else:
                        apuesta = ""
                else:
                    if evento.unicode.isdigit():
                        apuesta += evento.unicode

        pygame.display.flip()
        reloj.tick(30)

def main():
    creditos = 100
    reloj = pygame.time.Clock()

    # Botones
    boton_hit = Boton("Pedir (Hit)", 50, ALTO - 90, 140, 50, VERDE, (0, 200, 0))
    boton_stand = Boton("Plantarse (Stand)", 210, ALTO - 90, 160, 50, ROJO, (200, 0, 0))
    boton_double = Boton("Doblar (Double)", 390, ALTO - 90, 160, 50, (0, 0, 180), (0, 0, 255))
    boton_surrender = Boton("Rendirse (Surrender)", 570, ALTO - 90, 210, 50, (128, 128, 128), (180, 180, 180))

    while True:
        if creditos <= 0:
            pantalla.fill(FONDO)
            dibujar_texto("¡Te quedaste sin créditos!", 250, 250, ROJO)
            dibujar_texto("Presiona R para reiniciar o Q para salir.", 150, 300, BLANCO)
            pygame.display.flip()
            esperando = True
            while esperando:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            creditos = 100
                            esperando = False
                        elif evento.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                reloj.tick(30)
            continue

        baraja = crear_baraja()
        mano_jugador = [baraja.pop(), baraja.pop()]
        mano_banca = [baraja.pop(), baraja.pop()]
        turno_jugador = True
        resultado = ""
        apuesta = pedir_apuesta(creditos)
        apuesta_actual = apuesta  # Para doblar

        jugando = True
        doblado = False
        rendirse = False

        while jugando:
            pantalla.fill(FONDO)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if turno_jugador and not resultado:
                    if boton_hit.clickeado(evento):
                        mano_jugador.append(baraja.pop())
                        if valor_mano(mano_jugador) > 21:
                            resultado = "¡Te pasaste! Pierdes."
                            creditos -= apuesta_actual
                    elif boton_stand.clickeado(evento):
                        turno_jugador = False
                    elif boton_double.clickeado(evento):
                        # Solo puede doblar si tiene créditos suficientes
                        if not doblado and creditos >= apuesta_actual * 2:
                            mano_jugador.append(baraja.pop())
                            apuesta_actual *= 2
                            doblado = True
                            if valor_mano(mano_jugador) > 21:
                                resultado = "¡Te pasaste! Pierdes."
                                creditos -= apuesta_actual
                            else:
                                turno_jugador = False
                    elif boton_surrender.clickeado(evento):
                        resultado = "Te rendiste. Pierdes la mitad de tu apuesta."
                        creditos -= apuesta_actual // 2
                        rendirse = True

            # Mostrar créditos y apuesta
            dibujar_texto(f"Créditos: {creditos}", 600, 10, BLANCO)
            dibujar_texto(f"Apuesta: {apuesta_actual}", 600, 40, BLANCO)

            # Mostrar manos
            dibujar_texto("Mano del Jugador:", 50, 50, BLANCO)
            dibujar_mano(mano_jugador, 50, 80)
            dibujar_texto(f"Total: {valor_mano(mano_jugador)}", 50, 120, BLANCO)

            dibujar_texto("Mano de la Banca:", 50, 180, BLANCO)
            if not resultado and turno_jugador:
                dibujar_texto("??", 50, 210, BLANCO)
                if len(mano_banca) > 1:
                    dibujar_mano(mano_banca[1:], 110, 210)
            else:
                dibujar_mano(mano_banca, 50, 210)
                dibujar_texto(f"Total: {valor_mano(mano_banca)}", 50, 250, BLANCO)

            # Dibujar botones si está turno jugador y no hay resultado ni rendición
            if turno_jugador and not resultado and not rendirse:
                boton_hit.dibujar(pantalla)
                boton_stand.dibujar(pantalla)
                # Solo mostrar doblar si es la primera jugada y hay créditos suficientes
                if len(mano_jugador) == 2 and creditos >= apuesta_actual * 2 and not doblado:
                    boton_double.dibujar(pantalla)
                # Solo mostrar rendirse si es la primera jugada y no ha doblado
                if len(mano_jugador) == 2 and not doblado:
                    boton_surrender.dibujar(pantalla)

            # Cuando termina turno jugador y no hubo rendición
            if not turno_jugador and not resultado and not rendirse:
                while valor_mano(mano_banca) < 17:
                    mano_banca.append(baraja.pop())

                v_j = valor_mano(mano_jugador)
                v_b = valor_mano(mano_banca)

                if v_b > 21:
                    resultado = "La banca se pasó. ¡Ganaste!"
                    creditos += apuesta_actual
                elif v_b > v_j:
                    resultado = "La banca gana."
                    creditos -= apuesta_actual
                elif v_b < v_j:
                    resultado = "¡Ganaste!"
                    creditos += apuesta_actual
                else:
                    resultado = "Empate."

            # Mostrar resultado y opciones para continuar o salir
            if resultado:
                dibujar_texto(resultado, 50, ALTO - 140, BLANCO)
                dibujar_texto("Presiona N para nueva ronda o Q para salir.", 50, ALTO - 100, BLANCO)

            pygame.display.flip()

            if resultado:
                esperando = True
                while esperando:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_n:
                                jugando = False
                                esperando = False
                            elif evento.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()
                    reloj.tick(30)
            else:
                reloj.tick(30)

if __name__ == "__main__":
    main()
