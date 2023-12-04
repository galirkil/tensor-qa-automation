# tenzor-qa-automation
Test task for QA Automation engineer position at the Tensor company.

## Стек
- Python
- Selenium
- Pytest
- Google Chrome

## Особенности реализации
По умолчанию второй тестовый сценарий настроен на проверку правильного определения региона пользователя
при обращении к тестируемому приложению из Московского региона. В файле locator.py также доступен регион Республика Татарстан.
Для настройки теста на соответствующий регион необходимо передать информацию 
о регионе в первый вызов метода should_be_expected_region экзепляра класса SbisContactsPage.

## Локальный запуск проекта

Клонируйте репозиторий:

```bash
git clone git@github.com:galirkil/tensor-qa-automation.git
```

Перейдите в папку с проектом, установите и активируйте виртуальное окружение:

```bash
cd tensor-qa-automation
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Убедитесь, что на машине установлен Google Chrome.

Запустите тесты:

```bash
pytest
```
