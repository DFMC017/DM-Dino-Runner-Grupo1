import pygame

FONT_FAMILY = 'freesansbold.ttf'
FONT_COLOR_BLACK = (0, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FONT_FAMILY, 30)

    text = font.render('TU PUNTAJE ES: ' + str(points), True, FONT_COLOR_BLACK)
    text_rect = text.get_rect()
    text_rect.center = (500, 500)

    return text, text_rect

def get_text_element(text_to_display, height, width):
    font = pygame.font.Font(FONT_FAMILY, 40)

    text = font.render(text_to_display, True, FONT_COLOR_BLACK)
    text_rect = text.get_rect()
    text_rect.center = (height, width)

    return text, text_rect