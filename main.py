import tkinter as tk
from tkinter import messagebox
import minecraft_launcher_lib
import subprocess
import os
from PIL import Image, ImageTk

def first_launch():
    check_path = 'start.txt'
    if not os.path.isfile(check_path):
        with open(check_path, 'w', encoding='utf-8') as file:
            file.write('')
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Привет!", "Приветствую! Кажется это первый запуск лаунчера!")
        messagebox.showinfo("Инфа", "Пожалуйста установите Java перед использыванием лаунчера!")
        exit()
    else:
        print('ну ладно')

def launch_minecraft():
    version = version_entry.get()
    nickname = nickname_entry.get()
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', 'azurelauncher')
    minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory)
    options = {
        'username': nickname,
        'uuid': '',
        'token': ''
    }
    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options))

first_launch()

# Создание основного окна
root = tk.Tk()
root.title("AzureLauncher")

# Загрузка изображения
logo_image = Image.open("logo_azure.png")

logo_photo = ImageTk.PhotoImage(logo_image)

# Отображение изображения в Label
logo_label = tk.Label(root, image=logo_photo)
logo_label.image = logo_photo  # Сохранение ссылки на изображение
logo_label.pack()  # Или используйте другой менеджер компоновки

# Создание виджетов для ввода данных пользователя
version_label = tk.Label(root, text="Введите версию:")
version_label.pack()
version_entry = tk.Entry(root)
version_entry.pack()

nickname_label = tk.Label(root, text="Введите никнейм:")
nickname_label.pack()
nickname_entry = tk.Entry(root)
nickname_entry.pack()

launch_button = tk.Button(root, text="Запустить Minecraft", command=launch_minecraft)
launch_button.pack()

root.mainloop()


# Метки
tk.Label(root, text="Welcome!").pack()
tk.Label(root, text="Приветствую!").pack()

# Поля ввода с подсказками
version_entry = tk.Entry(root)
version_entry.insert(0, "Введите версию игры")
version_entry.pack()
nickname_entry = tk.Entry(root)
nickname_entry.insert(0, "Введите ник")
nickname_entry.pack()

# Кнопка запуска
launch_button = tk.Button(root, text="Запустить Minecraft", command=launch_minecraft)
launch_button.pack()

# Запуск основного цикла
root.mainloop()
