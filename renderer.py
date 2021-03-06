import pygame
from threading import Thread
size=int(input("input size: "))
class rendered():
    def __init__(self,color,pos,radious) -> None:
        self.color=color
        self.pos=pos
        self.rad=radious
    def move(self,new):
        self.pos = (self.pos[0]+new[0],self.pos[1]+new[1])

class enemy(rendered):
    def __init__(self,color,pos,radious,hp,damage) -> None:
        super().__init__(color, pos, radious)
        self.hp=hp
        self.damage=damage

player=False
screen = pygame.display.set_mode((size,size))
ren=[]
enemies=[]
cl =pygame.time.Clock()
objects = {
    "objects":[],
    "ids ":[]
}
def get_object_from_pos(pos) -> rendered:
    global ren
    for i in ren:
        if i.pos == pos:
            return i
def get_enemy_from_pos(pos) -> enemy:
    global enemies
    for i in enemies:
        if i.pos == pos:
            return i
def loop():
    while True:
        cl.tick(30)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                import network
                network.client.send("quit".encode())
                pygame.quit()
        screen.fill((24, 119, 9))
        for i in range(40): 
            pygame.draw.rect(screen,(0,0,0),(i*(size/40),0,1,800))
        for i in range(40): 
            pygame.draw.rect(screen,(0,0,0),(0,i*(size/40),800,1))
        for i in ren:
            pygame.draw.circle(screen,i.color,(i.pos[0]*(size/80),i.pos[1]*(size/80)),i.rad)
        for i in enemies:
            pygame.draw.circle(screen,i.color,(i.pos[0]*(size/80),i.pos[1]*(size/80)),i.rad)
        pygame.display.update()
Thread(target=loop).start()