import pygame
import glob


DISPLAY_SIZE = (640, 480)


class ResourceManager:

    resources_folder_path = 'resources'

    def __init__(self):
        self._resources = dict()

    def load_resources(self):
        for path in glob.glob(ResourceManager.resources_folder_path + '/*.png'):
            name = path.split('\\')[-1].split('.')[0]
            self._resources[name] = pygame.image.load(path).convert()

    def get_resource(self, name):
        return self._resources[name]


class Level:

    def __init__(self, background_name, resource_manager):
        self._background = pygame.sprite.Sprite()
        self._background.image = pygame.transform.scale(resource_manager.get_resource(background_name), DISPLAY_SIZE)
        self._background.rect = self._background.image.get_rect()
        self._spritegroup = pygame.sprite.Group()
        self._spritegroup.add(self._background)

    def draw(self, surf):
        self._spritegroup.draw(surf)


class GameWorld:

    def __init__(self, resource_manager):
        self._level = Level('background', resource_manager)

    def process_input_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Если нажали левую кнопку мыши
            # Замена текста Найти!!!!!
            pass

    def process_input_continues(self, pressed_keys, dt):
        # Переделать на фоновое изображение

        pass

    def update(self):
        pass

    def draw(self, surf):
        self._level.draw(surf)


class Game:

    def __init__(self, surf, resource_manager):
        self._world = GameWorld(resource_manager)
        self._surf = surf

    def loop(self):
        self._world.update()
        self._world.draw(self._surf)

    def process_input_event(self, event):
        self._world.process_input_event(event)

    def process_input_continues(self, pressed_keys, dt):
        self._world.process_input_continues(pressed_keys, dt)


pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)

resource_manager = ResourceManager()
resource_manager.load_resources()

game = Game(screen, resource_manager)
clock = pygame.time.Clock()

running = True
while running:

    dt = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        game.process_input_event(event)
    game.process_input_continues(pygame.key.get_pressed(), dt)

    screen.fill((0, 0, 0))
    game.loop()
    pygame.display.flip()

pygame.quit()
