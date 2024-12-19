import argparse
from downloader import download_images
from annotation import create_annotation, ImageIterator


def parse_args():
    """
    Разбирает аргументы командной строки.
    """
    parser = argparse.ArgumentParser(description="Скачивание изображений и создание аннотации.")
    parser.add_argument('keyword', type=str, help="Ключевое слово для поиска изображений.")
    parser.add_argument('save_dir', type=str, help="Папка для сохранения изображений.")
    parser.add_argument('csv_file', type=str, help="Путь к файлу аннотации.")
    parser.add_argument('num_images', type=int, help="Количество изображений для скачивания (50-1000).")
    return parser.parse_args()


def main():
    """
    Главная функция программы.
    """
    args = parse_args()  # Разбираем аргументы командной строки

    # Скачиваем изображения
    print(f"Скачивание {args.num_images} изображений по ключевому слову '{args.keyword}'...")
    download_images(args.keyword, args.save_dir, args.num_images)
    print(f"Изображения сохранены в папке: {args.save_dir}")

    # Создаем аннотацию
    print(f"Создание аннотации в файле: {args.csv_file}...")
    create_annotation(args.save_dir, args.csv_file)
    print(f"Аннотация успешно создана.")

    # Итерация по изображениям
    print("Итерация по изображениям:")
    iterator = ImageIterator(args.csv_file)
    for absolute_path, relative_path in iterator:
        print(f"Абсолютный путь: {absolute_path}, Относительный путь: {relative_path}")


if __name__ == '__main__':
    main()
