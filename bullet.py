import pygame#导入pygame模块
class Bullet1(pygame.sprite.Sprite):#定义Bullet1的子类，它会继承父类pygame.sprite.Sprite————已在pygame被定于
    def __init__(self,position):#初始化
        pygame.sprite.Sprite.__init__(self)#初始化Sprite模块
        self.image = pygame.image.load("images/bullet111.png").convert_alpha()#调用函数pygame.image.load根据路径提供的照片付给变量self.image。
        self.rect = self.image.get_rect()#把照片中的属性赋给变量self.rect
        self.rect.left,self.rect.top = position#初始化子弹的位置
        self.speed = 12#速度12
        self.active = True#子弹刚出现时能动的
        self.mask = pygame.mask.from_surface(self.image)# 从指定 Surface对象中返回一个Mask
    def move(self):
        self.rect.top -= self.speed#子弹的移动，修改TOP坐标，具体参考坐标系以及运算符 c -= a 等于 c = c - a, a不变，但是c越来越小,就是top逐渐靠近0
        if self.rect.top < 0:#如果top出现小于0时，说明子弹飞出游戏窗口
            self.active = False#此时设置子弹 死掉
    def reset(self,position):#子弹复活
        self.rect.left,self.rect.top = position#初始化子弹的位置
        self.active = True#子弹复活后 活的

class Bullet2(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet222.png")
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = 14
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False
    def reset(self,position):
        self.rect.left,self.rect.top = position
        self.active = True

class Bullet3(pygame.sprite.Sprite):
    def __init__(self,position):
        self.image = pygame.image.load("images/bomb and bullet3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = 18
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False
    def reset(self,position):
        self.rect.left,self.rect.top = position
        self.active = True