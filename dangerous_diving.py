import pygame
import random

game_width = 1152
game_height = 648

class Fish(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        pygame.sprite.Sprite.__init__(self)
        # size is set by width then height
        self.size = [size*2.2,size]
        self.image = pygame.Surface(self.size)
        self.image.fill((255, 0, 0))
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move_fish(self):
        if self.rect.x  <= 0 - self.rect.width:
            self.rect.x = game_width
            self.rect.y = random.randint(self.rect.height, (game_height-self.rect.height))
        else:
            self.rect.x -= 50

        #self.rect.center = [self.rect.x,self.rect.y]

    def render(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

def main():

    pygame.init()

    screen = pygame.display.set_mode((game_width, game_height))
    background_image = pygame.image.load('My_images/2_game_background.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (game_width, game_height))

    pygame.display.set_caption('Dangerous Diving')
    clock = pygame.time.Clock()

    # Game initialization
    smallFish = []
    fish_group = pygame.sprite.Group()


    for i in range(10):
        randomY = random.randint(0,game_height)
        smallFish.append(Fish(10,[game_width,randomY]))
        fish_group.add(smallFish[i])

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        for fish in smallFish:
            fish.move_fish()

        # Draw background
        screen.blit(background_image,[0,0])

        # Game display
        fish_group.draw(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
