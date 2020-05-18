import pygame
import random
import math
from pygame  import mixer

pygame.init()
clock = pygame.time.Clock()

#create the gaming screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('space.jpg')

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('reptile.png')
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('transportation.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemyship=4
enemyImg = pygame.image.load('invaders.png')

for i in range(no_of_enemyship):	
	enemyX.append(random.randint(0,735))
	enemyY.append(random.randint(50,150))
	enemyX_change.append(4)
	enemyY_change.append(40)

#bullet
	# Ready - You can't see the bullet on the screen
	# Fire  - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 480
bulletY_change = 5
bullet_state = "ready"

#score
global score_value
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf',64)

#levelUP
currentLevelScore=0
level=1
levelfont = pygame.font.Font('freesansbold.ttf',15)
levelUP = False


def show_score(x,y,l):
	score = font.render("Score :"+str(score_value),True,(255,255,255))
	screen.blit(score,(x,y))
	lvl = levelfont.render("Level :"+str(l),True,(255,255,255))
	screen.blit(lvl,(x,y+35))

def game_over_text():
	over_text= font.render("GAME OVER",True,(255,255,255))
	screen.blit(over_text,(300,250))

def player(x,y):
	screen.blit(playerImg,(x,y))

def enemy(x,y,i):
	screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg,(x+16,y+10))

def isCollison(bulletX,bulletY,enemyX,enemyY):
	distance = math.sqrt(math.pow((enemyX- bulletX),2) + math.pow((enemyY- bulletY),2))
	if distance< 27:
		return True
	else:
		return False




#game loop
running = True
while running:

	screen.fill((0,0,0))
	screen.blit(background,(0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# if keystroke is pressed check whether it is right or left
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -3
			if event.key == pygame.K_RIGHT:
				playerX_change = 3
			if event.key == pygame.K_SPACE:
				if bullet_state == "ready":
					bullet_sound = mixer.Sound('laser.wav')
					bullet_sound.play()
					bulletX = playerX
					fire_bullet(bulletX,bulletY)


		if event.type == pygame.KEYUP:
			if  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0
			
	#checking boundaries of spaceship to stay in screen
	playerX+=playerX_change

	if playerX<=0:
		playerX=0
	elif playerX>=736:
		playerX=736

	#checking boundaries of enemy to stay in screen
	for i in range(no_of_enemyship):

		#game over
		if enemyY[i] >440:
			for j in range(no_of_enemyship):
				enemyY[j]=2000
			game_over_text()
			bullet_state="ready"
			break

		enemyX[i]+=enemyX_change[i]

		if enemyX[i]<=0:
			enemyX_change[i] = 1
			enemyY[i] += enemyY_change[i]
		elif enemyX[i]>=736:
			enemyX_change[i] = -1
			enemyY[i] += enemyY_change[i]


	#bullet movement 
		if bulletY<=0:
			bulletY=480
			bullet_state="ready"
		if bullet_state == "fire":
			fire_bullet(bulletX,bulletY)
			bulletY -= bulletY_change

	#collision
		collision = isCollison(bulletX,bulletY,enemyX[i],enemyY[i])
		if collision:
			explosion_sound = mixer.Sound('explosion.wav')
			explosion_sound.play()
			bulletY = 480
			bullet_state = "ready"
			score_value+=1
			currentLevelScore+=1

			if currentLevelScore>15:
				currentLevelScore=0
				level+=1
				enemyX[i] = random.randint(0,736)
				enemyY[i] = random.randint(50,150)
				enemy(enemyX[i],enemyY[i],i)
				levelUP = True

			enemyX[i] = random.randint(0,736)
			enemyY[i] = random.randint(50,150)
		enemy(enemyX[i],enemyY[i],i)

	
	if levelUP:
		levelUP = False
		no_of_enemyship+=1
		enemyX.append(random.randint(0,736))
		enemyY.append(random.randint(50,150))
		enemy(enemyX[-1],enemyY[-1],i)

	player(playerX,playerY)
	show_score(textX,textY,level)
	pygame.display.update()