import pygame
import sys
import os
import time
import glob


#  процедура принудительного выхода из игры
def terminate():
    pygame.quit()
    sys.exit()

#  процедура загрузки фона из файла
def load_image(filename):
    fullname = os.path.join('resources', filename)
    image = pygame.image.load(fullname).convert_alpha()
    return image

# процедура загрузки основного текста из файла
def load_text(text_name):
    font = pygame.font.Font(None, 24)
    name = open(text_name, 'r', encoding='utf8')
    text_coord = 320
    for line in name:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

#  процедура рисования рамки кнопок внизу экрана
def buttons_imgs():
    button = load_image('buttons.png').convert_alpha()
    buttons_img = pygame.transform.scale(button, (200, 75))
    screen.blit(buttons_img, (20, 690))
    screen.blit(buttons_img, (220, 690))
    screen.blit(buttons_img, (420, 690))
    screen.blit(buttons_img, (620, 690))
    screen.blit(buttons_img, (820, 690))

#  процедура печати текста на кнопках
def buttons_text(text1, text2, text3):
    font = pygame.font.Font(None, 22)
    text = font.render('Выйти из игры', 1, (200, 200, 255))
    screen.blit(text, (60, 720))
    text = font.render(text1, 1, (200, 200, 255))
    screen.blit(text, (260, 720))
    text = font.render(text2, 1, (200, 200, 255))
    screen.blit(text, (460, 720))
    text = font.render(text3, 1, (200, 200, 255))
    screen.blit(text, (660, 720))
    text = font.render('Вернуться', 1, (200, 200, 255))
    screen.blit(text, (860, 720))


