import pygame
import random,time

pygame.init()


#setting the screen
screen = pygame.display.set_mode((720,460))
pygame.display.set_caption('snake game')

# Colors
red = pygame.Color(255, 0, 0) # gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background

running = True

#snake's positions
snakePos = [100,50]
snakeBody=[[100,50]]
initial=[[100,50]]


#apple's position
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True


direction = 'RIGHT'
changeto = direction

score_value = 0
high_score = 0
font = pygame.font.Font('freesansbold.ttf',20)
highScoreFont = pygame.font.Font('freesansbold.ttf',12)

clock = pygame.time.Clock()

def show_score():
    score = font.render("score:"+str(score_value),True,black)
    screen.blit(score,(10,10))

#optional
def show_hscore():
    score = highScoreFont.render("high score:"+str(high_score),True,black)
    screen.blit(score,(10,35))#adding font size to the score's x coordinate

def restart():
    snakeBody.clear()
    snakePos.clear()
    snakeBody.append([100,50])
    snakePos.append(100)
    snakePos.append(50)
    


while running:
    grow=0
    screen.fill(white)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False        

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'              

        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10


    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
        score_value+=1
    else:
        snakeBody.pop()


    #generating new food
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
        foodSpawn = True

    #checking it's not eating itself
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            restart()
            direction = 'RIGHT'
            high_score = score_value
            score_value=0

    #checking if it stays in the screen
    if snakePos[0] > 710 or snakePos[0] < 0:
        restart()
        direction = 'RIGHT'
        score_value=0
            
    if snakePos[1] > 450 or snakePos[1] < 0:
        restart()
        direction = 'RIGHT'
        score_value=0             


    #displaying the snake
    for pos in snakeBody:
        pygame.draw.rect(screen,red,pygame.Rect(pos[0],pos[1],10,10))

    #drawing the snake in the screen
    pygame.draw.rect(screen, green, pygame.Rect(foodPos[0],foodPos[1],10,10))
    show_score()
    if score_value>=high_score:
        high_score=score_value
    show_hscore()
    pygame.display.update()
    #choose the speed of the snake
    #larger number = more speed
    clock.tick(15)