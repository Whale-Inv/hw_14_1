## Описание проекта
Проект представляет собой систему управления категориями и продуктами. 
Он включает классы для работы с категориями и продуктами, а также вспомогательные функции для работы с JSON-файлами.
## Структура проекта
```
   hw_14_1/
├── data
│   └── products.json
├── htmlcov
├── src
│   ├── 14.1_main.py
│   ├── 14.2_main.py
│   ├── 15.1_main.py
│   ├── 16.1_main.py
│   ├── _init_.py
│   ├── category.py
│   ├── lawngrass.py
│   ├── product.py
│   ├── productfilter.py
│   ├── smartphone.py
│   └── utils.py
└── tests
    ├── _init_.py
    ├── conftest.py
    ├── test_category.py
    ├── test_lawngrass.py
    ├── test_product.py
    ├── test_smartphone.py
    └── test_utils.py
    ├── .coverage
├── .flake8
├── .gitignore
├── LICENSE.md
├── poetry.lock
├── pyproject.toml
├── README.md
└── test_file.json
```
## Основные компоненты
1. **Классы:**
- `Category`: для работы с категориями товаров.
- `Product`: для описания отдельных товаров.
- `Smartphone`: для добавления продукта категории Смартфоны
- `Lawngrass`: для добавления продукта категории Трава газанная
- `ProductIter`: для вывода продуктов из списка продуктов
2. **Функции:**
- `read_json(path)`: чтение данных из JSON-файла.
- `create_objects_from_json(data)`: создание объектов `Category` и `Product` на основе данных из JSON.
3. **Тесты:**
- Тесты для классов находятся в папке `tests`.
- Используются фикстуры для упрощения тестирования.

## Требования
- Python 3.10+
- Установленные зависимости (см. `pyproject.toml`).
## Запуск тестов
Для запуска тестов выполните:
`pytest`
## Лицензия
Этот проект лицензируется под лицензией MIT. Подробности в файле [LICENSE](LICENSE.md).
Если у вас есть вопросы или предложения, обращайтесь!