#  класс курсора (изменяет системный курсор на игровой)
class Mouse_new(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        mouse_img = load_image('arrow1.png').convert_alpha()
        self.image = mouse_img
        self.rect = self.image.get_rect()

    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y


class ResourceManager(pygame.sprite.Sprite):

    def __init__(self):
        pass

    def draw(self):
        global num
        self._num = num
        screen.fill((0, 0, 0))
        #  определяем области выбора варианта действий
        var1 = pygame.draw.rect(screen, (0, 0, 0), (20, 668, 200, 100), 1)
        var2 = pygame.draw.rect(screen, (0, 0, 0), (220, 668, 200, 100), 1)
        var3 = pygame.draw.rect(screen, (0, 0, 0), (420, 668, 200, 100), 1)
        var4 = pygame.draw.rect(screen, (0, 0, 0), (620, 668, 200, 100), 1)
        var5 = pygame.draw.rect(screen, (0, 0, 0), (820, 668, 200, 100), 1)
        # первая локация
        if self._num == 1:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('Остаться', 'Пойти по дороге', 'Пойти к замку')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var2.collidepoint(event.pos):
                        num = 101  #  вариант 1.1 развития событий
                        resource_manager.draw()
                    elif var3.collidepoint(event.pos):
                        num = 102  #  вариант 1.2 развития событий
                        resource_manager.draw()
                    elif var4.collidepoint(event.pos):
                        num = 2  #  вариант 1.3 развития событий
                        resource_manager.draw()

        # вариант 1.1 развития событий
        elif self._num == 101:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 100  #  вариант 1 развития событий
                        resource_manager.draw()

        # вариант 1.2 развития событий
        elif self._num == 102:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 101  #  вариант 1 развития событий
                        resource_manager.draw()

        # вторая локация
        elif self._num == 2:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('Уйти подальше', 'Остаться у ворот', 'Пойти в дом')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var2.collidepoint(event.pos):
                        num = 201  #  вариант 1.1 развития событий
                        resource_manager.draw()
                    elif var3.collidepoint(event.pos):
                        num = 202  #  вариант 1.2 развития событий
                        resource_manager.draw()
                    elif var4.collidepoint(event.pos):
                        num = 3  #  вариант 1.3 развития событий
                        resource_manager.draw()

        elif self._num == 201:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 199  #  вариант 2 развития событий
                        resource_manager.draw()

        # вариант 1.2 развития событий
        elif self._num == 202:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 200  #  вариант 2 развития событий
                        resource_manager.draw()

        # третья локация
        elif self._num == 3:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('Побыстрей закончить', 'Разговорить', 'Спросить совета')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var2.collidepoint(event.pos):
                        num = 301  # вариант 3.1 развития событий
                        resource_manager.draw()
                    elif var3.collidepoint(event.pos):
                        num = 4  # вариант 3.3 развития событий
                        resource_manager.draw()
                    elif var4.collidepoint(event.pos):
                        num = 303  # вариант 3.2 развития событий
                        resource_manager.draw()

        elif self._num == 301:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 298  # вариант 1 развития событий

                        resource_manager.draw()

            # вариант 3.3 развития событий

        elif self._num == 303:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 299  # вариант 1 развития событий
                        resource_manager.draw()

        # четвёртая локация
        elif self._num == 4:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('Правая', 'Центральная', 'Левая')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var2.collidepoint(event.pos):
                        num = 401  # вариант 3.1 развития событий
                        resource_manager.draw()
                    elif var3.collidepoint(event.pos):
                        num = 402  # вариант 3.2 развития событий
                        resource_manager.draw()
                    elif var4.collidepoint(event.pos):
                        num = 5  # вариант 3.3 развития событий
                        resource_manager.draw()

        elif self._num == 401:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 397  # вариант 1 развития событий

                        resource_manager.draw()

            # вариант 3.2 развития событий

        elif self._num == 402:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 398  # вариант 1 развития событий
                        resource_manager.draw()

        # пятая локация
        elif self._num == 5:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('Разговорить', 'Оставить', 'Помолчать')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var2.collidepoint(event.pos):
                        num = 501  # вариант 3.1 развития событий
                        resource_manager.draw()
                    elif var3.collidepoint(event.pos):
                        num = 502  # вариант 3.2 развития событий
                        resource_manager.draw()
                    elif var4.collidepoint(event.pos):
                        num = 6  # вариант 3.3 развития событий
                        resource_manager.draw()

        elif self._num == 501:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 496  # вариант 1 развития событий

                        resource_manager.draw()

            # вариант 3.2 развития событий

        elif self._num == 502:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 497  # вариант 1 развития событий
                        resource_manager.draw()

        # шестая локация
        elif self._num == 6:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('Разговорить', 'Оставить', 'Помолчать')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var2.collidepoint(event.pos):
                        num = 601  # вариант 3.1 развития событий
                        resource_manager.draw()
                    elif var3.collidepoint(event.pos):
                        num = 602  # вариант 3.2 развития событий
                        resource_manager.draw()
                    elif var4.collidepoint(event.pos):
                        num = 7  # вариант 3.3 развития событий
                        resource_manager.draw()

        elif self._num == 601:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 595  # вариант 1 развития событий

                        resource_manager.draw()

            # вариант 3.2 развития событий

        elif self._num == 602:
            # загружаем картинку
            kar = load_image(f'{num}.jpg').convert()
            self.image = pygame.transform.scale(kar, (1024, 300))
            screen.blit(self.image, (0, 0))
            #  загружаем Текст
            load_text(f'text/Локация{num}.txt')
            #  рисуем рамки кнопок внизу экрана
            buttons_imgs()
            #  печатаем текст на кнопках
            buttons_text('', 'Дальше', '')
            #  события на экране
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if var1.collidepoint(event.pos):
                        start_screen()
                    elif var3.collidepoint(event.pos):
                        finish_screen()
                    elif var5.collidepoint(event.pos):
                        num -= 596  # вариант 1 развития событий
                        resource_manager.draw()

def start_screen():
    global num
    intro_text = ["Лабиринты",
                  "СТРАХА"]
    # рисуется фон
    fon = pygame.transform.scale(load_image('background.png'), (DISPLAY_SIZE))
    # рисуется затемнение фона
    surf = pygame.Surface((DISPLAY_SIZE), pygame.SRCALPHA)

    # цикл увеличение прозрачности (фон проявляется)
    screen.blit(fon, (0, 0))
    surf.fill((0, 0, 0, 0))
    screen.blit(surf,(0, 0))
    # for k in range(255, 0, -10):
    #     screen.blit(fon, (0, 91))
    #     surf.fill((0, 0, 0, k))
    #     screen.blit(surf,(0, 0))
    #     pygame.display.flip()
    #     time.sleep(0.1)
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
                num = 1
                return  # начинаем игру
        pygame.display.flip()


# заставка Game Over
def finish_screen():
    # рисуется фон
    fon = pygame.transform.scale(load_image('GameOver.jpg'), (DISPLAY_SIZE))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()


pygame.init()
DISPLAY_SIZE = (1024, 768)
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Лабиринты СТРАХА')
all_sprites = pygame.sprite.Group()
mouse_new = Mouse_new()
all_sprites.add(mouse_new)
# делаем системный курсор невидимым
pygame.mouse.set_visible(False)
# номер варианта развития событий
num = 0
resource_manager = ResourceManager()

running = True
while running:
    # Один раз показать заставку
    if num == 0:
        start_screen()
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
    resource_manager.draw()
    all_sprites.draw(screen)

    pygame.display.flip()

