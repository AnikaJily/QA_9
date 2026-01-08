# Автоматическое тестирование с GitHub Actions

Этот проект содержит UI-тесты для формы контактов, настроенные для автоматического запуска в GitHub Actions.

## Структура проекта

- `test_contact.py` - тесты с использованием Selenium и Page Object Model
- `pop_classes.py` - классы для Page Object Model
- `index.html` - HTML страница для тестирования
- `requirements.txt` - зависимости Python

## Локальный запуск тестов

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов
pytest test_contact.py -v
```

## GitHub Actions

Workflow автоматически запускается при:
- Push в ветки `main` или `master`
- Создании Pull Request
- Ручном запуске через GitHub UI

### Что делает workflow:

1. ✅ Устанавливает Ubuntu (последняя версия)
2. ✅ Устанавливает Python 3.11
3. ✅ Устанавливает Chrome и ChromeDriver
4. ✅ Устанавливает зависимости из `requirements.txt`
5. ✅ Запускает тесты через `pytest`
6. ✅ Показывает результат (зеленая галочка при успехе)

### Проверка статуса

После push в репозиторий:
1. Перейдите на вкладку **Actions** в вашем GitHub репозитории
2. Выберите последний workflow run
3. Дождитесь завершения (обычно 2-3 минуты)
4. При успешном выполнении появится зеленая галочка ✅

## Настройка

Если нужно изменить версию Python, отредактируйте `.github/workflows/run-tests.yml`:

```yaml
python-version: '3.11'  # Измените на нужную версию
```






