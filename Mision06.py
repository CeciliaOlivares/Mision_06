#Cecilia Daniela Olivares Hernández, A01745727
#Misión 06. Crear un espirógrafo a partir de la formula

import pygame   # Librería de pygame
import random
import math
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

def generarColor():
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    return (rojo, verde, azul)

def dibujarEspirógrafo(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)


        for angulo in range(0, (360*(r // math.gcd(r, R))+1)):
            colorAleatorio = generarColor()
            a = math.radians(angulo)
            k = r/R
            x = int(R*((1-k)*math.cos(a)+l*k*math.cos(((1-k)/k)*a)))
            y = int(R*((1-k)*math.sin(a)-l*k*math.sin(((1-k)/k)*a)))
            pygame.draw.circle(ventana, colorAleatorio, (x+ANCHO//2,ALTO//2-y), 1)


        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()

def main():
    r = int(input("Inserta el valor del radio menor: "))
    R = int(input("Inserta el valor del radio mayor: "))
    l = float(input("Inserta el valor de l: "))
    dibujarEspirógrafo(r, R, l)

main()
