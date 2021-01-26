import pygame#导入pygame模块
class MyPlane(pygame.sprite.Sprite):#定义一个子类名为MyPlane继承父类Sprite
    def __init__(self,bg_size):#初始化
        pygame.sprite.Sprite.__init__(self)#初始化Sprite
        self.image1 = pygame.image.load("images/meme1.png")#两张飞机飞行时引擎棋气浪波动照片
        self.image2 = pygame.image.load("images/meme2.png")#分别赋给image1和2
        self.destroy_images = []#创建一个飞机炸毁图片列表
        self.destroy_images.extend([\
            pygame.image.load("images/me_destroy_11.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_22.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_33.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_44.png").convert_alpha() \
            ])# extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中
        self.rect = self.image1.get_rect()#把meme1.png赋给变量rect
        self.width,self.height = bg_size[0],bg_size[1]#把传进来的背景图片的宽和高分别给这里面width和height,含义是指飞机可以移动的宽和高，因为只有本地化了，在其他方法里才可以直接用到这两个属性，比如下面的方法需要来判断是否大于这个width或者这个height,大于就表示超出了游戏窗口
        #下面是玩家飞机初始化出现的位置
        self.rect.left,self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        #（游戏窗口宽度 - 飞机属性宽度）÷2     （游戏窗口高度 - 飞机属性高度）-60    这两个值是飞机属性的左上角坐标，一是飞机初始化出现的X轴坐标，二是飞机出现的Y轴坐标， -60 是为了让下面的飞机生命值对象和炸弹剩余值对象不与飞机相碰撞，具体对照坐标轴图例
        self.speed = 10#设定飞机移动速度为10    
        self.active = True#此时飞机是活的
        self.invincible = False#并不处于无敌状态
        self.mask = pygame.mask.from_surface(self.image1)# 从指定 Surface对象中返回一个Mask
    
    def moveUp(self):#向上飞
        if self.rect.top > 0:#如果飞机是在游戏窗口内的话
            self.rect.top -= self.speed#子弹的移动的同时修改TOP坐标,具体参考坐标系以及运算符 c -= a 等于 c = c - a, a不变，但是c越来越小,就是top逐渐靠近0
        else:#上面是 大于0   else就是小于等于0 证明此时飞机碰到游戏窗口顶端或是已经飞出时
            self.rect.top = 0#控制飞机TOP最小=0 那么飞机至多只能碰到游戏窗口顶端，而不能飞出窗口
    def moveDown(self):#向下飞
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60#因为上文提到，窗口仍需要空间放置飞机生命值与炸弹剩余值，所以飞机不能飞到其所在区域，意思为 飞机的最低端不能小于 游戏窗口高度-60即飞机生命值与炸弹剩余值所在区域
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
    def moveRight(self):#向右飞
        if self.rect.right < self.width:#如果飞机最右边坐标数值小于游戏窗口宽度
            self.rect.right += self.speed#那么飞机可以一直向右飞，此时飞机的最右边坐标数值一直变大 c += a 等于 c = c + a 
        else:#如果飞机最右边坐标数值大于等于游戏窗口宽度时
            self.rect.right = self.width#设定飞机最右边坐标数值最多等于游戏窗口宽度
    def reset(self):#复活，飞机出现位置
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2,\
            self.height - self.rect.height - 60
        self.active = True#飞机现在是活的
        self.invincible = True#飞机此时处于无敌状态
        

