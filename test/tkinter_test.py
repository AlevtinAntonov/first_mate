# import tkinter as tk
# from tkinter import ttk
#
# def validate_input(*args):
#     if entry1.get() and entry2.get() and combobox.get():
#         button.config(state=tk.NORMAL, style='active.TButton')
#     else:
#         button.config(state=tk.DISABLED, style='inactive.TButton')
#
# root = tk.Tk()
# root.title("Проверка ввода данных")
#
# frame = ttk.Frame(root, padding="10")
# frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#
# label1 = ttk.Label(frame, text="Введите данные:")
# label1.grid(row=0, column=0, sticky=tk.W)
#
# entry1 = ttk.Entry(frame, width=20)
# entry1.grid(row=1, column=0, sticky=tk.W)
# entry1.bind("<KeyRelease>", validate_input)
#
# entry2 = ttk.Entry(frame, width=20)
# entry2.grid(row=2, column=0, sticky=tk.W)
# entry2.bind("<KeyRelease>", validate_input)
#
# label2 = ttk.Label(frame, text="Выберите значение из списка:")
# label2.grid(row=3, column=0, sticky=tk.W)
#
# combobox = ttk.Combobox(frame, values=['Option 1', 'Option 2', 'Option 3'], width=17)
# combobox.grid(row=4, column=0, sticky=tk.W)
# combobox.bind("<<ComboboxSelected>>", validate_input)
#
# style = ttk.Style()
# style.configure('inactive.TButton', background='gray')
# style.configure('active.TButton', background='red')
#
# button = ttk.Button(frame, text="Сохранить", state=tk.DISABLED, style='inactive.TButton')
# button.grid(row=5, column=0, sticky=tk.W, pady=(10, 0))
#
# root.mainloop()
# import tkinter as tk
# from tkinter import ttk
#
# def validate_input(*args):
#     if entry1.get() and entry2.get() and combobox.get():
#         button.config(state=tk.NORMAL, style='active.TButton')
#     else:
#         button.config(state=tk.DISABLED, style='inactive.TButton')
#
# root = tk.Tk()
# root.title("Проверка ввода данных")
#
# frame = ttk.Frame(root, padding=10)
# frame.grid(row=0, column=0, sticky="nsew")
#
# label1 = ttk.Label(frame, text="Введите данные:")
# label1.grid(row=0, column=0, sticky="w")
#
# entry1 = ttk.Entry(frame, width=20)
# entry1.grid(row=1, column=0, sticky="w")
# entry1.bind("<KeyRelease>", validate_input)
#
# entry2 = ttk.Entry(frame, width=20)
# entry2.grid(row=2, column=0, sticky="w")
# entry2.bind("<KeyRelease>", validate_input)
#
# label2 = ttk.Label(frame, text="Выберите из списка:")
# label2.grid(row=3, column=0, sticky="w")
#
# combobox = ttk.Combobox(frame, values=['Option 1', 'Option 2', 'Option 3'], width=17)
# combobox.grid(row=4, column=0, sticky="w")
# combobox.bind("<<ComboboxSelected>>", validate_input)
#
# style = ttk.Style()
# style.map('TButton',
#     background=[('active', 'red'), ('disabled', 'gray')]
# )
#
# button = ttk.Button(frame, text="Сохранить", state=tk.DISABLED, style='inactive.TButton')
# button.grid(row=5, column=0, sticky="w", pady=(10, 0))
#
# root.mainloop()
import tkinter as tk
from tkinter import ttk


# def validate_input(*args):
#     if args.get():
#         button.config(state=tk.NORMAL, background='red', fg='white')
#     else:
#         button.config(state=tk.DISABLED, background='LightGray', fg='white')


def validate_input(*args):
    all_entries_filled = all(entry.get() for entry in entry_list)
    # all_comboboxes_selected = all(combobox.get() for combobox in combobox_list)

    if all_entries_filled:
        button.config(state=tk.NORMAL, background='red', fg='white')
    else:
        button.config(state=tk.DISABLED, background='LightGray', fg='white')


root = tk.Tk()
root.title("Проверка ввода данных")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label1 = ttk.Label(frame, text="Введите данные:")
label1.grid(row=0, column=0, sticky=tk.W)

entry1 = ttk.Entry(frame, width=20)
entry1.grid(row=1, column=0, sticky=tk.W)
entry1.bind("<KeyRelease>", validate_input)

entry2 = ttk.Entry(frame, width=20)
entry2.grid(row=2, column=0, sticky=tk.W)
entry2.bind("<KeyRelease>", validate_input)

label2 = ttk.Label(frame, text="Выберите значение из списка:")
label2.grid(row=3, column=0, sticky=tk.W)

combobox = ttk.Combobox(frame, values=['Option 1', 'Option 2', 'Option 3'], width=17)
combobox.grid(row=4, column=0, sticky=tk.W)
combobox.bind("<<ComboboxSelected>>", validate_input)
entry_list = [entry1, entry2, combobox]
# combobox_list = [combobox, ]
button = tk.Button(frame, text="Сохранить", state=tk.DISABLED, command=root.destroy)
button.grid(row=5, column=0, sticky=tk.W, pady=(10, 0))

root.mainloop()
validate_input_btn_ok