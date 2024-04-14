# Ebtesam Aloubid - 101260655
import pygame
import sys
import random
 # name of the source image as a command-line argument
image= sys.argv[1]
src_img = pygame.image.load(image)
# getting the size of the image 
(width, hight) = src_img.get_size()
#  scaled up by 5
surface= pygame.display.set_mode((width*5,hight*5))
#surface.blit(src_img,(0,0))
# nested loop to draw points 
for x in range(width):
    for y in range(hight):
        # getting the colors from the image
        (r,g,b,_) = src_img.get_at((x,y))
        # calucalting how many circles to draw
        n_r = r//50
        n_g= g//50
        n_b= b//50

        # draw circles
        while (n_g>0):
                 pygame.draw.circle(surface,(0,255,0),(random.randint((x*5)-12,(x*5)),random.randint((y*5)-12,(y*5))),1)
                 n_g= n_g - 1
        while(n_r>0):
                pygame.draw.circle(surface,(255,0,0),(random.randint((x*5)-12,(x*5)),random.randint((y*5)-12,(y*5))),1)
                n_r= n_r -1 
        while(n_b>0):
                pygame.draw.circle(surface,(0,0,255),(random.randint((x*5)-12,(x*5)),random.randint((y*5)-12,(y*5))),1)
                n_b= n_b - 1
# update the diplay 
pygame.display.update()
# while loop to keep the screen open 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()	