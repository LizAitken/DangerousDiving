import pygame
import random

game_width = 1152
game_height = 648

class Fish(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        # size is set by width then height
        self.randomize_size = random.randint(10,100)
        self.size = [self.randomize_size*2.2,self.randomize_size]
        self.score = self.size[0] * self.size[1]
        self.image = pygame.Surface(self.size)
        self.image.fill((255, 0, 0))
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = random.randint(1,10)

    def move_fish(self):
        if self.rect.x  <= 0 - self.rect.width:
            self.rect.x = game_width
            self.rect.y = random.randint(self.rect.height, (game_height-self.rect.height))
            self.randomize_size = random.randint(10,100)
            self.size = [self.randomize_size*2.2,self.randomize_size]
        else:
            self.rect.x -= self.speed

class Shark(Fish):
    def __init__(self,pos):
        super().__init__(pos)
        self.type = 'shark'
        self.size = [400,150]
        self.image = pygame.Surface(self.size)
        self.image.fill((0, 0, 255))
        self.speed = 30
        self.show_wait = 0
        self.show = False
        self.randomSet = random.randint(1,2000)

    def move_fish(self):
        print('Random: ',self.randomSet)
        if self.show_wait == self.randomSet:
            self.show = True
            self.show_wait = 0 
        elif self.show == True and self.rect.x > (0-self.size[0]):
            self.rect.x -= self.speed
        elif self.show == True and self.rect.x <= (0-self.size[0]):
            self.show = False
            self.randomSet = random.randint(1,2000)
            self.rect.x = game_width
            self.rect.y = random.randint(self.rect.height, (game_height-self.rect.height))
        else:
            self.show_wait += 1
        
def main():

    pygame.init()

    screen = pygame.display.set_mode((game_width, game_height))
    background_image = pygame.image.load('My_images/2_game_background.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (game_width, game_height))




    pygame.display.set_caption('Dangerous Diving')
    clock = pygame.time.Clock()

    # Game initialization
    smallFish = []
    shark = Shark([game_width+100,100])
    fish_group = pygame.sprite.Group()

    for i in range(7):
        randomStagger = random.randint(200,500)
        randomY = random.randint(0,game_height)
        smallFish.append(Fish([game_width+randomStagger,randomY]))
        fish_group.add(smallFish[i])

    fish_group.add(shark)

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        for fish in smallFish:
            fish.move_fish()
        
        shark.move_fish()

        # Draw background
        screen.blit(background_image,[0,0])

        # Game display
        fish_group.draw(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
