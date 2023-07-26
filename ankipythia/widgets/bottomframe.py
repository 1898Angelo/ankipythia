from customtkinter import (CTkFrame, CTkButton)
from .windows.deck import ModifyDecks
from .windows.add import AddCard

class BottomFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(pady=0, side="bottom", fill='x')
        self.master = master

        # Widgets
        self.modify = CTkButton(self, text="Modify Decks", border_color="black", 
                                border_width=2, command=self._decks_window)
        self.add = CTkButton(self, text="Add Card", border_color="black", 
                             border_width=2, command=self._card_window)

        # Positioning
        self.add.place(relx=0.9, rely=0.5, anchor="e")
        self.modify.place(relx=0.1, rely=0.5, anchor="w")

        self.window = None

    def _decks_window(self):
        if self.window is None or not self.window.winfo_exists():
            self.window = ModifyDecks(self.master)
            return
        self.window.focus()

    def _card_window(self):
        if self.window is None or not self.window.winfo_exists():
            self.window = AddCard(self.master)
            return
        self.window.focus()
