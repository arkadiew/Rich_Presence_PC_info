![Discord Rich Presence](https://img.shields.io/badge/Discord%20Rich%20Presence-active-5865F2?logo=discord&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-Supported-0078D6?logo=windows&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)


# System Info Discord Rich Presence

Приложение отображает информацию о системе (CPU, GPU, RAM, диск, ОС) в Discord Rich Presence. Использует OpenHardwareMonitor через WMI и требует client ID Discord-приложения.

> [!TIP]
> **Совет:** Для корректной работы запускайте OpenHardwareMonitor с правами администратора и убедитесь, что Discord уже запущен.

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

> [!IMPORTANT]
> Не забудьте создать файл `client_id.txt` с вашим Discord client ID и поместить его в папку с программой.

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

## Запуск EXE

1. Установите Rich_Presence_PC_info из Releases:
2. Поместите `client_id.txt` рядом с EXE-файлом.

## Использование

- Запустите OpenHardwareMonitor.exe с правами администратора.
- Запустите Discord.
- Запустите скрипт или EXE.
- Для отладки смотрите `system_info.log`.

> [!WARNING]
> Если не отображается информация или возникают ошибки — проверьте, что все требования выполнены и все программы запущены с нужными правами.

## Проблемы

- Нет `client_id.txt`: Discord Rich Presence отключён, смотрите лог.
- Нет данных от OpenHardwareMonitor: проверьте запуск с правами администратора.
- Ошибки WMI: проверьте службу WMI (`services.msc`), восстановите при необходимости (`winmgmt /resetrepository`).
- Discord не обновляет статус: проверьте client ID и работу Discord.

##
