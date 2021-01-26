import pygame#导入pygame模块    
from random import*#导入random模块，random模块用于生成随机数
class SmallEnemy(pygame.sprite.Sprite):#定义一个SmallEnemy的子类继承父类pygame.sprite.Sprite
    def __init__(self,bg_size):#添加__init__方法，那么在创建类的实例的时候，实例会自动调用这个方法，一般用来对实例的属性进行初使化
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy11.png").convert_alpha()#调用函数pygame.image.load以及路径把照片赋给变量image
        self.destroy_images = []#创建一个空列表
        self.destroy_images.extend([\
            pygame.image.load("images/enemy1_down11.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down22.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down33.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down44.png").convert_alpha() \
            ])## extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中
        self.rect = self.image.get_rect()#把图片属性赋给变量rect
        self.width,self.height = bg_size[0],bg_size[1]#把传进来的背景图片的宽和高分别给这里面width和height,含义是指飞机可以移动的宽和高，因为只有本地化了，在其他方法里才可以直接用到这两个属性，比如下面的方法需要来判断是否大于这个width或者这个height,大于就表示超出了游戏窗口
        self.speed = 2
        self.active = True#初始化时活的
        self.rect.left,self.rect.top = \
            randint(0,self.width - self.rect.width),\
            randint(-5 * self.height,0)#敌机初始化出现的位置。X轴坐标 = 0到(窗口宽度-敌机1宽度) Y轴 = 窗口看不见部分到0
        self.mask = pygame.mask.from_surface(self.image)## 从指定 Surface对象中返回一个Mask
    def move(self,flozen):#多了一个参数冻结
        if not flozen:#如果没有被冻结
            if self.rect.top < self.height:#只要敌机Y坐标处于窗口高度区间
                self.rect.top += self.speed#那么 c = c + a  ,top会一直变大，直到碰到窗口边缘
            else:#越过就会复活重来
                self.reset()
    def reset(self):#复活
        self.active = True#此时活的
        self.rect.left,self.rect.top = \
            randint(0,self.width - self.rect.width),\
            randint(-5 * self.height,0)#复活的位置
        
class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/enemy22.png').convert_alpha()
        self.image_hit = pygame.image.load('images/enemy22_hit.png').convert_alpha()#因为敌机2血多，多出一个被击中时特效照片
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy2_down11.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down22.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down33.png").convert_alpha(), \
            pygame.image.load("images/enemy2_down44.png").convert_alpha() \
            ])
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left,self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-10 * self.height,-self.height)#区间
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
        self.hit = False#刚开始，没被打中，被击中特效照片不触发
    
    def move(self,flozen):
        if not flozen:
            if self.rect.top < self.height:
                self.rect.top += self.speed
            else:
                self.reset()
    
    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy#复活时调用类MidEnemy中的energy，把生命值重新赋给敌机2
        self.rect.left,self.rect.top = \
            randint(0,self.width - self.rect.width),\
            randint(-10 * self.height,-self.height)
    
class BigEnemy(pygame.sprite.Sprite):
    energy = 20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load('images/enemy3_n21.png').convert_alpha()
        self.image2 = pygame.image.load('images/enemy3_n22.png').convert_alpha()
        self.image_hit = pygame.image.load('images/enemy33_hit.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy3_down11.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down22.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down33.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down44.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down55.png").convert_alpha(), \
            pygame.image.load("images/enemy3_down66.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left,self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-15 * self.height,-5 * self.height)#random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False
    
    def move(self,flozen):
        if not flozen:
            if self.rect.top < self.height:
                self.rect.top += self.speed
            else:
                self.reset()
    
    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left,self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-15 * self.height,-5 * self.height)
        