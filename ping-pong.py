from pygame import*

#игровая сцена
bg = (34, 153, 153)
win_wigth = 450
win_height = 600
window = display.set_mode((400, 470))
window.fill(bg)
display.set_caption('ping-pong')

clock = time.Clock()
FPS = 60
game = True

#игровой цикл:
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
