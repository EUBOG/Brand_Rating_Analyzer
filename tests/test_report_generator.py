import pytest
import tempfile
import os
from report_generator import read_csv_files, calculate_average_rating, generate_average_rating_report


@pytest.fixture
def sample_csv_files():
    content1 = """name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6"""

    content2 = """name,brand,price,rating
poco x5 pro,xiaomi,299,4.4
iphone se,apple,429,4.1"""

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f1:
        f1.write(content1)
        f1_path = f1.name

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f2:
        f2.write(content2)
        f2_path = f2.name

    yield [f1_path, f2_path]

    os.unlink(f1_path)
    os.unlink(f2_path)


def test_read_csv_files(sample_csv_files):
    data = read_csv_files(sample_csv_files)
    assert len(data) == 5
    assert data[0]['brand'] == 'apple'
    assert data[-1]['brand'] == 'apple'


def test_calculate_average_rating(sample_csv_files):
    data = read_csv_files(sample_csv_files)
    result = calculate_average_rating(data)
    brands = [r['brand'] for r in result]
    ratings = [round(r['average_rating'], 2) for r in result]

    # На основе тестовых данных:
    # samsung: [4.8] → 4.80
    # apple: [4.9, 4.1] → 4.50
    # xiaomi: [4.6, 4.4] → 4.50
    # При равных рейтингах порядок может зависеть от реализации (Python >=3.7 dict сохраняет порядок вставки)
    # Но в данном случае apple появляется раньше xiaomi → apple идёт перед xiaomi при равенстве

    assert brands == ['samsung', 'apple', 'xiaomi']
    assert ratings == [4.80, 4.50, 4.50]


def test_generate_average_rating_report(sample_csv_files):
    data = read_csv_files(sample_csv_files)
    output = generate_average_rating_report(data)
    assert "samsung" in output
    assert "4.80" in output
    assert "4.50" in output