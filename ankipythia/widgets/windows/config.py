from customtkinter import (CTkToplevel, CTkFrame, CTkLabel, CTkFont)
from ...lib.utils import FONT

class ConfigurationMenu(CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("300x600")
        self.resizable(False, False)
        self.title("Configuration")

        # Frame
        self.top = CTkFrame(self, height=100)
        self.bottom = CTkFrame(self, height=600)

        # Widgets
        CTkLabel(self.top, text="Settings", font=CTkFont(*FONT)
                 ).pack(side="top", fill="x", pady=10, padx=10)
        # WIP
        CTkLabel(self.bottom, text="WIP", font=CTkFont(*FONT)
                 ).pack(pady=10, padx=10)

        # Positioning
        self.top.pack(fill="x", pady=10, padx=10)
        self.bottom.pack(fill="both", pady=10, padx=10, expand=True)