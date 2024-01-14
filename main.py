import tkinter as tk

# from app_model.db.db_config import db_config
from app_view_model.login_page import LoginPage
from app_view_model.start_page import StartPage

if __name__ == '__main__':
    # при установке запускаем db_config ля записи пути к базе данных из base.ini
    # db_config()
    root = tk.Tk()
    # StartPage(root)
    LoginPage(root)
    root.mainloop()
