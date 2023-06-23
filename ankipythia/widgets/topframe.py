from customtkinter import (CTkFrame, CTkLabel, CTkFont, CTkOptionMenu, CTkButton, StringVar)
from .windows.config import ConfigurationMenu
from ..api import API
from ..lib.utils import FONT

class TopFrame(CTkFrame, API):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(pady=0, side="top", fill="x")
        self.master = master

        self.initial_value = StringVar()
        self.window = None

        # Widgets
        CTkLabel(self, height=25, font=CTkFont(*FONT),
                 text="Deck: ").place(relx=0.18, rely=0.5, anchor="w")
        self.configuration = CTkButton(self, height=20, width=10, text=" "*3,
                                       border_color="black", border_width=2,
                                       command=self.__menu__)
        self.dropdown = CTkOptionMenu(self, height=20, width=140,
                                    variable=self.initial_value,
                                    command=self.on_dropdown_change,
                                    dynamic_resizing=False)
        self.next = CTkButton(self, height=20, width=20, text="Next Card",
                              border_color="black", border_width=2,
                              command=master.next_card)
        self.turn = CTkButton(self, height=20, width=10, text="Turn",
                              border_color="black", border_width=2,
                              command=master.turn_card)
        
        # Positioning
        self.dropdown.place(relx=0.29, rely=0.5, anchor="w")
        self.next.place(relx=0.83, rely=0.51, anchor="e")
        self.turn.place(relx=0.94, rely=0.51, anchor="e")
        self.configuration.place(relx=0.05, rely=0.51, anchor="w")
    
    def __menu__(self):
        if self.window is None or not self.window.winfo_exists():
            self.window = ConfigurationMenu(self.master)
            return
        self.window.focus()
    
    def set_dropdown_value(self, value):
        return self.initial_value.set(value)
    
    def on_dropdown_change(self, *args, **kwargs):
        self.master.on_dropdown_change()

    @property
    def current_deck(self):
        return self.dropdown.get()