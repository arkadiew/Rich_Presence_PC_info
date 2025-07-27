# Discord System Monitor Rich Presence

Этот проект позволяет отображать в Discord Rich Presence актуальную информацию о вашей системе: загрузка CPU и GPU, температура, использование оперативной памяти, диска и версия ОС.

---

## 🧰 Шаг 1: Установка Python и Git

1. Установите **Python 3.7 или выше**: [python.org](https://www.python.org/downloads/)  
   ⚠️ При установке поставьте галочку **"Add Python to PATH"**

2. Установите **Git**: [git-scm.com](https://git-scm.com/downloads)

---

## 📁 Шаг 2: Получение проекта

Если проект размещён на GitHub:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

Или создайте папку вручную и поместите туда `main.py`.

---

## 📦 Шаг 3: Установка зависимостей

Выполните в терминале:

```bash
pip install pypresence psutil pywin32
```

Если появляется ошибка с `pywin32`, выполните:

```bash
python -m pywin32_postinstall install
```

---

## 🖥️ Шаг 4: Установка OpenHardwareMonitor

1. Скачайте [OpenHardwareMonitor](https://openhardwaremonitor.org/)
2. Распакуйте архив
3. Запустите `OpenHardwareMonitor.exe` **от имени администратора**
4. Убедитесь, что включена WMI-поддержка (если требуется)

---

## 🛠️ Шаг 5: Получение Discord Client ID

1. Перейдите на [Discord Developer Portal](https://discord.com/developers/applications)
2. Создайте новое приложение
3. Перейдите в **Rich Presence → Art Assets**, загрузите иконки (необязательно)
4. Перейдите в раздел **OAuth2** и скопируйте `Client ID`
5. Вставьте в файл `main.py`:

```python
client_id = "ВАШ_CLIENT_ID"
```

---

## 🚀 Шаг 6: Запуск скрипта

Откройте терминал в папке проекта и выполните:

```bash
python main.py
```

Скрипт будет обновлять ваш статус в Discord каждые 10 секунд.

---

## ✅ Проверка

Откройте Discord → Перейдите в профиль → Убедитесь, что отображаются данные о вашей системе:
- CPU: название и загрузка
- GPU: название, температура и нагрузка
- RAM, диск, ОС

---

## 🔧 Проблемы и решения

| Проблема                          | Решение                                                                 |
|----------------------------------|-------------------------------------------------------------------------|
| Не отображается GPU              | Убедитесь, что OpenHardwareMonitor запущен с правами администратора    |
| Discord не показывает статус     | Проверьте `Client ID` и подключение Rich Presence                      |
| Ошибка с `win32com`              | Убедитесь, что установлен `pywin32` и выполнен post-install скрипт     |

---

## 📝 Лицензия

MIT License — свободное использование, распространение и модификация.
