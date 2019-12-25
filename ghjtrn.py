import pygame


DISPLAY_SIZE = (640, 480)


class GameWorld:

    def __init__(self, start_x, start_y):
        pass

    def add_ball(self, ball):
        pass

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
        pass


class Game:

    def __init__(self, surf):
        self._world = GameWorld(10, 10)
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

game = Game(screen)
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

print()
