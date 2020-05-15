import pygame
import sys,random,time

pygame.init()

screen = pygame.display.set_mode((720,460))
pygame.display.set_caption('snake game')

# Colors
red = pygame.Color(255, 0, 0) # gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

running = True


#fpsController = pygame.time.Clock()


#snake's positions
snakePos = [100,50]
snakeBody=[[100,50]]#,[90,50],[80,50]]
initial=[[100,50]]#,[90,50],[80,50]]


#apple's position
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True


direction = 'RIGHT'
changeto = direction

score_value = 0
font = pygame.font.Font('freesansbold.ttf',20)
gameExit = False

def show_score():
    score = font.render("Score:"+str(score_value),True,black   )
    screen.blit(score,(10,10))

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


        if foodSpawn == False:
            foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
            foodSpawn = True

        #checking it's not eating itself
        for block in snakeBody[1:]:
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                restart()
                score_value=0

        #checking if it stays in the screen
        if snakePos[0] > 710 or snakePos[0] < 0:
            restart()
            score_value=0
            
        if snakePos[1] > 450 or snakePos[1] < 0:
            restart()
            score_value=0

                

    


    #displaying the snake
    for pos in snakeBody:
        pygame.draw.rect(screen,red,pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(screen, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
    show_score()
    pygame.display.update()

    
    