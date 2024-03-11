# استيراد مكتبة Pygame وبعض الوحدات الأخرى
import pygame
import random
import math
import time

# تهيئة Pygame
pygame.init()

# إنشاء شاشة اللعبة بحجم 800 × 600 بكسل ولون أسود
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((0, 0, 0))


# تحديد بعض الثوابت والمتغيرات التي سنستخدمها في اللعبة

# الألوان
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# الأشكال
CIRCLE = 0
SQUARE = 1
TRIANGLE = 2

# الأحجام
PLAYER_SIZE = 50
OBSTACLE_SIZE = 30
POINT_SIZE = 20

# المواقع
PLAYER_X = screen_width // 2
PLAYER_Y = screen_height - PLAYER_SIZE
OBSTACLE_X = random.randint(0, screen_width - OBSTACLE_SIZE)
OBSTACLE_Y = 0
POINT_X = random.randint(0, screen_width - POINT_SIZE)
POINT_Y = 0

# السرعات
PLAYER_SPEED = 10
OBSTACLE_SPEED = 5
POINT_SPEED = 3

# الاتجاهات
LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1

# الدرجة والوقت
score = 0
time_limit = 60
start_time = time.time()
