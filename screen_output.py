import pygame
import dangerous_diving
import score as total

GAME_WIDTH = 1152
GAME_HEIGHT = 648

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
                dangerous_diving.main()


        pygame.display.update()
        clock.tick(6)
        
    pygame.quit()      

def win_screen():
    pygame.init()
    #global total.totalscore
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
                total.totalscore = 0
                dangerous_diving.main()

        draw_text(screen,('Your score: %d' % total.totalscore), 60, GAME_WIDTH / 2, GAME_HEIGHT / 3, (255,255,255))
        draw_text(screen,('Press any key to play again'), 60, GAME_WIDTH / 2, 430, (255,128,0))
        draw_text(screen,('YOU WON!'), 68, GAME_WIDTH / 2, GAME_HEIGHT / 2, (255,255,255))

        pygame.display.update()
        
    pygame.quit()

def lose_screen():
    pygame.init()

    #global total.totalscore
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
                total.totalscore = 0
                dangerous_diving.main()

        draw_text(screen,('Your score: %d' % total.totalscore), 60, GAME_WIDTH / 2, GAME_HEIGHT / 3, (255,255,255))
        draw_text(screen,('Press any key to play again'), 60, GAME_WIDTH / 2, 430, (255,128,0))
        draw_text(screen,('YOU LOST!'), 68, GAME_WIDTH / 2, GAME_HEIGHT / 2, (255,255,255))

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

def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font('font/videophreak.ttf', size)
    text_surface = font.render(text, True, (255,165,0))
    text_surface2 = font.render(text, True, color)

    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)

    surf.blit(text_surface, [text_rect.x + 2,text_rect.y +2])
    surf.blit(text_surface2, text_rect)