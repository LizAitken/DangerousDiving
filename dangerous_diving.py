import pygame
import random
import time
import score as total
from datetime import datetime
from ocean import *
from player import *
from moving_background import *
from health import *
from score import *
from global_constants import *

# Add in keys
KEY_UP = 273
KEY_DOWN = 274       

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Game initializers
        pygame.init()
        pygame.display.set_caption('Dangerous Diving')
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.run_intro = True
        self.run = True
        self.status = ''
        self.background = ''

    # load background and scale
    def intro_screen(self):
        self.background = pygame.image.load('My_images/1_game_backgroundREDO.png').convert_alpha()
        self.background  = pygame.transform.scale(self.background, [GAME_WIDTH, GAME_HEIGHT])
        self.wait_for_screen()

    # load background, scale, and set the status
    def lose_screen(self):
        self.background = pygame.image.load('My_images/4_game_background.png').convert_alpha()
        self.background  = pygame.transform.scale(self.background, [GAME_WIDTH, GAME_HEIGHT])
        self.status = 'lose'
        self.wait_for_screen()

    # load background, scale, and set the status
    def win_screen(self):
        self.background = pygame.image.load('My_images/3_game_background.png').convert_alpha()
        self.background  = pygame.transform.scale(self.background, [GAME_WIDTH, GAME_HEIGHT])
        self.status = 'win'
        self.wait_for_screen()

    def wait_for_screen(self):
        self.screen.blit(self.background,[0,0])

        # During the screen we wait for the user input
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYUP:
                    self.run_intro = False
                    total.totalscore = 0
                    self.run_game()
            
            # We will always print these in the win and lose screens
            if self.status != '':
                draw_text(self.screen,('Your score: %d' % total.totalscore), 60, GAME_WIDTH / 2, GAME_HEIGHT / 3, (255,255,255))
                draw_text(self.screen,('Press any key to play again'), 60, GAME_WIDTH / 2, 430, (255,128,0))
            
            # We add custom text for win and lose
            if self.status == 'win':
                draw_text(self.screen,('YOU WON!'), 68, GAME_WIDTH / 2, GAME_HEIGHT / 2, (255,255,255))
            elif self.status == 'lose':
                draw_text(self.screen,('YOU LOSE!'), 68, GAME_WIDTH / 2, GAME_HEIGHT / 2, (255,255,255))

            pygame.display.update()
        pygame.quit()

    def run_game(self):
        # Moving Background
        background_image = Background(self.screen)

        # Load Images
        shark_image = pygame.image.load('My_images/shark.png').convert_alpha()
        jellyfish_image = pygame.image.load('My_images/shark.png').convert_alpha()
        pygame.display.set_caption('Dangerous Diving')
        
        # Main Music
        pygame.mixer.music.load('sounds/out_of_my_dreams.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        # Instantiatation 
        smallFish = []
        shark = Shark(shark_image)
        jelly = Jellyfish(jellyfish_image)
        coin = Coin(jellyfish_image)
        ocean_group = pygame.sprite.Group()

        # loop to load fish and add to ocean group
        for i in range(5):
            smallFish.append(Fish(pygame.image.load('My_images/fish_%d.png' % i).convert_alpha()))
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

        running = True

        # initialize the seconds and minutes. Minutes is needed even though we only got for 60 seconds because of the logic.
        second_start = int(time.strftime("%S", time.gmtime()))
        minute_start = int(time.strftime("%M", time.gmtime()))

        last = 0
        running = True

        while running:
            # check if we need to run the intro screen
            if game.run_intro:
                game.intro_screen()

            #Timer to check if we survived 60 seconds
            elpased_second = int(time.strftime("%S", time.gmtime()))
            elapsed_minute = int(time.strftime("%M", time.gmtime()))
            minute_timer = elapsed_minute - minute_start
            second_timer = 60 - (elpased_second - second_start + (minute_timer * 60))
            
            # If the timer runs out we win!
            if second_timer == 0:
                running = False
                game.win_screen()
                time.sleep(3)

            # If our health is 0 we lose
            if player.player_health <= 0:
                game.lose_screen()


            # Event handling for user input for when were in game
            for event in pygame.event.get():
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

            # Sprite Collision
            hit = pygame.sprite.spritecollide(player,ocean_group,False) # this is a list of sprites. Each item references a class
            if len(hit) != last and len(hit) > 0: # will only check for initial collision
                for thing in hit:
                    # If we get a coin we want to pop the coin then read add it,same function as spritecollide(True)
                    if 'Coin' in str(thing):
                        ocean_group.remove(coin)
                        ocean_group.add(coin)
                        # We set the coin all the way to the left axis and our Ocean class will reset the X,Y coords and the random timer
                        coin.rect.x = 0 - coin.rect.width
                        thing.sound.play()
                        if player.player_health < 10:
                            player.player_health += 1                    
                    elif 'Shark' in str(thing):
                        thing.sound.play()
                        # Shark deals an instant kill
                        player.player_health -= 10
                    elif 'Fish' in str(thing):
                        thing.sound.play()
                        thing.score = 0
                        player.player_health -= 1

                    elif 'Jellyfish' in str(thing):
                        thing.sound.play()

                # We don't want to have negative health
                if player.player_health < 0:
                    player.player_health = 0

                health.damage(player.player_health)
            last = len(hit)

            # UPDATES
            # move gif and move objects
            player_group.update()

            for fish in smallFish:
                fish.move_object()
            
            coin.update()
            jelly.update()
            shark.move_object()

            # Draw background
            background_image.render()
            background_image.update()

            # Game display
            ocean_group.draw(self.screen)
            player_group.draw(self.screen)
            health_group.draw(self.screen)
            our_score.show_score(self.screen)
            draw_text(self.screen,('Time Left: %d' % (second_timer)), 25, GAME_WIDTH-118, 25,(105,105,105))

            pygame.display.update()
            
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run_game()