# Программа анализа .csv файлов

import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import pandas as pd

# Создание главного окна
window = tk.Tk()
window.geometry("550x550")
window.title("Программа анализа .csv файлов")

# Создание меток вывода
label_00 = tk.Label(text = "Файл:")
label_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label_01 = tk.Label(text = "")
label_01.grid(row=0, column=1, sticky="w")

label_10 = tk.Label(text = "Строк:")
label_10.grid(row=1, column=0, padx=10, pady=10, sticky="e")

label_11 = tk.Label(text = "")
label_11.grid(row=1, column=1, sticky="w")

label_20 = tk.Label(text = "Столбцов:")
label_20.grid(row=2, column=0, padx=10, pady=10, sticky="e")

label_21 = tk.Label(text = "")
label_21.grid(row=2, column=1, sticky="w")

# Создание текстового вывода c прокруткой
output_text = st(height = 22, width = 50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Диалог открытия файла
def do_dialog():
    my_dir = os.getcwd()
    name= fd.askopenfilename(initialdir=my_dir)
    return name
    
# Обработчик csv файла при помощи pandas
def pandas_read_csv(file_name):
    df = pd.read_csv(file_name, header=None, sep=';')
    cnt_rows = df.shape[0]
    cnt_columns = df.shape[1]    
    label_11['text'] = cnt_rows
    label_21['text'] = cnt_columns
    return df
    
# Выборка столбца в список
def get_column(df, column_ix):
    cnt_rows = df.shape[0]
    lst = []
    for i in range(cnt_rows):
        lst.append(df.iat[i, column_ix])
    return lst
    
def meet_email(field):
    return '@' in str(field)
    
def meet_telphon(field):
    str_field=str(field)
    if '(' in str_field or ')' in str_field or '+' in str_field:
        return True
    else:
        return False
    
    
# Обработчик нажатия кнопки
def process_button():    
    file_name = do_dialog()
    label_01['text'] = file_name
    df = pandas_read_csv(file_name)
    cnt_columns = df.shape[1]    
    for column_ix in range(cnt_columns):
        lst = get_column(df, column_ix)    
        counter_total = 0        
        counter_meet = 0               
        counter_meet1 = 0                              
        for list_item in lst:
            counter_total += 1
            if meet_email(list_item):
                counter_meet += 1
            if meet_telphon(list_item):
                counter_meet1 += 1
        if counter_meet / counter_total > 0.5:
            output_text.insert(tk.END, "столбец " + str(column_ix+1) + " Емейлы!" + os.linesep)                        
        if counter_meet1 / counter_total > 0.5:
            output_text.insert(tk.END, "столбец " + str(column_ix+1) + " Телефоны!" + os.linesep)
    mb.showinfo(title=None, message="Готово")

# Создание кнопки
button=tk.Button(window, text="Прочитать файл", command=process_button)
button.grid(row=4, column=1)

# Запуск цикла mainloop
window.mainloop()


