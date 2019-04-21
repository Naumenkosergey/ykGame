import pygame

class Text:
    def __init__(self,font_color,font_type,font_size):
        self.font_color=font_color
        self.font_type=font_type
        self.font_size=font_size

    def print_text(self, window, message, x, y):
        font_type = pygame.font.Font(self.font_type, self.font_size)
        text = font_type.render(message, True, self.font_color)
        window.blit(text, (x, y - 5))