import pygame
import sys
import time
from random import randint
import itertools

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANNG =(255, 152, 0)
RED = (255, 10, 0)

def load_image(sre, x, y):
    image = pygame.image.load(sre).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect = image.get_rect(center=(x, y))
    trnsperent = image.get_at((0, 0))
    image.set_colorkey(trnsperent)
    return {'img':image, 'rct':rect}


class Game:
    def __init__(self):
        self.FPS = 8
        pygame.init()
        pygame.display.set_caption('My SNAKE for Edlach')
        self.screen = pygame.display.set_mode((1500, 800))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.font = pygame.font.SysFont(None, 32)
        self.game_sound = pygame.mixer.Sound('.\fdg\sound\gamesound.wav')
        self.poin_sound = pygame.mixer.Sound('./fdg/sound/point.wav')
        self.snake = Snake()
        self.game_play = True
        self.edlach_letters = [
            "./fdg/pics/f.png", 
            "./fdg/pics/d.png",
            "./fdg/pics/g.png",
        ]
        self.inf_edlach_letters = itertools.cycle(self.edlach_letters)
        letter_dct = load_image(next(self.inf_edlach_letters), 200, 200)
        self.leter_image, self.leter_rect = letter_dct['img'], letter_dct['rct']

    def main(self):
        self.game_sound.play(-1)
        while self.game_play:
            self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.leter_image, self.leter_rect)
            for segmnt in self.snake.snake_lst:
                self.screen.blit(segmnt['img'], segmnt['rct'])
            keys = pygame.key.get_pressed()
            self.pickup()
            self.snake.move(keys)
            self.text_on_screen(f"Ihre punkte:{self.score}", 400, 500)
            self.gameover()
            pygame.display.update()
            self.clock.tick(self.FPS)
        self.text_on_screen('Spiel vorbei', 400, 300)
        pygame.display.update()
        time.sleep(3)

    def pickup(self):
        '''если попала голова на яблоко добавляет счёт и риcует новое яблыко'''
        if self.snake.snake_lst[0]['rct'].colliderect(self.leter_rect):
            self.leter_rect.x = self.snake.snake_lst[-1]['rct'].x
            self.leter_rect.y = self.snake.snake_lst[-1]['rct'].y
            self.snake.snake_lst.append({'img': self.leter_image.copy(), 'rct': self.leter_rect.copy()})
            x = randint(40, 760)
            y = randint(30, 560)
            self.score = self.score + 10
            letter_dct = load_image(next(self.inf_edlach_letters), x, y)
            self.leter_image, self.leter_rect = letter_dct['img'], letter_dct['rct']

    def text_on_screen(self, text, x, y):
        '''выводит счет игры на экран'''
        self.text = self.font.render(text, True, ORANNG)
        self.text_rect = self.text.get_rect(center=(x, y))
        self.screen.blit(self.text, self.text_rect)

    def gameover(self):
        '''устонавливает self.game_play = False'''
        for segment in self.snake.snake_lst[1:]:
            if self.snake.snake_lst[0]['rct'].colliderect(segment['rct']):
                self.game_play = False

class Snake:
    def __init__(self):
        self.STEP = 30
        self.DIRECTION = [self.STEP, 0]
        self.x_x = 400
        self.y = 300
        self.snake_lst = [load_image('./Edlach/pics/head.png', self.x_x, self.y)]

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.DIRECTION[0] == 0:
            self.DIRECTION = [-self.STEP, 0]
        elif keys[pygame.K_RIGHT] and self.DIRECTION[0] == 0:
            self.DIRECTION = [self.STEP, 0]
        elif keys[pygame.K_UP] and self.DIRECTION[1] == 0:
            self.DIRECTION = [0, -self.STEP]   
        elif keys[pygame.K_DOWN] and self.DIRECTION[1] == 0:
            self.DIRECTION = [0, +self.STEP]

        if self.snake_lst[0]['rct'].bottom < 0:
            self.snake_lst[0]['rct'].bottom = 600
        elif self.snake_lst[0]['rct'].top > 600:
            self.snake_lst[0]['rct'].top = 0
        elif self.snake_lst[0]['rct'].right < 0:
            self.snake_lst[0]['rct'].right = 800
        elif self.snake_lst[0]['rct'].left > 800:
            self.snake_lst[0]['rct'].left = 0

        for indx in range(len(self.snake_lst)-1, 0, -1):
            self.snake_lst[indx]['rct'].x = self.snake_lst[indx-1]['rct'].x
            self.snake_lst[indx]['rct'].y = self.snake_lst[indx-1]['rct'].y

        self.snake_lst[0]['rct'].move_ip(self.DIRECTION)

if __name__== "__main__":
    snake_game = Game()
    snake_game.main()