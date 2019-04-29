import pygame

global totalscore
totalscore = 0

GAME_WIDTH = 1152
GAME_HEIGHT = 648

# Add in keys
KEY_UP = 273
KEY_DOWN = 274

def addScore(score):
    global totalscore
    score_sound = pygame.mixer.Sound('sounds/score.wav')
    if(score > 0):
        score_sound.play()
        totalscore += score

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = totalscore
        
    def show_score(self,screen):
        font_back = pygame.font.Font('font/videophreak.ttf', 30)
        font_front = pygame.font.Font('font/videophreak.ttf', 30)
        text = font_back.render('SCORE  : %d' % totalscore, True, (169,169,169))
        text2 = font_front.render('SCORE  : %d' % totalscore, True, (255,165,0))

        screen.blit(text, (GAME_WIDTH/2-text.get_width()/2, 20))
        screen.blit(text2, (GAME_WIDTH/2-text2.get_width()/2, 22))