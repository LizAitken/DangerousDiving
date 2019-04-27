import pygame
import random
import os, os.path

GAME_WIDTH = 1152
GAME_HEIGHT = 648

# Add in keys
KEY_UP = 273
KEY_DOWN = 274

class Ocean(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.randomize_size = random.randint(10,100)
        
        # Below are image initializers
        self.size = [self.randomize_size*3,self.randomize_size]
        self.score = self.size[0] * self.size[1]
        self.pos = [GAME_WIDTH + self.size[0],random.randint(200,500)]
        self.image = image
        self.image_orginal = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.sprite_index = 0
        self.sprite_speed = 3 # If you change this value change it in move_gif as well after the first
        
        self.speed = random.randint(1,10) # Speed: How fast a objects will move (left,right,up,down,diagonally)

        self.show = False
        self.show_wait = 0
        self.show_random = random.randint(1,2000) 
    def move_object(self):

        if self.rect.x  <= 0 - self.size[0]:
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
            self.randomize_size = random.randint(10,100)
            self.size = [self.randomize_size*3,self.randomize_size]
            self.image = pygame.transform.scale(self.image_original, (self.size[0], self.size[1]))
        else:
            self.rect.x -= self.speed
            

        # if self.show_wait == self.show_random:
        #     self.show = True
        #     self.show_wait = 0 
        # elif self.show == True and self.rect.x > (0-self.size[0]):
        #     self.rect.x -= self.speed
        # elif self.show == True and self.rect.x <= (0-self.size[0]):
        #     if self.show_immediately_after_off_screen:
        #         self.rect.x = GAME_WIDTH
        #         self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        #         self.randomize_size = random.randint(10,100)
        #         self.size = [self.randomize_size*3,self.randomize_size]
        #         self.image = pygame.transform.scale(self.image_original, (self.size[0], self.size[1]))
        #     else:
        #         self.show = False
        #         self.show_random = random.randint(1,2000)
        #         self.rect.x = GAME_WIDTH
        #         self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        # else:
        #     self.show_wait += 1

    def move_gif(self):
        if self.sprite_speed == 0:
            self.sprite_speed = 3
            self.sprite_index += 1
            if self.sprite_index >= len(self.images):
                self.sprite_index = 0
            self.image = self.images[self.sprite_index]
        else:
            self.sprite_speed -= 1

class Fish(Ocean):
    def __init__(self,image):
        super().__init__(image)
        self.image = pygame.transform.scale(image, (self.size[0], self.size[1]))
        self.image_original = image
        self.show_immediately_after_off_screen = True

class Shark(Ocean):
    def __init__(self,image):
        super().__init__(image)
        self.size = [400,150]
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.image_original = image
        self.speed = 30

    def move_object(self):

        if self.show_wait == self.show_random:
            self.show = True
            self.show_wait = 0 
        elif self.show == True and self.rect.x > (0-self.size[0]):
            self.rect.x -= self.speed
        elif self.show == True and self.rect.x <= (0-self.size[0]):
            self.show = False
            self.show_random = random.randint(1,2000)
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        else:
            self.show_wait += 1

class Jellyfish(Ocean):
    def __init__(self,image):
        super().__init__(image)

        self.size = [75,75]
        self.images= []
        self.images.append(pygame.image.load('My_images/jellyfish/jellyfish0.png'))
        self.images.append(pygame.image.load('My_images/jellyfish/jellyfish1.png'))
        self.images.append(pygame.image.load('My_images/jellyfish/jellyfish2.png'))
        self.images.append(pygame.image.load('My_images/jellyfish/jellyfish3.png'))
        self.images.append(pygame.image.load('My_images/jellyfish/jellyfish4.png'))
        self.images.append(pygame.image.load('My_images/jellyfish/jellyfish5.png'))
        self.images.append(pygame.image.load('My_images/jellyfish/jellyfish6.png'))


        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (self.size[0], self.size[1]))

        # for i in range(len([f for f in os.listdir(imagepath) if os.path.isfile(os.path.join(imagepath,f))])-1):
        #     self.images.append(pygame.image.load('%sjellyfish%d.png' % (imagepath,i)))

        self.image = self.images[self.sprite_index]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 2
        self.direction = 'S'

    def move_object(self):

        if self.rect.y <= 0:
            self.direction = 'S'
        elif self.rect.y >= (GAME_HEIGHT-self.size[1]) :
            self.direction = 'N'

        if self.rect.y > 0 and self.direction == 'N':
            self.rect.y -= self.speed
        elif self.rect.y < (GAME_HEIGHT-self.size[1]) and self.direction == 'S':
            self.rect.y += self.speed
        
        if self.show_wait == self.show_random:
            self.show = True
            self.show_wait = 0 
        elif self.show == True and self.rect.x > (0-self.size[0]):            
            self.rect.x -= self.speed
        elif self.show == True and self.rect.x <= (0-self.size[0]):
            self.show = False
            self.show_random = random.randint(1,2000)
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        else:
            self.show_wait += 1

