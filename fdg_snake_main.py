import pygame
import sys
import time
from random import randint
import itertools

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANNG =(255, 152, 0)
RED = (255, 10, 0)
BLAU = (79, 204, 242)

STEP = 30
FPS = 8 # Кадры в секунду - Скорость
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 32

def load_image(sre: str, x: int, y: int):
    '''
    input:
    sre - путь к картинке
    x, y - кординаты
    '''
    image = pygame.image.load(sre).convert()
    image = pygame.transform.scale(image, (STEP, STEP))
    rect = image.get_rect(center=(x, y))
    trnsperent = image.get_at((0, 0))
    image.set_colorkey(trnsperent)
    return {'img':image, 'rct':rect}


class Game:
    '''
    класс игры, описывает основные параметры игры
    игровое поле, картинки, звуки, шрифт
    '''
    def __init__(self):
        self.FPS = FPS
        pygame.init()
        pygame.display.set_caption('My SNAKE for FDG')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.game_sound = pygame.mixer.Sound('./fdg/sound/gamesound.wav')
        self.poin_sound = pygame.mixer.Sound('./fdg/sound/point.wav')
        self.snake = Snake()
        self.game_play = True
        self.fdg_letters = [
            "./fdg/pics/f.jpg", 
            "./fdg/pics/d.jpg",
            "./fdg/pics/g.jpg",
        ]
        self.inf_fdg_letters = itertools.cycle(self.fdg_letters)
        letter_dct = load_image(next(self.inf_fdg_letters), 200, 200)
        self.leter_image, self.leter_rect = letter_dct['img'], letter_dct['rct']

    def main(self):
        '''главный метод/цикл игры'''
        self.game_sound.play(-1)
        while self.game_play:
            self.screen.fill(BLACK)
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
            self.text_on_screen(f"Ihre punkte:{self.score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200)
            self.gameover()
            pygame.display.update()
            self.clock.tick(self.FPS)
        self.text_on_screen('Spiel vorbei', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.update()
        time.sleep(3)

    def pickup(self):
        '''если попала голова на яблоко добавляет счёт и риcует новое яблыко'''
        if self.snake.snake_lst[0]['rct'].colliderect(self.leter_rect):
            self.leter_rect.x = self.snake.snake_lst[-1]['rct'].x
            self.leter_rect.y = self.snake.snake_lst[-1]['rct'].y
            self.snake.snake_lst.append({'img': self.leter_image.copy(), 'rct': self.leter_rect.copy()})
            x = randint(STEP, SCREEN_WIDTH-STEP)
            y = randint(STEP, SCREEN_HEIGHT-STEP)
            self.poin_sound.play()
            self.score = self.score + 10
            letter_dct = load_image(next(self.inf_fdg_letters), x, y)
            self.leter_image, self.leter_rect = letter_dct['img'], letter_dct['rct']

    def text_on_screen(self, text, x, y):
        '''выводит текст на экран'''
        self.text = self.font.render(text, True, BLAU)
        self.text_rect = self.text.get_rect(center=(x, y))
        self.screen.blit(self.text, self.text_rect)

    def gameover(self):
        '''устонавливает self.game_play = False если голова змеи
        попала на тело змеи.'''
        for segment in self.snake.snake_lst[1:]:
            if self.snake.snake_lst[0]['rct'].colliderect(segment['rct']):
                self.game_play = False

class Snake:
    '''
    класс змеи, хранит параметры змеи
    '''
    def __init__(self):
        self.STEP = STEP
        self.DIRECTION = [self.STEP, 0]
        start_x = SCREEN_WIDTH // 2 + STEP // 2
        start_y = SCREEN_HEIGHT // 2 + STEP // 2
        self.snake_lst = [load_image('./fdg/pics/head.png', start_x, start_y)]

    def move(self, keys):
        '''
        метод движения змеи, проверяет нажатие клавиш
        и меняет направление движения
        '''
        if keys[pygame.K_LEFT] and self.DIRECTION[0] == 0:
            self.DIRECTION = [-self.STEP, 0]
        elif keys[pygame.K_RIGHT] and self.DIRECTION[0] == 0:
            self.DIRECTION = [self.STEP, 0]
        elif keys[pygame.K_UP] and self.DIRECTION[1] == 0:
            self.DIRECTION = [0, -self.STEP]   
        elif keys[pygame.K_DOWN] and self.DIRECTION[1] == 0:
            self.DIRECTION = [0, +self.STEP]

        if self.snake_lst[0]['rct'].top < 0:
            self.snake_lst[0]['rct'].bottom = SCREEN_HEIGHT
        elif self.snake_lst[0]['rct'].bottom > SCREEN_HEIGHT:
            self.snake_lst[0]['rct'].top = 0
        elif self.snake_lst[0]['rct'].left < 0:
            self.snake_lst[0]['rct'].right = SCREEN_WIDTH
        elif self.snake_lst[0]['rct'].right > SCREEN_WIDTH:
            self.snake_lst[0]['rct'].left = 0

        for indx in range(len(self.snake_lst)-1, 0, -1):
            self.snake_lst[indx]['rct'].x = self.snake_lst[indx-1]['rct'].x
            self.snake_lst[indx]['rct'].y = self.snake_lst[indx-1]['rct'].y

        self.snake_lst[0]['rct'].move_ip(self.DIRECTION)

if __name__== "__main__":
    snake_game = Game()
    snake_game.main()