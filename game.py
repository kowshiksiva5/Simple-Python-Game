import random
import math
import time
from config import *


start = pygame.time.get_ticks()
pygame.init()

font = pygame.font.Font('freesansbold.ttf', 50)

# game title
pygame.display.set_caption('my game')

# images declaration
player1Img = pygame.image.load('boy1.png')
player2Img = pygame.image.load('boy2.png')
movingobsImg = pygame.image.load('shark.png')
fixedobstacleImg = pygame.image.load('ship.png')

# x coordinates for obstacles
for i in range(0, 10):
    a[i] = (random.randrange(size, display_width-size))

for j in range(0, 4):
    b[j] = (random.randrange(size, display_width-size))


# class for obstacles
class GameObject:
    def __init__(self, image, speed, xcordinate, ycordinate):
        self.speed = speed
        self.image = image
        self.Xcordinate = xcordinate
        self.Ycordinate = ycordinate
        gameDisplay.blit(self.image, (self.Xcordinate, self.Ycordinate))

    # function for movement
    def move(self):
        self.Xcordinate = (self.Xcordinate + self.speed)
        if self.Xcordinate > display_width:
            self.Xcordinate = 0


class GameObject2:
    def __init__(self, image, speed, xcordinate, ycordinate):
        self.speed = speed
        self.image = image
        self.Xcordinate = xcordinate
        self.Ycordinate = ycordinate
        gameDisplay.blit(self.image, (self.Xcordinate, self.Ycordinate))

    # function for movement
    def move(self):
        self.Xcordinate = (self.Xcordinate + self.speed)
        if self.Xcordinate > display_width:
            self.Xcordinate = 0


obstacles2 = []
fixedobstacles2 = []
obstacles = []
fixedobstacles = []


def player1(x5, y5):
    gameDisplay.blit(player1Img, (x5, y5))


def player2(x6, y6):
    gameDisplay.blit(player2Img, (x6, y6))


def text_objects(text, fonti):
    text_surface = fonti.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 50)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(1)


def message_display4(text):
    large_text = pygame.font.Font('freesansbold.ttf', 50)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2 + 100))
    gameDisplay.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(1)


def message_display1(x, y, text):
    val = font.render("score:" + str(text), True, (0, 0, 0))
    gameDisplay.blit(val, (x, y))


def message_display_time(x, y, text):
    val = font.render("Time:" + str(text), True, (0, 0, 0))
    gameDisplay.blit(val, (x, y))


def message_display2(x, y, text):
    val = font.render("" + str(text), True, (0, 0, 0))
    gameDisplay.blit(val, (x, y))


def movingobs(x7, y7):
    gameDisplay.blit(movingobsImg, (x7, y7))


def convertmillis(millis):
    seconds = (millis / 1000) % 60
    return int(seconds)


def collisionof(x1, y1, x2, y2):
    q1 = math.pow(x1 - x2, 2)
    q2 = math.pow(y1 - y2, 2)
    dist = math.sqrt(q1 + q2)
    if y1 < 2 * size:
        message_display('Sucess')
        obstacles2.clear()
        obstacles.clear()
        fixedobstacles.clear()
        fixedobstacles2.clear()
        game_loop2()
    if dist < size:
        message_display('Crash')
        obstacles2.clear()
        obstacles.clear()
        fixedobstacles.clear()
        fixedobstacles2.clear()
        game_loop2()


def collisionof2(x1, y1, x2, y2):
    q1 = math.pow(x1 - x2, 2)
    q2 = math.pow(y1 - y2, 2)
    dist = math.sqrt(q1 + q2)

    if y1 == display_height - 48:
        message_display('Sucess')
        whowin(score[0], score[1])
    if dist < size:
        message_display('Crash')
        whowin(score[0], score[1])


def whowin(w1, w2):
    for ss in range(16):
        c[ss] = 0

    c[4] = 1
    c[7] = 1
    c[10] = 1
    c[13] = 1
    for ss in range(2, 16):
        d[ss] = 0
    d[5] = 1
    d[8] = 1
    d[11] = 1
    d[14] = 1
    compare[0] = score[0]
    compare[1] = score[1]
    score[0] = 0
    score[1] = 0
    var[0] = 1
    var[1] = 1
    obstacles2.clear()
    obstacles.clear()
    fixedobstacles.clear()
    fixedobstacles2.clear()
    print(moving[0], moving[1])
    if w1 > w2:
        message_display4('player1 wins')
        temp = moving[0]
        temp = temp + 1
        moving[0] = temp
    if w1 < w2:
        message_display4('player2wins')
        temp = moving[1]
        temp = temp + 1
        moving[1] = temp
    print(moving[0], moving[1])
    if w1 == w2:
        if time_arr[0] > time_arr[1]:
            message_display4('player1 wins')
            temp = moving[0]
            temp = temp + 10
            moving[0] = temp
        if time_arr[1] > time_arr[0]:
            message_display4('player2wins')
            temp = moving[1]
            temp = temp + 1
            moving[1] = temp
    gameDisplay.fill(blue)
    message_display("Click R to continue or Q to quit")
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_r:
                    game_loop()


