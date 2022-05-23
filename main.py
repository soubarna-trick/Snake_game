

import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# Colors
green = (90, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
#bg image
bg=pygame.image.load("b5.jpg")
bg=pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("NOKIA SNAKE")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont('chisel', 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((150,150,200))
        text_screen("Welcome to Nokia Snake ", black,200,200)
        text_screen("Press Space Bar to Play", black,232,290)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if  event.type == pygame.KEYDOWN:
                 if event.key ==pygame.K_SPACE:
                     gameloop()

        pygame.display.update()
        clock.tick(50)

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    level_finished = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    #check if highscore file exit
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        highscore = f.read()


    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    level=0
    lv1=0;
    lv2=0;
    lv3=0;
    lv4=0
    lv5=0
    lv6=0
    lv7=0
    lv7=0
    lv8=0
    lv9=0
    init_velocity = 5
    snake_size = 30
    fps = 53
    while not exit_game:

        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gameWindow.fill(green)
            if level_finished is True :
                text_screen("Hay Champ , You have finished all the levels", red, 50, 250)
            else:
                text_screen("Game Over! Press Enter To Continue", red, 100, 250)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<25 and abs(snake_y - food_y)<25:
                score +=10
                if score>20 and lv1 is 0:
                    level = level+1
                    lv1 = lv1+1
                    init_velocity=init_velocity+3


                if score>100 and lv2 is 0:
                    level = level+1
                    lv2 = lv2+1

                    init_velocity = init_velocity + 3

                if score>200 and lv3 is 0:
                    level = level+1
                    lv3 = lv3+1
                    init_velocity = init_velocity + 3

                if score>300 and lv4 is 0:
                    level = level+1
                    lv4 = lv4+1
                    init_velocity = init_velocity + 3

                if score>400 and lv5 is 0:
                    level = level+1
                    lv5 = lv5+1
                    init_velocity = init_velocity + 3

                if score>500 and lv6 is 0:
                    level = level+1
                    lv6 = lv6+1
                    init_velocity = init_velocity + 3

                if score>600 and lv7 is 0:
                    level = level+1
                    lv7 = lv7+1
                    init_velocity = init_velocity + 3

                if score > 700 and lv8 is 0:
                    level = level + 1
                    lv8 = lv8 + 1
                    init_velocity = init_velocity + 3

                if score > 800 and lv9 is 0:
                    level = level + 1
                    lv9 = lv9 + 1
                    level_finished = True
                    game_over = True


                pygame.mixer.music.load('eat.wav')
                pygame.mixer.music.play()
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(highscore):
                    highscore=score

            gameWindow.fill(green)
            gameWindow.blit(bg,(0,0))

            text_screen("Score: " + str(score),red,10,5)
            text_screen("Highscore:"+str(highscore),red,600,5)
            text_screen("Level:" + str(level), red, 300, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]



            if head in snk_list[:-1]:

                game_over = True
                pygame.mixer.music.load('die.wav')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('die.wav')

                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

