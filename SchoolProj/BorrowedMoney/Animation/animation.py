import os
import asyncio

from screeninfo import get_monitors
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep



x = [
"B",
"y",
" ",
"C",
"o",
"d",
"e",
"r",
"X..\n",
]
l_l = ...
def animation():
    count = 0
    count1 = 0
    for i in x:
        if count%6==0:
            count=0
        print(f"\033[3{count};1m{i}\033[0m", end='', flush=1)
        sleep(.05)
        count+=1
    sleep(1.5)
    os.system("CLS||clear")

class Loader:
    def __init__(self, desc="\nLoading...", end="", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = [f'⢿', "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()

def loader_anim():
    with Loader("\033[32;1mStarting Script...\033[0m"):
        for i in range(10):
            sleep(0.25)

    loader = Loader("\033[35;1mLoading modules..\033[0m").start()
    for i in range(10):
        sleep(0.25)
    loader.stop()

animation()
loader_anim()
import os
from random import choice, randrange
import pygame as pg

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height
ALPHA = 100

pg.init()

screen = pg.display.set_mode(RES)
surface = pg.Surface(RES, pg.SRCALPHA)
surface.set_alpha(ALPHA)
clock = pg.time.Clock()

katakana_chars = ['゠', 'ァ', 'ア', 'ィ', 'イ', 'ゥ', 'ウ', 'ェ', 'エ', 'ォ', 'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ', 'ケ', 'ゲ', 'コ',
                  'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ', 'ゼ', 'ソ', 'ゾ', 'タ', 'ダ', 'チ', 'ヂ', 'ッ', 'ツ', 'ヅ', 'テ', 'デ',
                  'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ', 'フ', 'ブ', 'プ', 'ヘ', 'ベ', 'ペ', 'ホ',
                  'ボ', 'ポ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ャ', 'ヤ', 'ュ', 'ユ', 'ョ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ヮ', 'ワ',
                  'ヰ', 'ヱ', 'ヲ', 'ン', 'ヴ', 'ヵ', 'ヶ', 'ヷ', 'ヸ', 'ヹ', 'ヺ', '・', 'ー', 'ヽ', 'ヾ', 'ヿ']


class Symbol:
    def __init__(self, x, y, font_size, speed):
        self.x = x
        self.y = y
        self.y0 = - font_size
        self.font_size = font_size
        self.speed = speed
        self.char_change_speed = randrange(20, 40)
        self.value = choice(katakana_chars)
        self.font_increase = 0

    def draw(self, position):
        self.font_increase_speed = int(self.y / 80)
        self.font_increase = self.font_size + self.font_increase_speed if 0 < self.y < HEIGHT else 0
        font = pg.font.Font("BorrowedMoney/Animation/Fonts/MS Mincho.ttf", self.font_increase)
        frames = pg.time.get_ticks()
        if not frames % self.char_change_speed:
            self.value = choice(katakana_chars)

        self.y = self.y + self.speed if self.y < HEIGHT else self.y0

        if position < 8:
            self.char = font.render(self.value, True, (255 - 32 * position, 255, 255 - 32 * position))
        if position >= 8:
            self.char = font.render(self.value, True, (0, 255 - 22 * (position - 8), 0))

        screen.blit(self.char, (self.x, self.y))


class SymbolColumn:
    def __init__(self, x, y, font_size):
        self.column_height = randrange(5, 20)
        self.speed = randrange(5, 20)
        self.font_size = font_size
        self.symbols = [Symbol(x=x, y=i, font_size=self.font_size, speed=self.speed) for i in
                        range(y, y - (self.font_size + 10) * self.column_height, -(self.font_size + 10))]

    def draw(self):
        [symbol.draw(position=i) for i, symbol in enumerate(self.symbols)]


symbol_columns = [SymbolColumn(x=i, y=0, font_size=20) for i in range(100, WIDTH - 100, 200)]


def matrix():
    running = 0
    while running<=150:
        screen.blit(surface, (0, 0))
        surface.fill(pg.Color('black'))

        [symbol_column.draw() for symbol_column in symbol_columns]

        [exit() for event in pg.event.get() if event.type == pg.QUIT]

        pg.display.update()

        clock.tick(60)
        running+=1
    print("\033[32;1;2mCurrent Time:\033[0m")
matrix()

import pygame
from math import pi, cos, sin
import datetime

WIDTH, HEIGHT = get_monitors()[0].width, get_monitors()[0].height

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Clock")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def numbers(number, size, color, position):
    font = pygame.font.SysFont("DS-Digital", size, True, False)
    text = font.render(number, True, color)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return int(x + WIDTH / 2 + 175), int(-(y - HEIGHT / 2))


def clock_anim():
    run = 0
    while run<=300:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        second = current_time.strftime('%S')
        minute = current_time.strftime('%M')
        hour = current_time.strftime('%I')
        am_pm = current_time.strftime('%p')
        weekday = current_time.strftime('%A')

        screen.fill(BLACK)

        numbers(f"{hour}:{minute}", 200, WHITE, (WIDTH / 2 - 100, HEIGHT / 2))
        numbers(second, 60, RED, (WIDTH / 2 + 175, HEIGHT / 2))
        numbers(am_pm, 60, WHITE, (WIDTH / 2 + 260, HEIGHT / 2 - 45))
        numbers(weekday, 60, WHITE, (WIDTH / 2 + 300, HEIGHT / 2 + 44))

        r = 45
        theta = int(second) * 360 / 60

        pygame.draw.circle(screen, WHITE, (int(WIDTH / 2 + 175), int(HEIGHT / 2)), r, 1)
        pygame.draw.circle(screen, RED, polar_to_cartesian(r, theta), 8)

        pygame.display.update()

        clock.tick(FPS)
        run+=1

    pygame.quit()

clock_anim()