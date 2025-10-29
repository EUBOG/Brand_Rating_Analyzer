# Тестирование от «Workmate» - Анализ рейтинга брендов

Скрипт для генерации отчётов по CSV-файлам с товарами.

## Установка зависимостей

```bash
pip install tabulate pytest
'''
## Пример запуска

```bash
python report_generator.py --files products1.csv products2.csv --report average-rating
'''
## Добавление новых отчётов

1. Добавьте новую функцию generate_<report_name>_report(data).
2. Зарегистрируйте её в main() через if args.report == '<report_name>':.
3. Обновите choices в аргументе --report.

## Тесты

```bash
python -m pytest tests/ -v
'''
