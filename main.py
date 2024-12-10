import argparse
import re

class ProfileCounter:
    """Класс для подсчета анкет мужчин в файле"""

    def __init__(self, filename):
        """Конструктор класса"""
        self.filename = filename

    def read_file(self):
        """Читает содержимое файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print("Файл не найден. Убедитесь, что имя файла введено правильно.")
            return None
        

    def count_men(self, data):
        """Считает количество анкет мужчин"""
        if data is None:
            return 0
        # Ищем анкеты мужского пола
        return len(re.findall(r'\bМужской\b', data))


def main():

    # Настраиваем парсер аргументов
    parser = argparse.ArgumentParser(description="Подсчет анкет мужчин в указанном файле.")
    parser.add_argument("filename", type=str, help="Путь к файлу, содержащему анкеты.")

    # Парсим аргументы командной строки
    args = parser.parse_args()

    # Создаем объект счетчика
    counter = ProfileCounter(args.filename)

    # Читаем файл
    data = counter.read_file()

    # Считаем количество анкет мужчин
    men_count = counter.count_men(data)

    # Выводим результат
    print(f"Количество анкет мужчин: {men_count}")


if __name__ == "__main__":
    main()
