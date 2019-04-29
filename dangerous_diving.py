import pygame
import random
import time
from datetime import datetime

GAME_WIDTH = 1152
GAME_HEIGHT = 648

# Add in keys
KEY_UP = 273
KEY_DOWN = 274

global ticks
ticks = 0

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
        self.radius = 3
        self.total_score = 0

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

totalscore = 0

def addScore(score):
    global totalscore
    totalscore += score

def resetScore():
    totalscore = 0

class Fish(Ocean):
    def __init__(self,image):
        super().__init__(image)
        self.image = pygame.transform.scale(image, (self.size[0], self.size[1]))
        self.image_original = image
        self.rect = self.image.get_rect()
        self.rect.x = GAME_WIDTH
        self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        self.fish_sound = pygame.mixer.Sound('sounds/chomp.wav')

    def move_object(self):
        if self.rect.x  <= 0 - self.size[0]:
            addScore(self.score)
            self.randomize_size = random.randint(10,100)
            self.size = [self.randomize_size*3,self.randomize_size]
            self.score = self.size[0]*self.size[1]
            self.image = pygame.transform.scale(self.image_original, (self.size[0], self.size[1]))
            self.rect = self.image.get_rect()
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        else:
            self.rect.x -= self.speed

class Shark(Ocean):
    def __init__(self,image):
        super().__init__(image)
        self.size = [400,150]
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.image_original = image
        self.speed = 30
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 2000

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
        self.show = True
        self.coin_sound = pygame.mixer.Sound('sounds/coin_sound.wav')


    def move_object(self):

        if self.show_wait == self.show_random:
            self.show = True
            self.show_wait = 0 
        elif self.show == True and self.rect.x > (0-self.size[0]):
            self.rect.x -= self.speed
        elif self.show == True and self.rect.x <= (0-self.size[0]):
            self.show = False
            self.show_random = random.randint(500,1000)
            self.rect.x = GAME_WIDTH
            self.rect.y = random.randint(self.size[1], (GAME_HEIGHT-self.size[1]))
        else:
            self.show_wait += 1

    def animation(self):
        pass
        

class Game():
    pass

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

class Health(pygame.sprite.Sprite):
    def __init__(self,life):
        pygame.sprite.Sprite.__init__(self)
        # Life has to be set from 1-10
        self.life = life
        self.images = []

        for i in range(self.life + 1):
            self.images.append(pygame.image.load('My_images/life/life%d.png'%i).convert_alpha())
        self.image = self.images[10]
        #self.image.fill((255, 255, 255))
        self.index = 0
        self.rect = self.image.get_rect()
        self.rect.center = [GAME_WIDTH - (self.rect.width/2) -20, GAME_HEIGHT - (self.rect.height/2) - 20]
    
    def damage(self,damage):
        self.image = self.images[damage]

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = totalscore
        #self.spritesheet =  pygame.image.load('My_images/fishSpriteSheet/fishSpritesheet.png').convert_alpha()
        
    def show_score(self,screen):
        font_back = pygame.font.Font('font/videophreak.ttf', 30)
        font_front = pygame.font.Font('font/videophreak.ttf', 30)
        text = font_back.render('SCORE  : %d' % totalscore, True, (169,169,169))
        text2 = font_front.render('SCORE  : %d' % totalscore, True, (255,165,0))
        #print(text.get_width())
        screen.blit(text, (GAME_WIDTH/2-text.get_width()/2, 20))
        screen.blit(text2, (GAME_WIDTH/2-text2.get_width()/2, 22))

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, [0,0,0])
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def intro_screen():
    pygame.init()

    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    enter_image = pygame.image.load('My_images/1_game_backgroundREDO.png').convert_alpha()
    enter_image = pygame.transform.scale(enter_image, [GAME_WIDTH, GAME_HEIGHT])
    pygame.display.set_caption('Dangerous Diving')
    clock = pygame.time.Clock()
    intro = True

    while intro:
        screen.blit(enter_image,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                intro = False
                main()


        pygame.display.update()
        clock.tick(6)
        
    pygame.quit()      


def win_screen():
    pygame.init()
    global totalscore
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    end_image = pygame.image.load('My_images/4_game_background.png').convert_alpha()
    end_image = pygame.transform.scale(end_image, [GAME_WIDTH, GAME_HEIGHT])
    pygame.display.set_caption('Dangerous Diving')

    run = True
    while run:
        screen.blit(end_image,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                run = False
                totalscore = 0
                main()

        draw_text(screen,('Your score: %d' % totalscore), 60, GAME_WIDTH / 2, GAME_HEIGHT / 3)
        draw_text(screen,('Press any key to play again'), 60, GAME_WIDTH / 2, 430)
        draw_text(screen,('YOU WON!'), 68, GAME_WIDTH / 2, GAME_HEIGHT / 2)

        pygame.display.update()
        
    pygame.quit()

def lose_screen():
    pygame.init()

    global totalscore
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    end_image = pygame.image.load('My_images/4_game_background.png').convert_alpha()
    end_image = pygame.transform.scale(end_image, [GAME_WIDTH, GAME_HEIGHT])
    pygame.display.set_caption('Dangerous Diving')
    
    run = True
    while run:
        screen.blit(end_image,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                run = False
                ticks = 0
                totalscore = 0
                main()

        draw_text(screen,('Your score: %d' % totalscore), 60, GAME_WIDTH / 2, GAME_HEIGHT / 3)
        draw_text(screen,('Press any key to play again'), 60, GAME_WIDTH / 2, 430)
        draw_text(screen,('YOU LOST!'), 68, GAME_WIDTH / 2, GAME_HEIGHT / 2)

        pygame.display.update()
        
    pygame.quit()

# Side scroll from : https://gamedev.stackexchange.com/questions/126046/how-to-make-a-moving-background-with-pygame
class Background():
    def __init__(self,surface):
        self.bgimage = pygame.image.load('My_images/2_game_background.png')
        self.rectBGimg = self.bgimage.get_rect()
        self.bgimage = pygame.transform.scale(self.bgimage, (GAME_WIDTH,GAME_HEIGHT))
        self.rectBGimg = self.bgimage.get_rect()
        self.surface = surface
        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.movingUpSpeed = 2

    def update(self):
        self.bgX1 -= self.movingUpSpeed
        self.bgX2 -= self.movingUpSpeed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        self.surface.blit(self.bgimage, (self.bgX1, self.bgY1))
        self.surface.blit(self.bgimage, (self.bgX2, self.bgY2))

def main():

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

    # Game initialization
    game_over = True
    running = True

    second_start = int(time.strftime("%S", time.gmtime()))
    minute_start = int(time.strftime("%M", time.gmtime()))


    while running:

        #Timer
        elpased_second = int(time.strftime("%S", time.gmtime()))
        elapsed_minute = int(time.strftime("%M", time.gmtime()))

        minute_timer = elapsed_minute - minute_start
        second_timer = elpased_second - second_start + (minute_timer * 60)

        if second_timer >= 60:
            running = False
            win_screen()

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
            time.sleep(3)
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
                    thing.coin_sound.play()
                elif 'Shark' in str(thing):
                    player.player_health -= 10
                elif 'Fish' in str(thing):
                    thing.fish_sound.play()
                    thing.score = 0
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
        draw_text(screen,('%d' % (second_timer)), 45, 1030, 20)

        pygame.display.update()

    pygame.quit()

intro_screen()
if __name__ == '__main__':
#    main()
    pass
