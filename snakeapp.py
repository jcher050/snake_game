from dis import dis
import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
Blue = (50, 153, 213)


dis_width = 600
dis_height = 400

dis = pygame.display.set_module((dis_width, dis_height))
pygame.display.set_caption('Snake Game In Python')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameloop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Lemgth_of_snake = 1
