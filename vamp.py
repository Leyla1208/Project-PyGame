import pygame
import sys
import os
import time
import glob


DISPLAY_SIZE = (1024, 768)
slovar = {'location_1': "resources/Горная дорога1.jpg",
          'location_2': "resources/К-1.jpeg",
          'location_3': "resources/интерьер.jpg",
          'location_4': "resources/Гостевая комната.jpg",
          'location_5': "resources/Горная дорога.png",
          'location_6': "resources/Кухня.jpg",
          'location_7': "resources/Кухня.jpg",
          'location_8': "resources/Кухня.png",
          'location_9': "resources/шкаф.jpg",
          'location_10': "resources/входная дверь.jpg",
          'location_1_0': "resources/Локация_1.txt",}

def load_image(filename):
    fullname = os.path.join('resources', filename)
    image = pygame.image.load(fullname).convert_alpha()
    return image

class Mouse_new(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        mouse_img = load_image('arrow1.png').convert_alpha()
        self.image = mouse_img
        self.rect = self.image.get_rect()

    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y


# class ResourceManager:
#
#     resources_folder_path = 'resources'
#
#     def __init__(self, num1):
#         self._resources = dict()
#         self._text = list()
#         self._num = num1
#         #  номер локации
#         self._location = f"location_{self._num}"
#         #  имя изображения
#
#     def load_resources(self):
#         #  создание словаря: ключ-имя -- значение-изображение
#         #  исправить !!!
#         for path in glob.glob('*.txt'):
#             file = open(path, encoding='utf8')
#             self._text.append(file.read())
#
#     def get_resource(self, name):
#         pictures = name.draw(self._location)
#         return pictures
#
#     def draw(self):
#         global further, back, all_out
#         screen.fill((0, 0, 0))
#         if self._num == 1:
#             kar = pygame.image.load(slovar[self._location]).convert()
#             self.image = pygame.transform.scale(kar, (1024, 768))
#             screen.blit(self.image, (0, 0))
#             #  Шрифт
#             font = pygame.font.Font(None, 18)
#             name = open('resources/location_1.txt', 'r', encoding='utf8')
#             text = font.render('asdf', 1, (200, 200, 255))
#             #  Текст   !!!!!!!!!!!!!!!!!
#             screen.blit(text, (10, 370))
#             #  Верхний левый угол
#             pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
#             #  Тёмный фон
#             font = pygame.font.Font(None, 16)
#             text = font.render('Остаться', 1, (200, 200, 255))
#             screen.blit(text, (240, 700))
#             var1 = pygame.draw.rect(screen, (0, 0, 0), (230, 700, 200, 100), 1)
#             font = pygame.font.Font(None, 16)
#             text = font.render('Пойти по дороге', 1, (200, 200, 255))
#             screen.blit(text, (440, 700))
#             var2 = pygame.draw.rect(screen, (0, 0, 0), (430, 700, 200, 100), 1)
#             font = pygame.font.Font(None, 16)
#             text = font.render('Пойти к замку', 1, (200, 200, 255))
#             screen.blit(text, (640, 700))
#             var3 = pygame.draw.rect(screen, (0, 0, 0), (630, 700, 200, 100), 1)
#             for i in pygame.event.get():
#                 if i.type == pygame.MOUSEBUTTONUP:
#                     if var1.collidepoint(i.pos):
#                 #
#                 # elif rect_right.collidepoint(i.pos):
#                 #
#                 #
#                 # if var1.collidepoint() is True:
#                         font = pygame.font.Font(None, 16)
#                         name = open('Локация_1_1.txt')
#                         text = font.render(name, 1, (200, 200, 255))
#                         screen.blit(text, (10, 370))
#                         pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Назад', 1, (200, 200, 255))
#                         screen.blit(text, (130, 370))
#                         back = pygame.draw.rect(screen, (0, 0, 0),
#                                                 (230, 370, 100, 100), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Новая игра', 1, (200, 200, 255))
#                         screen.blit(text, (230, 370))
#                         all_out = pygame.draw.rect(screen, (0, 0, 0),
#                                                    (340, 370, 100, 100), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Далее', 1, (200, 200, 255))
#                         screen.blit(text, (330, 370))
#                         further = pygame.draw.rect(screen, (0, 0, 0),
#                                                    (450, 370, 100, 100), 1)
#
#                 # elif var2.collidepoint() is True:
#                     elif var2.collidepoint(i.pos):
#                         font = pygame.font.Font(None, 18)
#                         intro_text = open('resources/Локация_1_2.txt')
#                         text_coord = 50
#
#                         for line in intro_text:
#                             string_rendered = font.render(line, 1, pygame.Color('black'))
#                             intro_rect = string_rendered.get_rect()
#                             text_coord += 10
#                             intro_rect.top = text_coord
#                             intro_rect.x = 10
#                             text_coord += intro_rect.height
#                             screen.blit(string_rendered, intro_rect)
#
#
#                         # text = font.render(name, 1, (200, 200, 255))
#                         # screen.blit(text, (10, 370))
#                         pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Назад', 1, (200, 200, 255))
#                         screen.blit(text, (130, 370))
#                         back = pygame.draw.rect(screen, (0, 0, 0),
#                                                 (230, 370, 100, 100), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Новая игра', 1, (200, 200, 255))
#                         screen.blit(text, (230, 370))
#                         all_out = pygame.draw.rect(screen, (0, 0, 0),
#                                                    (340, 370, 100, 100), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Далее', 1, (200, 200, 255))
#                         screen.blit(text, (330, 370))
#                         further = pygame.draw.rect(screen, (0, 0, 0),
#                                                    (450, 370, 100, 100), 1)
#                     elif var3.collidepoint(i.pos):
#                 # elif var3.collidepoint() is True:
#                         font = pygame.font.Font(None, 18)
#                         name = open('Локация_1_3.txt')
#                         text = font.render(name, 1, (200, 200, 255))
#                         screen.blit(text, (10, 370))
#                         pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Назад', 1, (200, 200, 255))
#                         screen.blit(text, (130, 370))
#                         back = pygame.draw.rect(screen, (0, 0, 0),
#                                                 (230, 370, 100, 100), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Новая игра', 1, (200, 200, 255))
#                         screen.blit(text, (230, 370))
#                         all_out = pygame.draw.rect(screen, (0, 0, 0),
#                                                    (340, 370, 100, 100), 1)
#                         font = pygame.font.Font(None, 16)
#                         text = font.render('Далее', 1, (200, 200, 255))
#                         screen.blit(text, (330, 370))
#                         further = pygame.draw.rect(screen, (0, 0, 0),
#                                                    (450, 370, 100, 100), 1)

def start_screen():
    # intro_text = ["ЗАСТАВКА", "",
    #               "Правила игры",
    #               "Если в правилах несколько строк,",
    #               "приходится выводить их построчно"]
    intro_text = ["Лабиринты",
                  "СТРАХА"]
    # рисуется фон
    fon = pygame.transform.scale(load_image('background.png'), (1024,576))
    # рисуется затемнение фона
    surf = pygame.Surface((DISPLAY_SIZE), pygame.SRCALPHA)
    for k in range(255, 0, -10):
        screen.blit(fon, (0, 91))
        surf.fill((0, 0, 0, k))
        screen.blit(surf,(0, 0))
        pygame.display.flip()
        time.sleep(0.2)
    font = pygame.font.Font(None, 50)
    text_coord = 450
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 650
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)
all_sprites = pygame.sprite.Group()
mouse_new = Mouse_new()
all_sprites.add(mouse_new)
pygame.mouse.set_visible(False)

# resource_manager = ResourceManager(num)
# resource_manager.load_resources()

#  game = Game(screen, resource_manager)
# clock = pygame.time.Clock()
n = 0
running = True
while running:
    # Один раз показать заставку
    if n == 0:
        start_screen()
        n += 1
    # clock.tick(50)
    x_event, y_event = None, None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # Mouse(*event.pos)
        #     pass
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    all_sprites.update(pos[0], pos[1])
    screen.fill((255, 0, 255))
    all_sprites.draw(screen)
    # resource_manager.draw()
    pygame.display.flip()

# pygame.quit()
# print('New Game')
