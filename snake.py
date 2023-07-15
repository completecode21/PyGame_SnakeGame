import random
import pygame
pygame.init()
pygame.mixer.init()


#CREATING WINDOW
screen_width = 800
screen_height =400
GameWindow = pygame.display.set_mode((screen_width,screen_height))
#GIVING TITLE
pygame.display.set_caption("SnakeGame")
pygame.display.update()

#colour required
white = (248,248,255)
black =(0,0,0)
red = (255,0 ,0)
blue = (0,191,255)
green = (202,255,112)



#Showing score in screen
bg_image = pygame.image.load("game_bg.jpg")
bg_image = pygame.transform.scale(bg_image,(screen_width,screen_height)).convert_alpha()
font = pygame.font.SysFont(None,40)
def text_screen(text, color, x, y ):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, [x,y])



#Increasing snake size
def plot_snake(GameWindow,color,snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(GameWindow, color, [x, y, snake_size, snake_size])

#Welcome Window
def welcome():
    exit_game = False
    while not exit_game:
        GameWindow.fill(green)
        GameWindow.blit(bg_image,(0,0))
        text_screen("Welcome to Snakes", blue, 230, 170)
        text_screen("Press Space to Start!", blue, 225, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('game_back.mp3')
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(30)
 


#Defining a clock
clock = pygame.time.Clock()



#Game loop
def game_loop():
    

    #game specific variabes
    exit_game = False
    game_over = False
    snake_size = 20
    snake_x = 55
    snake_y = 55
    fps = 30
    velocity_x = 4
    velocity_y = 4
    with open("hiscore.txt","r") as f:
        hiscore = f.read()
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20,screen_height/2)
    score = 0
    snake_list = []
    snake_length = 1

    # #Snake Face
    # snake_face = pygame.image.load("block.jpg").convert_alpha()
    # GameWindow.blit(snake_face,(snake_x, snake_y))
    # pygame.display.update()
    # clock.tick(30)

     

 #loop
    
    while not exit_game:
        if game_over:
            with open("hiscore.txt","w") as f:
               f.write(str(hiscore))
            GameWindow.fill(white)
            GameWindow.blit(bg_image,(0,0))
            text_screen("Game Over! Press Enter to Continue or Backspace for Quit",red,10,170)
            text_screen("Your Score: "+ str(score),red,270,200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if  event.key == pygame.K_RETURN:
                        welcome()
                    if  event.key == pygame.K_BACKSPACE:
                        exit_game = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = + 5
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 5
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y  = - 5
                        velocity_x =0 
                    if event.key == pygame.K_DOWN:
                        velocity_y = + 5
                        velocity_x = 0
                    #Cheate code:
                    if event.key == pygame.K_z:
                        score += 5


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            


            if abs(snake_x - food_x)< 6 and abs(snake_y - food_y)<6:     
                score += 1
                eat_sound = pygame.mixer.Sound('game_eat.mp3')
                eat_sound.play()
            

                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20,screen_height/2)
                snake_length += 5
                if score > int(hiscore):
                    hiscore = score



            GameWindow.fill(white)
            GameWindow.blit(bg_image,(0,0))
            text_screen("Score: "+ str(score) + " Hiscore: " +str(hiscore), red, 10, 10)
            pygame.draw.rect(GameWindow,red,[food_x, food_y, snake_size, snake_size])
            

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)> snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.pause()
                game_over_sound = pygame.mixer.Sound('game_over.mp3')
                game_over_sound.play()
                

            if snake_x<0 or snake_x>screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.pause()
                game_over_sound = pygame.mixer.Sound('game_over.mp3')
                game_over_sound.play()

            #pygame.draw.rect(GameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(GameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)





    pygame.quit()
    quit()
welcome()