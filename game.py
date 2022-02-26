import pygame as pg
pg.init()

class Ball:
    def __init__(self, x, y, color = (255, 255, 255), radio = 10):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.dx = 1
        self.dy = 1

    def moveball(self, limitRight, limitInf):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.radio or self.x >= limitRight - self.radio:
            self.dx *= -1
        if self.y <= self.radio or self.y >= limitInf - self.radio:
            self.dy *= -1

    def drawball(self, surface):
            pg.draw.circle(surface, self.color, (self.x, self.y), self.radio)

class Game:
    def __init__(self, width=600, height=800):
        self.screen = pg.display.set_mode((width, height))
        self.ball = Ball(width//2, height//2, (255, 255, 0))


    def bucle_ppal(self):
        game_over = False

        while not game_over:

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    game_over = True
            
            self.ball.moveball(self.screen.get_width(), self.screen.get_height())
            self.screen.fill((255, 0, 0))
            self.ball.drawball(self.screen)

            pg.display.flip()

if __name__== '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()
