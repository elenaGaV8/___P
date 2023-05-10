from pygame import *
mixer.init()
font.init()
from time import time as timer
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)
window = display.set_mode((700, 500))
display.set_caption('')
window.fill(LIGHT_BLUE)


clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed, size1, size2):
        super(). __init__()
        self.image = transform.scale(image.load(image1), (size1,size2))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 25:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 25:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(30,650)
            self.rect.x += self.speed
player_1 = Player('левая платформа.png', 50, 300, 4, 50, 150)
player_2 = Player('правая платформа.png', 550, 300, 4, 50, 150)
ball = Enemy('ball.png', 100, 100, 4, 50, 50)
speed_x = 3
speed_y =3
game = True
FPS = 60
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            shot = False
            if i.key == K_ESCAPE:
                finish = True
                pause = font.SysFont('Arial', 30).render('Хотите продолжить? Нажмите R', 1 , (255, 255, 255))
                window.blit(pause, (150,250))
            if i.key == K_r:
                finish = False  
                    
                               
    if finish != True:
        window.fill(LIGHT_BLUE)
        player_1.update_l()
        player_1.reset()
        player_2.reset()
        player_2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y*=-1
        if sprite.collide_rect(ball, player_1) or sprite.collide_rect(ball, player_2):
            speed_x *= -1
        #ball.update()

        ball.reset()
        if ball.rect.x > 650:
            finish = True
            win1 = font.SysFont('Arial', 30).render('Игрок 1 выиграл!!!', 1 , (255, 255, 255))
            window.blit(win1, (100, 100))
        if ball.rect.x < 0:
            finish = True
            win2 = font.SysFont('Arial', 30).render('Игрок 2 выиграл!!!', 1 , (255, 255, 255))
            window.blit(win2, (100, 100))    
    
    
    clock.tick(60)
    display.update()
    

display.update()
