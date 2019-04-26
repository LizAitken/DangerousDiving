import pygame

# Add in keys
KEY_UP = 273
KEY_DOWN = 274

# Created Player class
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
    def __init__(self, image, pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([200, 60])
            color = self.image.fill((255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.center = pos
            

class HealthWhite(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 60])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos

class HealthRed(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 60])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos



def main():
    width = 1152
    height = 648

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load('My_images/2_game_background.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, [width, height])
    pygame.display.set_caption('Dangerous Diving')
    # clock = pygame.time.Clock()

    # Our Player
    player = Player(185, 320)
    # Our Health_box
    # white_box = HealthWhite([1038, 605])
    # green_box = HealthGreen([1038, 605])
    # red_box = HealthRed([1038, 605])
    # Adding the player to a group
    player_group = pygame.sprite.Group()
    player_group.add(player)
    # Adding the health box to a group
    health_group = pygame.sprite.Group()
    health_group.add(white_box)


    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
            # Event handling
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
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
        # Draw background
        screen.blit(background_image,[0, 0])

        # Game display
        # Draw player and health to screen
        player_group.draw(screen)
        health_group.draw(screen)
        
        pygame.display.update()
        # clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()