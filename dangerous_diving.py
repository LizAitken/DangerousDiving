import pygame
import random
import os, os.path

GAME_WIDTH = 1152
GAME_HEIGHT = 648

class Ocean(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.randomize_size = random.randint(10,100)
        # size is set by width then height
        self.size = [self.randomize_size*3,self.randomize_size]
        self.score = self.size[0] * self.size[1]
        self.pos = [GAME_WIDTH + self.size[0],random.randint(200,500)]
        self.image = image
        self.image_orginal = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = random.randint(1,10)

    def move_object(self):
        if self.rect.x  <= 0 - self.size[0]:
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
            self.randomize_size = random.randint(10,100)
            self.size = [self.randomize_size*3,self.randomize_size]
            self.image = pygame.transform.scale(self.image_original, (self.size[0], self.size[1]))
        else:
            self.rect.x -= self.speed

class Fish(Ocean):
    def __init__(self,image):
        super().__init__(image)
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.image_original = image
class Shark(Ocean):
    def __init__(self,image):
        super().__init__(image)
        self.size = [400,150]
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.speed = 30
        self.show_wait = 0
        self.show = False
        self.randomSet = random.randint(1,2000)

    def move_object(self):
        
        if self.show_wait == self.randomSet:
            self.show = True
            self.show_wait = 0 
        elif self.show == True and self.rect.x > (0-self.size[0]):
            self.rect.x -= self.speed
        elif self.show == True and self.rect.x <= (0-self.size[0]):
            self.show = False
            self.randomSet = random.randint(1,2000)
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

        self.index = 0
        self.stagger = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 2
        self.show_wait = 0
        self.show = False
        self.direction = 'S'
        self.randomSet = random.randint(1,2000)

    def move_object(self):

        if self.rect.y <= 0:
            self.direction = 'S'
        elif self.rect.y >= (GAME_HEIGHT-self.size[1]) :
            self.direction = 'N'

        if self.rect.y > 0 and self.direction == 'N':
            self.rect.y -= self.speed
        elif self.rect.y < (GAME_HEIGHT-self.size[1]) and self.direction == 'S':
            self.rect.y += self.speed
        
        if self.show_wait == self.randomSet:
            self.show = True
            self.show_wait = 0 
        elif self.show == True and self.rect.x > (0-self.size[0]):            
            self.rect.x -= self.speed
        elif self.show == True and self.rect.x <= (0-self.size[0]):
            self.show = False
            self.randomSet = random.randint(1,2000)
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        else:
            self.show_wait += 1

    def update(self):
        if self.stagger == 3:
            self.stagger = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        else:
            self.stagger += 1

class Coin(Ocean):
    def __init__(self,image):
        super().__init__(image)

        self.size = [50,50]
        self.images= []
        self.images.append(pygame.image.load('My_images/coin/coin0.png'))
        self.images.append(pygame.image.load('My_images/coin/coin1.png'))
        self.images.append(pygame.image.load('My_images/coin/coin2.png'))
        self.images.append(pygame.image.load('My_images/coin/coin3.png')) #
        self.images.append(pygame.image.load('My_images/coin/coin4.png')) #
        self.images.append(pygame.image.load('My_images/coin/coin5.png')) #
        self.images.append(pygame.image.load('My_images/coin/coin6.png')) #
        self.images.append(pygame.image.load('My_images/coin/coin7.png')) #
        self.images.append(pygame.image.load('My_images/coin/coin8.png'))

        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (self.size[0], self.size[1]))

        # for i in range(len([f for f in os.listdir(imagepath) if os.path.isfile(os.path.join(imagepath,f))])-1):
        #     self.images.append(pygame.image.load('%sjellyfish%d.png' % (imagepath,i)))

        self.index = 0
        self.stagger = 0
        self.image = self.images[self.index]
        self.image_original = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 2
        self.show_wait = 0
        self.show = False
        self.direction = 'S'
        self.randomSet = 20#random.randint(500,2000)

    def update(self):
        if self.stagger == 3:
            self.stagger = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        else:
            self.stagger += 1

def main():

    pygame.init()

    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    background_image = pygame.image.load('My_images/2_game_background.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (GAME_WIDTH, GAME_HEIGHT))
    shark_image = pygame.image.load('My_images/shark.png').convert_alpha()
    jellyfish_image = pygame.image.load('My_images/shark.png').convert_alpha()

    # create all fish images
    fish_image = {}
    for i in range(5):
        fish_image['fish_%d'%i] = pygame.image.load('My_images/fish_%d.png' % i).convert_alpha()

    pygame.display.set_caption('Dangerous Diving')

    # Game initialization
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
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        for fish in smallFish:
            fish.move_object()

        jelly.update()
        coin.update()

        shark.move_object()
        jelly.move_object()
        coin.move_object()
        # Draw background
        screen.blit(background_image,[0,0])

        # Game display
        ocean_group.draw(screen)

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
