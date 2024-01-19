import tkinter as tk

from app_view_model.login_page import LoginPage

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    LoginPage(root)
    root.deiconify()
    root.mainloop()
