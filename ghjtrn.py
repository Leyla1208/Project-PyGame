import pygame


DISPLAY_SIZE = (640, 480)
new_file = 1
BALL_SPEED = 50 / 1000


class Text:

    def __init__(self, x, y):
        self._coords = (x, y)

    def move(self, delta_pos):
        self._coords = (self._coords[0] + delta_pos[0],
                        self._coords[1] + delta_pos[1])

    def get_position(self):
        return self._coords


class GameWorld:

    def __init__(self, start_x, start_y):
        self._player = Text(start_x, start_y)
        self._balls = list()

    def add_ball(self, ball):
        global num_file
        # Переключение текстов(файлов)
        if num_file == 2:
            new_surf = pygame.image.load('dog.bmp')
            new_rect = new_surf.get_rect(bottomright=(400, 300))
            screen.blit(new_surf, new_rect)

    def process_input_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Если нажали левую кнопку мыши
            # Замена текста Найти!!!!!
            self.add_ball(Text(*event.pos))

    def process_input_continues(self, pressed_keys, dt):
        # Переделать на фоновое изображение

        if pressed_keys[pygame.K_UP]:
            self._player.move((0, -BALL_SPEED * dt))
        elif pressed_keys[pygame.K_DOWN]:
            self._player.move((0, BALL_SPEED * dt))
        elif pressed_keys[pygame.K_d]:
            self._player.move((BALL_SPEED * dt, 0))
        elif pressed_keys[pygame.K_a]:
            self._player.move((-BALL_SPEED * dt, 0))

    def update(self):
        pl_x, pl_y = self._player.get_position()
        for ball in self._balls:
            bl_x, bl_y = ball.get_position()
            dist_vector = (pl_x - bl_x, pl_y - bl_y)
            dist = (dist_vector[0] ** 2 + dist_vector[1] ** 2) ** 0.5
            if dist < 2 * 10:
                pen_depth = 2 * 10 - dist
                self._player.move((dist_vector[0] / dist * pen_depth,
                                  dist_vector[1] / dist * pen_depth))

    def draw(self, surf):
        pl_x, pl_y = self._player.get_position()
        pygame.draw.ellipse(surf, pygame.Color(255, 255, 255),
                            (pl_x - 10, pl_y - 10, 20, 20))
        for ball in self._balls:
            bl_x, bl_y = ball.get_position()
            pygame.draw.ellipse(surf, pygame.Color(255, 255, 255),
                                (bl_x - 10, bl_y - 10, 20, 20))


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
