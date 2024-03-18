#***************************************CREATED BY MWAMBA CHANDA******************************************************
import pygame
import time
import random
pygame.font.init()


#*****************************************Global Variables****************************************************
WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
#at this point the window runs and closes, well how then do we tell py to hold the window open?
#Essentially all games run in a loop, and so with the loop we can tell the game to stay open as long as the
#loop is still running!



#Let's create a variable to hold the background image
BG = pygame.transform.scale(pygame.image.load("space.jpg"), (WIDTH, HEIGHT))

#assigning player variable with defined characteristics like width height
PLAYER_WIDTH = 40 #pixels
PLAYER_HEIGHT = 60 #pixels
PLAYER_VEL = 10
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 5






FONT = pygame.font.SysFont("comicsans", 30)

#*****************************************Global Variables****************************************************
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0,)) #Blit here is inbuilt in python to draw something to the screen
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    #Draw star
    for star in stars:
        pygame.draw.rect(WIN, "White", star)

    pygame.display.update()
    
def main():
    run = True
    
    #lets create a player variable
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT) #this player rectangle needs dimentions
    clock = pygame.time.Clock()

    start_time = time.time() #lets create a way to keep track of time
    elapsed_time = 0

#Now lets add some projectiles to the game, the logic here is to add projectiles increasingly quicker with the passage
#of time
#***********Projectiles**********
    star_add_increment = 2000 #after every 2000 milliseconds lets add a projectile to the screen
    star_count = 0 #initiallize the number of projectiles at 0
    stars = [] #the list to hold the projectiles
    hit = False
#***********Projectiles**********
    while run:
        clock.tick(60)
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time #keeping track of time

        if star_count > star_add_increment: 
            for _ in range (3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)


                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0 #resets the star count


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        #Let's now create movement on the screen. we use events and even listeners to achieve this
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys [pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        #Lets put those star projectiles on the sceen
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT: 
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break


        if hit:
            lost_text = FONT.render("You lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)

            break

        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()

#***************************************CREATED BY MWAMBA CHANDA******************************************************