def game_loop():
    x = 0
    y = display_height - size
    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x > 0:
                    x = x - size
                if event.key == pygame.K_RIGHT and x < display_width - size + 2:
                    x = x + size
                if event.key == pygame.K_UP and y > 0:
                    y = y - size
                if event.key == pygame.K_DOWN and y < display_height - size + 2:
                    y = y + size

        gameDisplay.fill(blue)

        # For land on sea
        pygame.draw.rect(gameDisplay, grey, (0, size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 5 * size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 8 * size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 11 * size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 14 * size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 16 * size, 1000, 50))

        time_arr[0] = pygame.time.get_ticks()
        end = convertmillis(time_arr[0])
        time_arr[0] = end
        a2 = end - time_arr[1]
        time_arr1[0] = a2
        message_display_time(300, 0, a2)

        if var[0] == 1:
            for x in range(0, 10):
                k = GameObject(movingobsImg, moving[0], a[x], arr[x])
                print(moving[0], moving[1])

                obstacles.append(k)
            for x in range(0, 4):
                o = GameObject(fixedobstacleImg, 0, b[x], brr[x])
                fixedobstacles.append(o)
                var[0] = 0

        for kk in obstacles:
            kk.move()
            gameDisplay.blit(kk.image, (kk.Xcordinate, kk.Ycordinate))
            collisionof(x, y, kk.Xcordinate, kk.Ycordinate)

        for oo in fixedobstacles:
            gameDisplay.blit(oo.image, (oo.Xcordinate, oo.Ycordinate))
            for i1 in range(0, 4):
                collisionof(x, y, b[i1], brr[i1])

        for r in range(16):
            if y < r * size and c[r - 1] == 0:
                score[0] += 10
                c[r - 1] = 3

            if r * size > y and c[r - 1] == 1:
                score[0] += 5
                c[r - 1] = 3

            if y < 1 * size - 1:
                score[0] += -10

        # to display player 1 image
        player2(display_width - size, size)
        player1(x, y)

        message_display1(0, 0, score[0])
        message_display2(display_width / 2 - 100, 16 * 48, 'Start')
        message_display2(display_width / 2 - 100, size, 'End')
        pygame.display.update()


def game_loop2():
    x = display_width - 50
    y = size
    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x > 0:
                    x = x - size
                if event.key == pygame.K_d and x < display_width - size:
                    x = x + size
                if event.key == pygame.K_w and y > 0:
                    y = y - size
                if event.key == pygame.K_s and y < display_height - size:
                    y = y + size

        gameDisplay.fill(blue)

        # For land on sea
        pygame.draw.rect(gameDisplay, grey, (0, size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 5 * size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 8 * size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 11 * size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 14 * size, 1000, 50))
        pygame.draw.rect(gameDisplay, grey, (0, 16 * size, 1000, 50))

        time_arr[1] = pygame.time.get_ticks()
        end = convertmillis(time_arr[1])
        time_arr[1] = end
        a2 = end - time_arr[0]
        time_arr1[1] = a2
        message_display_time(300, 0, a2)

        # for obstacles
        if var[1] == 1:
            print(var[0], var[1])
            for x in range(0, 10):
                k = GameObject(movingobsImg, moving[0], a[x], arr[x])
                print(moving[0], moving[1])

                obstacles2.append(k)
            for x in range(0, 4):
                o = GameObject(fixedobstacleImg, 0, b[x], brr[x])
                fixedobstacles2.append(o)
                var[1] = 0

        for kk in obstacles2:
            kk.move()
            gameDisplay.blit(kk.image, (kk.Xcordinate, kk.Ycordinate))
            collisionof2(x, y, kk.Xcordinate, kk.Ycordinate)

        for oo in fixedobstacles2:
            gameDisplay.blit(oo.image, (oo.Xcordinate, oo.Ycordinate))
            for i1 in range(0, 4):
                collisionof2(x, y, b[i1], brr[i1])

        for r in range(2, 16):
            if y > r * size and d[r] == 0:
                score[1] += 10
                d[r] = 4

            if r * size < y and d[r] == 1:
                score[1] += 5
                d[r] = 4

            if y < 15 * size + 1:
                score[1] += 0

        # to display player 1 image
        player2(x, y)
        player1(0, display_height - size)

        message_display1(0, 0, score[1])
        message_display2(display_width / 2 - 100, 16 * 48, 'End')
        message_display2(display_width / 2 - 100, size, 'Start')
        pygame.display.update()


game_loop()
pygame.quit()
quit()
