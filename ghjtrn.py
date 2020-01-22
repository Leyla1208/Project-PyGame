import pygame
import glob


DISPLAY_SIZE = (640, 480)
slovar = {'location_1': "resources/Горная дорога1.jpg",
          'location_2': "resources/К-1.jpeg",
          'location_3': "resources/интерьер.jpg",
          'location_4': "resources/Гостевая комната.jpg",
          'location_5': "resources/Горная дорога.png",
          'location_6': "resources/Кухня.jpg",
          'location_7': "resources/Кухня.jpg",
          'location_8': "resources/Кухня.png",
          'location_9': "resources/шкаф.jpg",
          'location_10': "resources/входная дверь.jpg", }


class ResourceManager:

    resources_folder_path = 'resources'

    def __init__(self):
        self._resources = dict()
        self._text = list()
        self._num = 1
        #  номер локации
        self._location = f'location_{self._num}'
        #  имя изображения

    def load_resources(self):
        #  создание словаря: ключ-имя -- значение-изображение
        for path in glob.glob(ResourceManager.resources_folder_path + '/*.txt'):
            file = open(path, encoding='utf8')
            self._text.append(file.read())

    def get_resource(self, name):
        pictures = name.draw(self._location)
        return pictures

    def draw(self, x_event, y_event):
        screen.fill((0, 0, 0))
        if self._num == 1:
            kar = pygame.image.load(slovar[self._location]).convert()
            pygame.transform.scale(kar, (640, 480))
            font = pygame.font.Font(None, 18)
            #  Шрифт
            text = font.render(self._text[self._num], 1, (200, 200, 255))
            #  Текст
            screen.blit(text, (10, 370))
            #  Верхний левый угол
            pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
            #  Тёмный фон
            font = pygame.font.Font(None, 14)
            text = font.render('Остаться', 1, (200, 200, 255))
            screen.blit(text, (130, 370))
            var1 = pygame.draw.rect(screen, (0, 0, 0), (120, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Пойти по дороге', 1, (200, 200, 255))
            screen.blit(text, (230, 370))
            var2 = pygame.draw.rect(screen, (0, 0, 0), (220, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Пойти к замку', 1, (200, 200, 255))
            screen.blit(text, (330, 370))
            var3 = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
            if var1.collidepoint() is True:
                font = pygame.font.Font(None, 14)
                name = open('Локация_1-1.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back1.collidepoint() is True:
                #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var2.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_1-2.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
            elif var3.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_1-3.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
        if self._num == 2:
            kar = pygame.image.load(slovar[self._location]).convert()
            pygame.transform.scale(kar, (640, 480))
            font = pygame.font.Font(None, 18)
            #  Шрифт
            text = font.render(self._text[self._num], 1, (200, 200, 255))
            #  Текст
            screen.blit(text, (10, 370))
            #  Верхний левый угол
            pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
            #  Тёмный фон
            font = pygame.font.Font(None, 14)
            text = font.render('Отойти', 1, (200, 200, 255))
            screen.blit(text, (130, 370))
            var1 = pygame.draw.rect(screen, (0, 0, 0), (120, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Не заходить', 1, (200, 200, 255))
            screen.blit(text, (230, 370))
            var2 = pygame.draw.rect(screen, (0, 0, 0), (220, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Пройти к дом', 1, (200, 200, 255))
            screen.blit(text, (330, 370))
            var3 = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
            if var1.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_2-1.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var2.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_2-2.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var3.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_2-3.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
        if self._num == 3:
            kar = pygame.image.load(slovar[self._location]).convert()
            pygame.transform.scale(kar, (640, 480))
            font = pygame.font.Font(None, 18)
            #  Шрифт
            text = font.render(self._text[self._num], 1, (200, 200, 255))
            #  Текст
            screen.blit(text, (10, 370))
            #  Верхний левый угол
            pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
            #  Тёмный фон
            font = pygame.font.Font(None, 14)
            text = font.render('Побыстрее уйти', 1, (200, 200, 255))
            screen.blit(text, (130, 370))
            var1 = pygame.draw.rect(screen, (0, 0, 0), (120, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Разговорить', 1, (200, 200, 255))
            screen.blit(text, (230, 370))
            var2 = pygame.draw.rect(screen, (0, 0, 0), (220, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Узнать совет', 1, (200, 200, 255))
            screen.blit(text, (330, 370))
            var3 = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
            if var1.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_3-1.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var2.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_3-2.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var3.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_3-3.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
        if self._num == 4:
            kar = pygame.image.load(slovar[self._location]).convert()
            pygame.transform.scale(kar, (640, 480))
            font = pygame.font.Font(None, 18)
            #  Шрифт
            text = font.render(self._text[self._num], 1, (200, 200, 255))
            #  Текст
            screen.blit(text, (10, 370))
            #  Верхний левый угол
            pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
            #  Тёмный фон
            font = pygame.font.Font(None, 14)
            text = font.render('Правая дверь', 1, (200, 200, 255))
            screen.blit(text, (130, 370))
            var1 = pygame.draw.rect(screen, (0, 0, 0), (120, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Центральная дверь', 1, (200, 200, 255))
            screen.blit(text, (230, 370))
            var2 = pygame.draw.rect(screen, (0, 0, 0), (220, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Левая дверь', 1, (200, 200, 255))
            screen.blit(text, (330, 370))
            var3 = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
            if var1.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_4-1.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var2.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_4-2.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var3.collidepoint() is True:
                    font = pygame.font.Font(None, 18)
                    name = open('Локация_4-3.txt')
                    text = font.render(name, 1, (200, 200, 255))
                    screen.blit(text, (10, 370))
                    pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                    font = pygame.font.Font(None, 14)
                    text = font.render('Назад', 1, (200, 200, 255))
                    screen.blit(text, (130, 370))
                    back = pygame.draw.rect(screen, (0, 0, 0),
                                            (120, 370, 100, 100), 1)
                    font = pygame.font.Font(None, 14)
                    text = font.render('Новая игра', 1, (200, 200, 255))
                    screen.blit(text, (230, 370))
                    all_out = pygame.draw.rect(screen, (0, 0, 0),
                                               (220, 370, 100, 100), 1)
                    font = pygame.font.Font(None, 14)
                    text = font.render('Далее', 1, (200, 200, 255))
                    screen.blit(text, (330, 370))
                    further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
        if self._num == 5:
            kar = pygame.image.load(slovar[self._location]).convert()
            pygame.transform.scale(kar, (640, 480))
            font = pygame.font.Font(None, 18)
            #  Шрифт
            text = font.render(self._text[self._num], 1, (200, 200, 255))
            #  Текст
            screen.blit(text, (10, 370))
            #  Верхний левый угол
            pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
            #  Тёмный фон
            font = pygame.font.Font(None, 14)
            text = font.render('Правая дверь', 1, (200, 200, 255))
            screen.blit(text, (130, 370))
            var1 = pygame.draw.rect(screen, (0, 0, 0), (120, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Центральная дверь', 1, (200, 200, 255))
            screen.blit(text, (230, 370))
            var2 = pygame.draw.rect(screen, (0, 0, 0), (220, 370, 100, 100), 1)
            font = pygame.font.Font(None, 14)
            text = font.render('Левая дверь', 1, (200, 200, 255))
            screen.blit(text, (330, 370))
            var3 = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
            if var1.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_5-1.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var2.collidepoint() is True:
                    font = pygame.font.Font(None, 18)
                    name = open('Локация_5-2.txt')
                    text = font.render(name, 1, (200, 200, 255))
                    screen.blit(text, (10, 370))
                    pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                    font = pygame.font.Font(None, 14)
                    text = font.render('Назад', 1, (200, 200, 255))
                    screen.blit(text, (130, 370))
                    back = pygame.draw.rect(screen, (0, 0, 0),
                                            (120, 370, 100, 100), 1)
                    font = pygame.font.Font(None, 14)
                    text = font.render('Новая игра', 1, (200, 200, 255))
                    screen.blit(text, (230, 370))
                    all_out = pygame.draw.rect(screen, (0, 0, 0),
                                               (220, 370, 100, 100), 1)
                    font = pygame.font.Font(None, 14)
                    text = font.render('Далее', 1, (200, 200, 255))
                    screen.blit(text, (330, 370))
                    further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл
            elif var3.collidepoint() is True:
                font = pygame.font.Font(None, 18)
                name = open('Локация_5-3.txt')
                text = font.render(name, 1, (200, 200, 255))
                screen.blit(text, (10, 370))
                pygame.draw.rect(screen, (0, 0, 0), (120, 140, 400, 220), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Назад', 1, (200, 200, 255))
                screen.blit(text, (130, 370))
                back = pygame.draw.rect(screen, (0, 0, 0),
                                        (120, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Новая игра', 1, (200, 200, 255))
                screen.blit(text, (230, 370))
                all_out = pygame.draw.rect(screen, (0, 0, 0),
                                           (220, 370, 100, 100), 1)
                font = pygame.font.Font(None, 14)
                text = font.render('Далее', 1, (200, 200, 255))
                screen.blit(text, (330, 370))
                further = pygame.draw.rect(screen, (0, 0, 0), (320, 370, 100, 100), 1)
                # if back.collidepoint() is True:
                #     pass
                # if all_out.collidepoint() is True:
                #                 #     pass
                #     Перенести в другой метод и оттуда вызывать начальный файл


class Mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y




class Location:
    def __init__(self):
        pass


pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)

resource_manager = ResourceManager()
resource_manager.load_resources()

#  game = Game(screen, resource_manager)
clock = pygame.time.Clock()

running = True
while running:

    dt = clock.tick()
    x_event, y_event = None, None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_event, y_event = event.pos

        #  game.process_input_event(event)
    #  game.process_input_continues(pygame.key.get_pressed(), dt)

    screen.fill((0, 0, 0))
    #  game.loop()
    resource_manager.draw(x_event, y_event)
    pygame.display.flip()

pygame.quit()
