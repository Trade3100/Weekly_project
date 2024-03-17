import pygame
from pygame.locals import *
import sys, os
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
speed = 5
score = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self) :
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600) :
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 :
            if pressed_keys[K_LEFT] :
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH :
            if pressed_keys[K_RIGHT] :
                self.rect.move_ip(5, 0)



def main() :
    P1 = Player()
    E1 = Enemy()
    global speed

    #sprite groups
    enemies = pygame.sprite.Group()
    enemies.add(E1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(E1)
    all_sprites.add(P1)

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    while True :
        for event in pygame.event.get() :
            if event.type == INC_SPEED :
                speed += 0.2

            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        
        DISPLAYSURF.blit(background, (0,0))
        scores = font_small.render(str(score), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))

        for entity in all_sprites :
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(0.5)

            DISPLAYSURF.fill(RED)   
            DISPLAYSURF.blit(game_over, (50, 250))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()


        pygame.display.update()
        FramePerSec.tick(FPS)


main()





