import pygame
#Variables
height = 600
width = height + height//2
black = (0,0,0)
bg_color = (0,2,22)
player_x = width//2 - width//20
player_y = height//3*2 - 300
playerx_change = 0
playery_change = 0
#Initialisation
pygame.init()
screen = pygame.display.set_mode((width,height))
running = True
game_over = False
# var projectile_size
# var botposition botwidth, var bot depth
#setting title,icon,images
icon = pygame.image.load("icon.png")
cover = pygame.image.load("space-invaders.png")
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)
player_image = pygame.transform.scale(icon, (height//10, height//10))
#Functions
def player(x,y):
    if not 0 < x < width - height//10:
        if 0 > x:
            x = 0
        else:
            x = width - height//10
    if not 0 < y < height - height//10:
        if 0 > y:
            y = 0
        else:
            y = height - height//10
    screen.blit(player_image, (x,y))
screen.fill(bg_color)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -width / 2500
            elif event.key == pygame.K_RIGHT:
                playerx_change = width / 2500
            if event.key == pygame.K_UP:
                playery_change = -width / 2500
            elif event.key == pygame.K_DOWN:
                playery_change = width / 2500
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playery_change = 0
        #if event.type == pygame.KEYUP:
            #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
    player_x += playerx_change
    player_y += playery_change
    player(player_x,player_y)
    pygame.display.update()