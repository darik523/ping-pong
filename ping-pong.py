from pygame import *
from time import time as timer
font.init()
#display
win_width = 600
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('Hello')
bg = transform.scale(image.load('backdrop.jpg'), (win_width, win_height))
#display

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 350:
            self.rect.x += self.speed
        
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 350:
            self.rect.x += self.speed


font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 lose!', True, (76, 0, 51))

player_1 = Player('platform.png', 5, win_height - 100, 250, 65, 6)
player_2 = Player('platform.png', 5, win_height - 660, 250, 65, 6)
ball = Player('ballp.png', 5, win_height - 0, 250, 65, 5)


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.blit(bg,(0, 0))
        
        player_1.reset()
        player_1.update_l()

        player_2.reset()
        player_2.update_r()

        ball.reset()
        
        

    display.update()
