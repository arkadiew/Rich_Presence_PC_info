<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/discord.svg" alt="Discord" width="64" height="64"/>
  <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/windows.svg" alt="Windows" width="64" height="64"/>
  <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/python.svg" alt="Python" width="64" height="64"/>
</p>

# System Info Discord Rich Presence

Приложение отображает информацию о системе (CPU, GPU, RAM, диск, ОС) в Discord Rich Presence. Использует OpenHardwareMonitor через WMI и требует client ID Discord-приложения.

## Возможности

- CPU: имя и загрузка
- GPU: имя, температура, загрузка
- RAM и диск: использование
- ОС: версия
- Обновление статуса каждые 10 секунд
- Обработка ошибок и отсутствие данных

## Требования

- Windows (WMI, OpenHardwareMonitor)
- Python 3.x
- OpenHardwareMonitor (скачать и запустить с правами администратора)
- Discord (должен быть запущен)
- Зависимости: `pypresence`, `psutil`, `pywin32`

## Установка

1. Клонируйте репозиторий.
2. Установите зависимости:
   ```
   pip install pypresence psutil pywin32
   ```
3. Скачайте и распакуйте OpenHardwareMonitor с [openhardwaremonitor.org](https://openhardwaremonitor.org/).
4. Создайте файл `client_id.txt` с вашим Discord client ID (без пробелов и переносов).
5. Поместите `client_id.txt` в папку с `Rich_Presence_PC_info.py`.
6. Запустите скрипт:
   ```
   python Rich_Presence_PC_info.py
   ```

## Сборка EXE

1. Установите PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Соберите EXE:
   ```
   python -m PyInstaller --onefile Rich_Presence_PC_info.py
   ```
3. Поместите `client_id.txt` в папку `_internal` рядом с EXE-файлом.

## Использование

- Запустите OpenHardwareMonitor.exe с правами администратора.
- Запустите Discord.
- Запустите скрипт или EXE.
- Для отладки смотрите `system_info.log`.

## Проблемы

- Нет `client_id.txt`: Discord Rich Presence отключён, смотрите лог.
- Нет данных от OpenHardwareMonitor: проверьте запуск с правами администратора.
- Ошибки WMI: проверьте службу WMI (`services.msc`), восстановите при необходимости (`winmgmt /resetrepository`).
- Discord не обновляет статус: проверьте client ID и работу Discord.

## Лицензия

MIT
