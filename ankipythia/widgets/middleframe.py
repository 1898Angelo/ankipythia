from customtkinter import (CTkFrame, CTkTextbox, CTkLabel, CTkFont, StringVar)
from ..lib.utils import FONT

class MiddleFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack(pady=60, padx=10, fill="both", expand=True)
        self.front_value = StringVar()

        # Widgets
        self.front = CTkLabel(self,
                              fg_color=("gray100", "gray10"),
                              textvariable=self.front_value,
                              corner_radius=6,
                              font=CTkFont(*FONT),
                              height=200)
        self.back = CTkTextbox(self,
                               font=CTkFont(*FONT),
                               height=350,
                               wrap="word")

        # Positioning
        self.front.pack(pady=10, ipady=10, padx=10, fill="x", side="top")
        self.back.pack(pady=10, padx=10, fill="x", side="bottom")

    def set_front_value(self, value):
        return self.front_value.set(value)
    
    def delete_text(self):
        self.back.configure(state="normal")
        self.back.delete("0.0", "end")
        self.back.configure(state="disabled")
    
    def set_back_value(self, value):
        self.back.configure(state="normal")
        self.back.insert("0.0", value)
        self.back.configure(state="disabled")