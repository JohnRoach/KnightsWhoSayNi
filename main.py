import sys
import pygame
import knightmove
import os


pygame.init()

square_list = []
line_list = []
i = 0
j = 1


def make_gif():
    os.system("convert   -delay 40   -loop 0   Screenshots/screenshot*.png   knights_tour.gif")


def get_moves(start_move):
    return knightmove.knights_tour(start_move, 8)


def scratch(move):
    move_x, move_y = move
    x = int(move_x) * 50
    y = int(move_y) * 50
    line_list.append([x+25, y+25])
    square_list.append([x, y])
    for index in range(len(square_list)):
        screen.blit(square, square_list[index])


def draw_line():
    for index in range(len(line_list)-1):
        pygame.draw.line(screen, black, (line_list[index]), (line_list[index+1]), 2)


def draw_dot():
    return pygame.draw.circle(screen, red, (line_list[i]), 3, 0)


def screenshot():
    if j <= 9:
        c = "0"+str(j)
    else:
        c = j
    pygame.image.save(screen, "Screenshots/screenshot"+str(c)+".png")


size = width, height = 400, 400
white = 255, 255, 255
black = 0, 0, 0, 0
red = 255, 0, 0

screen = pygame.display.set_mode(size)
square = pygame.image.load("Untitled.png")

start = raw_input("Enter the start position:")
moves = get_moves(start)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(white)
    pygame.draw.line(screen, black, (0, 50), (400, 50), 3)
    pygame.draw.line(screen, black, (0, 100), (400, 100), 3)
    pygame.draw.line(screen, black, (0, 150), (400, 150), 3)
    pygame.draw.line(screen, black, (0, 200), (400, 200), 3)
    pygame.draw.line(screen, black, (0, 250), (400, 250), 3)
    pygame.draw.line(screen, black, (0, 300), (400, 300), 3)
    pygame.draw.line(screen, black, (0, 350), (400, 350), 3)

    pygame.draw.line(screen, black, (50, 0), (50, 400), 3)
    pygame.draw.line(screen, black, (100, 0), (100, 400), 3)
    pygame.draw.line(screen, black, (150, 0), (150, 400), 3)
    pygame.draw.line(screen, black, (200, 0), (200, 400), 3)
    pygame.draw.line(screen, black, (250, 0), (250, 400), 3)
    pygame.draw.line(screen, black, (300, 0), (300, 400), 3)
    pygame.draw.line(screen, black, (350, 0), (350, 400), 3)

    scratch(moves[i])
    draw_line()
    draw_dot()
    screenshot()
    i += 1
    j += 1
    pygame.display.flip()
    if i == 64:
        make_gif()
        print "GIF was created"
        break

