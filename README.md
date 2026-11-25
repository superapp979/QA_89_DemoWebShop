# QA89 · Demo Web Shop

Упражнение по Selenium. Скрипт открывает главную страницу Demo Web Shop и находит десять разных HTML-тегов. Для каждого тега он выводит число совпадений и проверяет, что TAG_NAME и CSS_SELECTOR нашли одни и те же элементы.

## Запуск на macOS

Откройте папку проекта в PyCharm. В терминале проекта выполните:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python locators/css_selectors_index.py
```

Для запуска нужен Google Chrome и доступ к сайту. Числа в двух столбцах каждой строки должны совпасть и быть больше нуля.
