import tempfile
import os
from report_generator import read_csv_files, generate_average_rating_report

# Тестовые данные — такие же, как в ваших юнит-тестах
content1 = """name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6"""

content2 = """name,brand,price,rating
poco x5 pro,xiaomi,299,4.4
iphone se,apple,429,4.1"""

# Создаём временные файлы
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8') as f1:
    f1.write(content1)
    f1_path = f1.name

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8') as f2:
    f2.write(content2)
    f2_path = f2.name

try:
    # Читаем и генерируем отчёт
    data = read_csv_files([f1_path, f2_path])
    output = generate_average_rating_report(data)

    print("=== ВЫВОД ОТЧЁТА ===")
    print(output)
    print("\n=== СЫРОЙ ВЫВОД (repr) ===")
    print(repr(output))

finally:
    # Удаляем временные файлы
    os.unlink(f1_path)
    os.unlink(f2_path)