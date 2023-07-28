from customtkinter import (CTkToplevel, CTkButton, CTkFrame, CTkEntry, CTkTextbox)
from time import time_ns
from ...api import API


class AddCard(CTkToplevel, API):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master
        self.geometry("500x250")
        self.resizable(False, False)
        self.title("Add Card")

        # Frame
        self.frame = CTkFrame(self, height=200)
        
        # Widgets
        self.front = CTkEntry(self.frame, placeholder_text="Front",
                                height=30, width=300)
        self.back = CTkTextbox(self.frame, height=100, width=500, wrap="word")
        self.button = CTkButton(self, text="Add to Current Deck",
                                border_color="black", border_width=2,
                                command=self.add_card)
        
        # Positioning
        self.frame.pack(ipady=5, pady=10, padx=10, fill="both", side="top")
        self.front.pack(pady=10, padx=10)
        self.back.pack(ipady=12, padx=10)
        self.button.place(rely=0.96, relx=0.5, anchor="s")
    
    def add_card(self):
        if len(self.card_front) == 0 or len(self.card_back) == 0:
            return
        if self.master.current_deck  == "Empty Deck":
            if not self.exists(self.master.current_deck):
                self.__enter_deck__(self.master.current_deck)
            
        timestamp = time_ns()
        query = """
        INSERT INTO card(timestamp, deck_id, front, back)
        VALUES (?, 
		(SELECT id FROM deck WHERE name = (?)),
        ?, ?)
        """.strip()
        parameters = (timestamp, 
                      self.master.current_deck,
                      self.card_front, 
                      self.card_back)
        self.query(query, parameters)

        tup = [((self.card_front, self.card_back))]
        self.master.gen += tup
        if self.master.last_card:
            self.master.next_card()
        
        return self._refresh_widget()

    def _refresh_widget(self):
        self.front.delete("0", "end")
        self.back.delete("0.0", "end")
        self.front.focus()
    
    @property
    def card_front(self):
        return self.front.get()
    
    @property
    def card_back(self):
        return self.back.get("0.0", "end").strip()