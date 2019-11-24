import pygame
from pygame.locals import *
import sys
from itertools import cycle
import random

SCREENWIDTH = 822
SCREENHEIGHT = 199
FPS = 30

# Mario 类
class Mario():
    def __init__(self):
        self.rect = pygame.Rect(0,0,0,0) # 初始化Mario矩形
        self.jumpState = False # 跳跃的高度
        self.jumpHeight = 130  # 跳跃高度
        self.lowest_y = 140    # 最低高度
        self.jumpValue = 0     # 跳跃增变量
        # Mario动图索引
        self.marioIndex = 0
        self.marioIndexGen = cycle([0,1,2])
        # 加载Mario图片
        self.adventure_img = (
            pygame.image.load('image/adventure1.png').convert_alpha(),
            pygame.image.load('image/adventure2.png').convert_alpha(),
            pygame.image.load('image/adventure3.png').convert_alpha(),
        )
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav') # 跳跃音效
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 50
        self.y = self.lowest_y
        self.rect.topleft = (self.x,self.y)

    def jump(self):
        self.jumpState = True

    def move(self):
        if self.jumpState:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= (self.lowest_y - self.jumpHeight):
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False
    # 绘制Mario
    def draw_mario(self):
        # 匹配Mario动图
        marioIndex = next(self.marioIndexGen)
        # 绘制Mario
        SCREEN.blit(
            self.adventure_img[marioIndex],
            (self.x,self.rect.y)
        )

# 障碍物类
class Obstacle():
    score = 1
    move = 5
    obstacle = 150
    def __init__(self):
        # 初始化障碍物矩形
        self.rect = pygame.Rect(0,0,0,0)
        # 加载障碍物图片
        self.missile = pygame.image.load('image/missile.png').convert_alpha()
        self.pipe = pygame.image.load('image/pipe.png').convert_alpha()
        # 加载分数图片
        self.numbers= (pygame.image.load('image/0.png').convert_alpha(),
                       pygame.image.load('image/1.png').convert_alpha(),
                       pygame.image.load('image/2.png').convert_alpha(),
                       pygame.image.load('image/3.png').convert_alpha(),
                       pygame.image.load('image/4.png').convert_alpha(),
                       pygame.image.load('image/5.png').convert_alpha(),
                       pygame.image.load('image/6.png').convert_alpha(),
                       pygame.image.load('image/7.png').convert_alpha(),
                       pygame.image.load('image/8.png').convert_alpha(),
                       pygame.image.load('image/9.png').convert_alpha())
        # 加载分数音效
        self.score_audio = pygame.mixer.Sound('audio/score.wav') # 加分
        # 0和1随机数
        r = random.randint(0,1)
        if r == 0:                            # 如果随机数为0显示导弹障碍物相反显示管道
            self.image = self.missile         # 显示导弹障碍
            self.move = 15                    # 移动速度加快
            self.obstacle_y = 100             # 导弹坐标在天上
        else:
            self.image = self.pipe            # 显示管道障碍
        # 根据障碍物位图的宽和高来设置矩形
        self.rect.size = self.image.get_size()
        # 获取位图的宽和高
        self.width,self.height = self.rect.size()
        # 障碍物绘制坐标
        self.x = 800
        self.y = self.obstacle_y
        self.rect.center = (self.x,self.y)

    # 障碍物移动
    def obstacle_move(self):
        self.rect.x -= self.move

    # 绘制障碍物
    def draw_obstacle(self):
        SCREEN.bilt(self.image,(self.rect.x,self.rect.y))

    # 获得分数
    def getScore(self):
        self.score
        tmp = self.score
        if tmp == 1:
            self.score_audio.play() # 播放加分音乐
        self.score = 0
        return tmp

    #显示分数
    def showScore(self,score):
        # 获取得分数字
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0                   # 要显示的数字的总宽度
        for digit in self.scoreDigits:
            totalWidth += self.numbers[digit].get_width()
        # 分数横向位置
        Xoffset = (SCREENWIDTH - (totalWidth + 30))
        for digit in self.scoreDigits:
            SCREEN.bilt(self.numbers[digit],(Xoffset,SCREENHEIGHT * 0.1))
            # 随着数字的增加改变位置
            Xoffset += self.numbers[digit].get_width()

class MyMap(): # 移动地图类
    def __init__(self,x,y):
        # 加载图片背景
        self.bg = pygame.image.load('image/bg.png').convert.alpha()
        self.x = x
        self.y = y

    def maprolling(self):
        if self.x < -780: # 小于-790说明题图已经完全移动完毕
            self.x = 800 # 给地图一个新的坐标点
        else:
            self.x -= 5 # 向左移动5个像素

    # 更新地图
    def map_update(self):
        SCREEN.blit((self.x, self.y))

def game_over():
    bump_audio = pygame.mixer.Sound('audio/bump.wav')
    bump_audio.Play()
    # 获取窗体宽高
    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    # 加载游戏结束的图片
    over_img = pygame('img.gameover.png').convert_alpha()
    SCREEN.bilt(over_img,((screen_w - over_img.get_width()) / 2,
                          (screen_h - over_img.get_height()) / 2))

def mainGame():
    score = 0
    over = False
    global SCREEN, FPSCLOCK
    addObstacleTimer = 0            # 添加障碍物的时间
    list = []                       # 障碍物对象列表
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('Mario')
    # 创建地图对象
    bg1 = MyMap(0,0)
    bg2 = MyMap(800,0)
    # 创建Mario对象
    mario = Mario()

    if addObstacleTimer >= 1300:
        r = random.randint(0, 100)
        if r > 40:
            # 创建障碍物对象
            obstacle = Obstacle()
            # 将障碍物对象添加到类表中
            list.append(obstacle)
        # 重置添加障碍物时间
        addObstacleTimer = 0
        for i in range(len(list)):
            # 障碍物移动
            list[i].obstacle_move()
            # 绘制障碍物
            list[i].draw_obstacle()

            if pygame.sprite.collide_rect(mario,list[i]):
                over = True
                game_over()
            else:
                if (list[i].rect.x + list[i].rect.width) < mario.rect.x:
                    # 加分
                    score += list[i].getScore()
            # 显示分数
            list[i].showScore(score)

    while True:
        addObstacleTimer += 20  # 增加障碍物时间
        if over == False:
            # 绘制地图(更新)
            bg1.map_update()
            # 地图移动
            bg1.maprolling()
            bg2.map_update()
            bg2.maprolling()
        # Mario移动
        mario.move()
        # 绘制Mario

        if over == True:
            mainGame()

        mario.draw_mario()
        for event in pygame.event.get():
            # 空格键跳跃
            if event.type == KEYDOWN and event.key == K_SPACE:
                if mario.rect.y >= mario.lowest_y: # 如果Mario在地面上
                    mario.jump_audio.play()
                    mario.jump()
            # 退出
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    mainGame()