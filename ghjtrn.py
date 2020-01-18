import pygame
import glob


DISPLAY_SIZE = (640, 480)


class ResourceManager:

    resources_folder_path = 'resources'

    def __init__(self, x, y):
        self._resources = dict()
        self._x = x
        self._y = y
        self._text = ''

    def load_resources(self):
        #  создание словаря: ключ-имя -- значение-изображение
        for path in glob.glob(ResourceManager.resources_folder_path + '/*.png'):
            name = path.split('\\')[-1].split('.')[0]
            self._resources[name] = pygame.image.load(path).convert()
        for path in glob.glob(ResourceManager.resources_folder_path + '/*.txt'):
            file = open(path)
            self._text = file.read()

    def get_resource(self, name):
        pictures = name.draw(name)
        return pictures

    def draw(self, name):
        screen.fill(0, 0, 0)
        pygame.transform.scale(name, (640, 480))
        font = pygame.font.Font(None, 50)
        text = font.render(f"{self._text}", 1, (200, 200, 255))
        screen.blit(text, (10, 370))
        pygame.draw.rect(screen, (0, 0, 0), (0, 380, 640, 440), 1)
        #  Движение текста и 40 пикселей на "кнопки"
        #  Разделить текст и сделать "кнопки выбора"



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