import argparse
import csv
from collections import defaultdict
from typing import List, Dict
from tabulate import tabulate


def read_csv_files(file_paths: List[str]) -> List[Dict[str, str]]:
    """Читает несколько CSV-файлов и возвращает список всех строк как словари."""
    all_rows = []
    for file_path in file_paths:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_rows.append(row)
    return all_rows


def calculate_average_rating(data: List[Dict[str, str]]) -> List[Dict[str, float]]:
    """Вычисляет средний рейтинг по каждому бренду и возвращает отсортированный список."""
    brand_ratings = defaultdict(list)

    for row in data:
        brand = row['brand'].strip()
        rating = float(row['rating'].strip())
        brand_ratings[brand].append(rating)

    average_ratings = [
        {'brand': brand, 'average_rating': sum(ratings) / len(ratings)}
        for brand, ratings in brand_ratings.items()
    ]

    # Сортировка по убыванию среднего рейтинга
    average_ratings.sort(key=lambda x: x['average_rating'], reverse=True)
    return average_ratings


def generate_average_rating_report(data: List[Dict[str, str]]) -> str:
    report_data = calculate_average_rating(data)
    table = [
        [item['brand'], f"{item['average_rating']:.2f}"]
        for item in report_data
    ]
    return tabulate(table, headers=["brand", "average_rating"], tablefmt="grid", disable_numparse=True)


def main():
    parser = argparse.ArgumentParser(description="Генерация отчётов по CSV-файлам с товарами.")
    parser.add_argument('--files', nargs='+', required=True, help="Пути к CSV-файлам")
    parser.add_argument('--report', required=True, choices=['average-rating'], help="Название отчёта")

    args = parser.parse_args()

    data = read_csv_files(args.files)

    if args.report == 'average-rating':
        output = generate_average_rating_report(data)
        print(output)
    else:
        raise ValueError(f"Неизвестный тип отчёта: {args.report}")


if __name__ == '__main__':
    main()