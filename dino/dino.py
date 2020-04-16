import pygame
import random
pygame.init()
win = pygame.display.set_mode((1000, 500))

anim=[pygame.image.load('дино1.png'),pygame.image.load('дино2.png'),pygame.image.load('дино3.png')]
pl=pygame.image.load('дино1.png')
pol=pygame.image.load('пол.png')
trees=[pygame.image.load('дерево1.png'),pygame.image.load('дерево2.png'),pygame.image.load('дерево3.png')]
class Dino:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
class floor:
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
    def draw(self,win):
        win.blit(pol,(self.x,self.y))
class tree:
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed=speed
        self.tree=random.choice(trees)
    def draw(self,win):
        win.blit(self.tree,(self.x,self.y))
floors=[floor(1,400,10),floor(1001,400,10)]
treesg=[tree(1000,330,5),tree(2000,330,5)]
run=True
start=False
isRun=True
anx=1
c=0
dino=Dino(10,280,150,150)
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        start=True
    #if start==True:
    if dino.y+dino.height<430:
        dino.y+=2
    # else:
    #     isRun=True


    floors[0].x-=floors[0].speed
    floors[1].x-=floors[1].speed
    if floors[0].x<=-1000:
        floors.clear()
        floors.append(floor(1,400,5))
        floors.append(floor(1001,400,5))

    if treesg[0].x<=0:
        treesg.append(tree(1500+random.randint(1,500),330,5))
    if treesg[0].x<=0:
        del treesg[0]
    treesg[0].x-=treesg[0].speed
    treesg[1].x-=treesg[1].speed
    win.fill((255,255,255))
    for b in floors:
        b.draw(win)
    for b in treesg:
        b.draw(win)


    if key[pygame.K_SPACE]and dino.y>=425 :
        isRun=False
    if isRun ==False and  c<10:
        c+=1
        dino.y-=20
        win.blit(anim[0],(dino.x,dino.y))
    if c >= 10 :
        c=0
        isRun=True


    if isRun==True:
        if anx ==4:
            win.blit(anim[2],(dino.x,dino.y))
            anx=1
        if anx ==3:
            win.blit(anim[0],(dino.x,dino.y))
            anx+=1
        if anx ==2:
            win.blit(anim[1],(dino.x,dino.y))
            anx+=1
        if anx ==1:
            win.blit(anim[0],(dino.x,dino.y))
            anx+=1
    pygame.display.update()
pygame.quit()
