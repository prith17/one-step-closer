# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:39:54 2018

@author: PRITHVIRAJ NAIK
"""
import pygame,sys
#import time
from pygame.locals import *
pygame.init()
BG= pygame.display.set_mode((600, 600))
pygame.display.set_caption('One Step Closer')
cnt=0

B=(0,0,0)
W=(255,255,255)
O=(255,165,0)
G=(185,255,70)
R=(255,0,0)
P=(186,85,211)
Y=(255,255,0)
BL=(0,191,255)
"""def next():
    e=pygame.image.load('next.png')
    BG.blit(e,(0,0)) 
    time.sleep(2.5)"""
    

def gameover():
       c=pygame.image.load('Untitled1.png')
       BG.blit(c,(0,0))
def last():
       c=pygame.image.load('last.png')
       BG.blit(c,(0,0))       
def level6():
   cnt=0
   size=12
   BG.fill(B)
   c=pygame.image.load('level6.png')
   BG.blit(c,(240,0))       
   s=pygame.image.load('S6.png')
   BG.blit(s,(550,520))  
   d=pygame.image.load('D6.png')
   BG.blit(d,(40,120))  
   f=pygame.image.load('evaluate.png')
   BG.blit(f,(240,560))
   for i in range(size):
     for j in range(size):
        pygame.draw.rect(BG,BL,(70+j*40,70+i*40,40,40),4)          
   while True: # main game loop
     for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
           mx,my = event.pos
           for i in range(size):
               for j in range(size):
                   if mx >=70+j*40 and mx <=110+j*40 and my >=70+i*40 and my <=110+i*40:
                       pygame.draw.rect(BG,BL,(70+j*40,70+i*40,40,40))
                       cnt=cnt+1              
                   if mx>=240 and mx<=380 and my>=560 and my<=596:
                       if cnt==22:
                          last()
                       else:
                          gameover()
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
     pygame.display.update()        
       
def level5():
   cnt=0
   size=10
   BG.fill(B)
   c=pygame.image.load('level5.png')
   BG.blit(c,(240,0))       
   s=pygame.image.load('S5.png')
   BG.blit(s,(500,140))  
   d=pygame.image.load('D5.png')
   BG.blit(d,(60,460))  
   f=pygame.image.load('evaluate.png')
   BG.blit(f,(240,530))
   for i in range(size):
     for j in range(size):
        pygame.draw.rect(BG,Y,(100+j*40,100+i*40,40,40),4)          
   while True: # main game loop
     for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
           mx,my = event.pos
           for i in range(size):
               for j in range(size):
                   if mx >=100+j*40 and mx <=140+j*40 and my >=100+i*40 and my <=140+i*40:
                       pygame.draw.rect(BG,Y,(100+j*40,100+i*40,40,40))
                       cnt=cnt+1  
                   if mx>=240 and mx<=380 and my>=530 and my<=566:
                       if cnt==18:
                          level6()
                       else:
                          gameover()
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
     pygame.display.update() 
     
def level4():
   cnt=0
   size=8
   BG.fill(B)
   c=pygame.image.load('level4.png')
   BG.blit(c,(240,0))       
   s=pygame.image.load('S4.png')
   BG.blit(s,(110,60))  
   d=pygame.image.load('D4.png')
   BG.blit(d,(350,510))  
   f=pygame.image.load('evaluate.png')
   BG.blit(f,(240,550))
   for i in range(size):
     for j in range(size):
        pygame.draw.rect(BG,P,(100+j*50,100+i*50,50,50),4)          
   while True: # main game loop
     for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
           mx,my = event.pos
           for i in range(size):
               for j in range(size):
                   if mx >=100+j*50 and mx <=150+j*50 and my >=100+i*50 and my <=150+i*50:
                       pygame.draw.rect(BG,P,(100+j*50,100+i*50,50,50))
                       cnt=cnt+1    
                   if mx>=240 and mx<=380 and my>=550 and my<=586:
                       if cnt==13:
                          level5()
                       else:
                          gameover()
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
     pygame.display.update() 
     
       
def level3():
   cnt=0
   size=6
   BG.fill(B)
   c=pygame.image.load('level3.png')
   BG.blit(c,(240,0))       
   s=pygame.image.load('S3.png')
   BG.blit(s,(100,160))  
   d=pygame.image.load('D3.png')
   BG.blit(d,(350,460))  
   f=pygame.image.load('evaluate.png')
   BG.blit(f,(240,520))
   for i in range(size):
     for j in range(size):
        pygame.draw.rect(BG,R,(150+j*50,150+i*50,50,50),4)          
   while True: # main game loop
     for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
           mx,my = event.pos
           for i in range(size):
               for j in range(size):
                   if mx >=150+j*50 and mx <=200+j*50 and my >=150+i*50 and my <=200+i*50:
                       pygame.draw.rect(BG,R,(150+j*50,150+i*50,50,50))
                       cnt=cnt+1    
                   if mx>=240 and mx<=380 and my>=520 and my<=556:
                       if cnt==10:
                          level4()
                       else:
                          gameover() 
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
     pygame.display.update()       

def level2():
   cnt=0
   size=4
   BG.fill(B)
   c=pygame.image.load('level2.png')
   BG.blit(c,(240,0))       
   s=pygame.image.load('S2.png')
   BG.blit(s,(40,200))  
   d=pygame.image.load('D2.png')
   BG.blit(d,(500,400)) 
   f=pygame.image.load('evaluate.png')
   BG.blit(f,(240,500)) 
   for i in range(size):
     for j in range(size):
        pygame.draw.rect(BG,G,(100+j*100,100+i*100,100,100),4)          
   while True: # main game loop
     for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
           mx,my = event.pos
           for i in range(size):
               for j in range(size):
                   if mx >=100+j*100 and mx <=200+j*100 and my >=100+i*100 and my <=200+i*100:
                       pygame.draw.rect(BG,G,(100+j*100,100+i*100,100,100))
                       cnt=cnt+1
                   if mx>=240 and mx<=380 and my>=500 and my<=536:
                       if cnt==6:
                          level3()
                       else:
                          gameover()   
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
     pygame.display.update()
     
def level1():
   cnt=0
   size=2
   BG.fill(B)
   c=pygame.image.load('level1.png')
   BG.blit(c,(240,0))
   s=pygame.image.load('S.png')
   BG.blit(s,(80,180))  
   d=pygame.image.load('D.png')
   BG.blit(d,(450,320))
   f=pygame.image.load('evaluate.png')
   BG.blit(f,(240,460))     
   for i in range(size):
     for j in range(size):
        pygame.draw.rect(BG,O,(150+j*150,150+i*150,150,150),4)          
   while True: # main game loop
     for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
           mx,my = event.pos
           for i in range(size):
               for j in range(size):
                   if mx >=150+j*150 and mx <=300+j*150 and my >=150+i*150 and my <=300+i*150:
                       pygame.draw.rect(BG,O,(150+j*150,150+i*150,150,150))
                       cnt=cnt+1
                   if mx>=240 and mx<=380 and my>=460 and my<=496:
                       if cnt==3:
                          level2()
                       else:
                          gameover()
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
     pygame.display.update() 
            
BG.fill(W)
c=pygame.image.load('Untitled.png')
BG.blit(c,(0,0))    
while True:
     for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
               level1()
     pygame.display.update()     

    