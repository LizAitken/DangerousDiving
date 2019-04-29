import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.player_health = 10
        self.score = 0
        self.x = x
        self.y = y

        self.size = [250,50]
        self.speed_y = 0
        self.radius = 50

        #Animation
        self.index = 0
        self.images = []
        self.images.append(pygame.image.load('My_images/divercrop_1pixel.png'))
        self.images.append(pygame.image.load('My_images/divercrop_5pixel.png'))
        self.images.append(pygame.image.load('My_images/divercrop_4pixel.png'))
        self.images.append(pygame.image.load('My_images/divercrop_2pixellower.png'))

        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (self.size[0], self.size[1]))

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        self.move_image = 0

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
        if self.move_image == 3:
            self.move_image = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        else:
            self.move_image += 1
    #def hurt(self):