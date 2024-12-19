import os
from icrawler.builtin import GoogleImageCrawler


def download_images(keyword: str, save_dir: str, num_images: int) -> None:
    """
    Скачивает изображения по ключевому слову.

    :param keyword: Ключевое слово для поиска (например, 'cat').
    :param save_dir: Папка для сохранения изображений.
    :param num_images: Количество изображений для скачивания.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)  # Создаем папку, если её нет

    crawler = GoogleImageCrawler(storage={'root_dir': save_dir})  # Указываем папку для сохранения
    crawler.crawl(keyword=keyword, max_num=num_images)  # Запускаем загрузку изображений
