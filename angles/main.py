import pygame, math
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

posx = 400
posy = 300

base = 0
per = 0
hyp = 0
angle = 0
ang = 0


def find_angle(mouse_pos):
    global per, base, angle, hyp, ang, angle
    base = (posx - mouse_pos[0])
    per = (posy - mouse_pos[1])
    hyp = math.sqrt(base**2 + per**2)
    try:
        ratio = per / base
        angle = math.atan(ratio)
    except ZeroDivisionError:
        if per > 0:
            angle = math.pi/2
    if base < 0 and per >= 0:
        angle = abs(angle)
    elif base > 0 and per >= 0:
        angle = math.pi - angle
    elif base > 0 and per < 0:
        angle = math.pi + abs(angle)
    elif base < 0 and per < 0:
        angle = math.pi*2 - angle
    ang = math.degrees(angle)


font = pygame.font.Font(None, 30)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('black')
    mouse_pos = pygame.mouse.get_pos()
    find_angle(mouse_pos)
    txt = font.render(f'angle:{round(ang)} ', True, (255, 255, 255))
    txt_rect = txt.get_rect(center=(230, 50))
    screen.blit(txt, txt_rect)

    pygame.draw.line(screen, 'white', (posx, posy), mouse_pos)
    pygame.draw.line(screen, 'white', mouse_pos, (mouse_pos[0], posy))
    pygame.draw.line(screen, 'white',(posx, posy), (mouse_pos[0], posy))


    clock.tick(60)
    pygame.display.flip()