class Coin(Ocean):
    def __init__(self,image):
        super().__init__(image)

        self.size = [50,50]
        self.images= []
        self.images.append(pygame.image.load('My_images/coin/coin0.png'))
        self.images.append(pygame.image.load('My_images/coin/coin1.png'))
        self.images.append(pygame.image.load('My_images/coin/coin2.png'))
        self.images.append(pygame.image.load('My_images/coin/coin3.png')) 
        self.images.append(pygame.image.load('My_images/coin/coin4.png')) 
        self.images.append(pygame.image.load('My_images/coin/coin5.png')) 
        self.images.append(pygame.image.load('My_images/coin/coin6.png')) 
        self.images.append(pygame.image.load('My_images/coin/coin7.png'))
        self.images.append(pygame.image.load('My_images/coin/coin8.png'))
        self.images.append(pygame.image.load('My_images/coin/coin9.png'))

        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (self.size[0], self.size[1]))

        # for i in range(len([f for f in os.listdir(imagepath) if os.path.isfile(os.path.join(imagepath,f))])-1):
        #     self.images.append(pygame.image.load('%sjellyfish%d.png' % (imagepath,i)))

        self.image = self.images[self.sprite_index]
        self.image_original = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 2
        self.show_random = random.randint(500,1000)

class Game():
    pass

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([252, 60])
        # self.image.fill((0, 255, 0))
        self.x = x
        self.y = y
        # self.speed_x = 0
        self.speed_y = 0
        self.radius = 50
        #Animation
        self.index = 0
        self.images = []
        self.images.append(pygame.image.load('My_images/divercrop_1pixel.png'))
        self.images.append(pygame.image.load('My_images/divercrop_5pixel.png'))
        self.images.append(pygame.image.load('My_images/divercrop_4pixel.png'))
        self.images.append(pygame.image.load('My_images/divercrop_2pixellower.png'))
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
    
    def update(self):
        barrier_top = 22
        barrier_bottom = 580
        if self.rect.y >= barrier_top and self.rect.y <= barrier_bottom:
            self.rect.y += self.speed_y
        elif self.rect.y < barrier_top:
            self.rect.y = barrier_top
        elif self.rect.y > barrier_bottom:
            self.rect.y = barrier_bottom
        #Animation
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Boxes(pygame.sprite.Sprite):
    def __init__(self, pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([200, 60])
            self.image.fill((255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.center = pos

#screen.blit(enter_image,[0,0])
# pygame.time.delay(3000)

def intro_screen():
    pygame.init()

    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    enter_image = pygame.image.load('My_images/1_game_background.png').convert_alpha()
    enter_image = pygame.transform.scale(enter_image, [GAME_WIDTH, GAME_HEIGHT])
    pygame.display.set_caption('Dangerous Diving')
    clock = pygame.time.Clock()
    
    intro = True
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.time.get_ticks() >= 5000:
                intro = False
        screen.blit(enter_image,[0,0])
        pygame.display.update()
        clock.tick(15)
        

    pygame.quit()
        #gameDisplay.fill(white)


def main():

    pygame.init()

    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    background_image = pygame.image.load('My_images/2_game_background.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (GAME_WIDTH, GAME_HEIGHT))

    # enter_image = pygame.image.load('My_images/1_game_background.png').convert_alpha()
    # enter_image = pygame.transform.scale(enter_image, [GAME_WIDTH, GAME_HEIGHT])

    shark_image = pygame.image.load('My_images/shark.png').convert_alpha()
    jellyfish_image = pygame.image.load('My_images/shark.png').convert_alpha()
    pygame.display.set_caption('Dangerous Diving')
    


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
    player = Player(185, 320)
    # Our Health_box
    white_box = Boxes([1038, 605])
    # Adding the player to a group
    player_group = pygame.sprite.Group()
    player_group.add(player)
    # Adding the health box to a group
    health_group = pygame.sprite.Group()
    health_group.add(white_box)

    
    # Game initialization
    running = True
    while running:
        for event in pygame.event.get():
            # Event handling
            if pygame.time.get_ticks() >= 50000:
                running = False
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

        # Game logic
        player_group.update()

        for fish in smallFish:
            fish.move_object()

        jelly.move_gif()
        coin.move_gif()

        shark.move_object()
        jelly.move_object()
        coin.move_object()

        # Draw background

        screen.blit(background_image,[0,0])

        # Game display
        ocean_group.draw(screen)
        player_group.draw(screen)
        health_group.draw(screen)
        
        pygame.display.update()
        # clock.tick(60)

    pygame.quit()

intro_screen()
if __name__ == '__main__':
    main()