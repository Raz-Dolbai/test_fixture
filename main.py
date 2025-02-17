import pytest
import requests


@pytest.fixture(scope="session")
def test_data(request) -> list:
    path_file = request.param
    with open(f'{path_file}', 'r', encoding='utf-8') as file:
        tfl = [el.strip() for el in file.readlines()]
    return tfl


@pytest.mark.parametrize("test_data", ["test_data.txt"], indirect=True)  # передаем название файла с тестовыми данными
def test_open_data_file(test_data):
    URL = "https://www.google.com/{}"
    response = requests.get(URL.format(test_data))
    print(response)
