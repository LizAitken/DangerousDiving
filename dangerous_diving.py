import pygame
import random
import time
from datetime import datetime
from ocean import *
from player import *
import score as total
from screen_output import *
from health import *
from score import *

GAME_WIDTH = 1152
GAME_HEIGHT = 648

# Add in keys
KEY_UP = 273
KEY_DOWN = 274       

class Game():
    pass

def main():

    # Game initialization
    pygame.init()

    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    background_image = Background(screen)

    shark_image = pygame.image.load('My_images/shark.png').convert_alpha()
    jellyfish_image = pygame.image.load('My_images/shark.png').convert_alpha()
    pygame.display.set_caption('Dangerous Diving')
    
    # Main Music
    pygame.mixer.music.load('sounds/out_of_my_dreams.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    # create all fish images
    fish_image = {}
    for i in range(5):
        fish_image['fish_%d'%i] = pygame.image.load('My_images/fish_%d.png' % i).convert_alpha()

    smallFish = []
    shark = Shark(shark_image)
    jelly = Jellyfish(jellyfish_image)
    coin = Coin(jellyfish_image)
    ocean_group = pygame.sprite.Group()

    for i in range(len(fish_image)):
        smallFish.append(Fish(fish_image['fish_%d'%i]))
        ocean_group.add(smallFish[i])

    ocean_group.add(shark)
    ocean_group.add(jelly)
    ocean_group.add(coin)

    # Our Player
    player = Player(185, GAME_HEIGHT/2)
    # Our Health_box
    health = Health(player.player_health)
    # Adding the player to a group
    player_group = pygame.sprite.Group()
    player_group.add(player)
    # Adding the health box to a group
    health_group = pygame.sprite.Group()
    health_group.add(health)

    #Score
    our_score = Score()
    our_score_group = pygame.sprite.Group()
    our_score_group.add(our_score)

    last = 0

    running = True

    second_start = int(time.strftime("%S", time.gmtime()))
    minute_start = int(time.strftime("%M", time.gmtime()))

    while running:

        #Timer
        elpased_second = int(time.strftime("%S", time.gmtime()))
        elapsed_minute = int(time.strftime("%M", time.gmtime()))

        minute_timer = elapsed_minute - minute_start
        second_timer = 60 - (elpased_second - second_start + (minute_timer * 60))

        if second_timer == 0:
            running = False
            win_screen()
            time.sleep(3)


        for event in pygame.event.get():
            # Event handling

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # activate the corresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    player.speed_y = 20
                elif event.key == KEY_UP:
                    player.speed_y = -20
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    player.speed_y = 0
                elif event.key == KEY_UP:
                    player.speed_y = 0

        ################
        ################
        ## Game logic ##
        ################
        ################

        # Sprite Collision
        if player.player_health <= 0:
            lose_screen()

        hit = pygame.sprite.spritecollide(player,ocean_group,False)
        if len(hit) != last and len(hit) > 0:
            hit_coin = False
            for thing in hit:
                if 'Coin' in str(thing):
                    ocean_group.remove(coin)
                    ocean_group.add(coin)
                    coin.rect.x = 0 - coin.rect.width
                    hit_coin = True
                    thing.sound.play()
                elif 'Shark' in str(thing):
                    player.player_health -= 10
                    thing.sound.play()
                elif 'Fish' in str(thing):
                    thing.sound.play()
                    thing.score = 0
                elif 'Jellyfish' in str(thing):
                    thing.sound.play()
            if hit_coin == True:
                if player.player_health < 10:
                    player.player_health += 1
            else:
                player.player_health -= 1
            if player.player_health < 0:
                player.player_health = 0

            health.damage(player.player_health)

        last = len(hit)

        #print(player.score)

        # UPDATES
        player_group.update()

        for fish in smallFish:
            fish.move_object()
        
        #move gif and move objects
        jelly.move_gif()
        coin.move_gif()
        shark.move_object()
        jelly.move_object()
        coin.move_object()

        # Draw background
        background_image.render()
        background_image.update()

        # Game display
        ocean_group.draw(screen)
        player_group.draw(screen)
        health_group.draw(screen)
        our_score.show_score(screen)
        #our_score_group.draw(screen)
        draw_text(screen,('Time Left: %d' % (second_timer)), 25, GAME_WIDTH-118, 25,(105,105,105))

        pygame.display.update()

    pygame.quit()

intro_screen()
if __name__ == '__main__':
#    main()
    pass