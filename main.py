import tkinter as tk

from app_view_model.login_page import LoginPage
from app_view_model.start_page import StartPage

if __name__ == '__main__':
    root = tk.Tk()
    StartPage(root)
    # LoginPage(root)
    root.mainloop()
