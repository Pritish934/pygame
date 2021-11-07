import pygame 
import random
pygame.init()
screen_width = 900
screen_height = 500


# colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")

# game variable
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10
fps = 50
velocity_x = 0
velocity_y = 0
food_x = random.randint(0,screen_width)
food_y = random.randint(0,screen_height)
score = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,50,)

def screen_score(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color, snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,black,[x,y,snake_size,snake_size])
    
snk_list = []
snk_length = 1


# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x += 10
                velocity_x = 10
                velocity_y = 0
            
            if event.key == pygame.K_DOWN:
                snake_y += 10
                velocity_y = 10
                velocity_x = 0
            
            if event.key == pygame.K_LEFT:
                snake_x -= 10
                velocity_x = -10
                velocity_y = 0
            
            if event.key == pygame.K_UP:
                snake_y -= 10
                velocity_y = -10
                velocity_x = 0
    
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y


    if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
        score = score + 1
        food_x = random.randint(0,screen_width)
        food_y = random.randint(0,screen_height)
        snk_length += 5
        


    gameWindow.fill(white)
    screen_score("Score: " + str(score),red, 5,5)
    pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list) >snk_length:
        del snk_list[0]

    # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    plot_snake(gameWindow,black,snk_list,snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()