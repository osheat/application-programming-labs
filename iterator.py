import os
import csv


class ImageIterator:
    """
    Итератор для обхода изображений.
    """

    def __init__(self, source: str) -> None:
        """
        Инициализация итератора.

        :param source: Путь к файлу аннотации (CSV) или папке.
        """
        self.images = []  # Список изображений
        if os.path.isfile(source) and source.endswith('.csv'):  # Если это CSV-файл
            with open(source, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Пропускаем заголовок
                self.images = [(row[0], row[1]) for row in reader]  # Читаем строки из CSV
        elif os.path.isdir(source):  # Если это папка
            for root, _, files in os.walk(source):
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):  # Проверяем изображения
                        absolute_path = os.path.join(root, file)
                        relative_path = os.path.relpath(absolute_path, source)
                        self.images.append((absolute_path, relative_path))

    def __iter__(self):
        return iter(self.images)  # Возвращаем итератор по списку
