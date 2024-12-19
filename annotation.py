import os
import csv


def create_annotation(save_dir: str, csv_file: str) -> None:
    """
    Создает CSV-файл с аннотацией (пути к изображениям).

    :param save_dir: Папка, где хранятся изображения.
    :param csv_file: Путь к файлу CSV.
    """
    image_paths = []  # Список для путей к изображениям

    for root, _, files in os.walk(save_dir):  # Проходим по всем файлам в папке
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):  # Проверяем, что это изображение
                absolute_path = os.path.join(root, file)  # Абсолютный путь к файлу
                relative_path = os.path.relpath(absolute_path, save_dir)  # Относительный путь
                image_paths.append((absolute_path, relative_path))  # Сохраняем пути в список

    # Записываем пути в CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['absolute_path', 'relative_path'])  # Заголовки для CSV
        writer.writerows(image_paths)  # Записываем пути из списка


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
