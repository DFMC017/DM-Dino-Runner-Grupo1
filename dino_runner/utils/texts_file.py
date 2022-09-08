import pygame

FONT_FAMILY = 'freesansbold.ttf'
FONT_COLOR_BLACK = (0, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FONT_FAMILY, 20)

    text = font.render('SCORE: ' + str(points), True, FONT_COLOR_BLACK)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)

    return text, text_rect