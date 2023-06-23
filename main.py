from ankipythia.anki import Anki
from ankipythia.api import API
from customtkinter import (set_appearance_mode, set_default_color_theme)

if __name__ == "__main__":
    API.__db_dir__()
    API.__create_tables__()
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    app = Anki()
    app.iconbitmap(default=r"./resources/images/icon.ico")
    app.mainloop()
