import pygame
import glob


DISPLAY_SIZE = (640, 480)
dictionary = {'location_1': "Горная дорога1.jpg",
          'location_2': "К-1.jpeg",
          'location_3': "интерьер.jpg",
          'location_4': "Гостевая комната.jpg",
          'location_5': "Горная дорога.png",
          'location_6': "Кухня.jpg",
          'location_7': "Кухня.jpg",
          'location_8': "Кухня.png",
          'location_9': "шкаф.jpg",
          'location_10': "входная дверь.jpg", }


class ResourceManager:

    resources_folder_path = 'resources'

    def __init__(self, x, y):
        self._resources = dict()
        self._text = ''
        self._num = 1
        #  номер локации
        self._location = f'location_{self._num}'
        #  имя изображения

    def load_resources(self):
        #  создание словаря: ключ-имя -- значение-изображение
        for path in glob.glob(ResourceManager.resources_folder_path + '/*.txt'):
            file = open(path)
            self._text = file.read()

    def get_resource(self, name):
        pictures = name.draw(self._location)
        return pictures

    def draw(self):
        screen.fill(0, 0, 0)
        pygame.transform.scale(open(slovar[self._location]), (640, 480))
        font = pygame.font.Font(None, 18)
        text = font.render(f"{self._text}", 1, (200, 200, 255))
        screen.blit(text, (10, 370))
        pygame.draw.rect(screen, (0, 0, 0), (120, 140, 520, 360), 1)
        font = pygame.font.Font(None, 14)
        text = font.render('Остаться', 1, (200, 200, 255))
        screen.blit(text, (130, 150))
        pygame.draw.rect(screen, (0, 0, 0), (530, 370, 630, 470), 1)
        font = pygame.font.Font(None, 14)
        text = font.render('Остаться', 1, (200, 200, 255))
        screen.blit(text, (130, 150))
        pygame.draw.rect(screen, (0, 0, 0), (530, 370, 630, 470), 1)
        font = pygame.font.Font(None, 14)
        text = font.render('Остаться', 1, (200, 200, 255))
        screen.blit(text, (130, 150))
        pygame.draw.rect(screen, (0, 0, 0), (530, 370, 630, 470), 1)
        #  Разделить текст и сделать "кнопки выбора"

class Level:

    def __init__(self, background_name, resource_manager):
        self._background = pygame.sprite.Sprite()
        self._background.image = pygame.transform.scale(resource_manager.get_resource(background_name), DISPLAY_SIZE)
        self._background.rect = self._background.image.get_rect()
        self._spritegroup = pygame.sprite.Group()
        self._spritegroup.add(self._background)

    def draw(self, surf):
        self._spritegroup.draw(surf)


pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)

resource_manager = ResourceManager(x_event, y_event)
resource_manager.load_resources()

game = Game(screen, resource_manager)
clock = pygame.time.Clock()

running = True
while running:

    dt = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_event, y_event = event.pos

        game.process_input_event(event)
    game.process_input_continues(pygame.key.get_pressed(), dt)

    screen.fill((0, 0, 0))
    game.loop()
    pygame.display.flip()

pygame.quit()
print('New Game')


pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)

resource_manager = ResourceManager(x_event, y_event)
resource_manager.load_resources()

game = Game(screen, resource_manager)
clock = pygame.time.Clock()

running = True
while running:

    dt = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_event, y_event = event.pos

        game.process_input_event(event)
    game.process_input_continues(pygame.key.get_pressed(), dt)

    screen.fill((0, 0, 0))
    game.loop()
    pygame.display.flip()

pygame.quit()
print('New Game')