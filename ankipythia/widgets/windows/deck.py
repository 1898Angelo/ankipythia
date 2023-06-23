from customtkinter import (CTkToplevel, CTkFrame, CTkButton, CTkEntry)
from ...api import API
from tkinter.ttk import Treeview
from tkinter import CENTER
from tkinter.ttk import Style

class TableFrame(CTkFrame, API):
    def __init__(self, master, root_window=None, **kwargs):
        super().__init__(master, **kwargs)
        self.root_window = root_window
        self.tree = Treeview(self, 
                              height=10,
                              columns=("#1", "#2"),
                              selectmode="browse")
        self.tree.pack(fill="both", expand=True, pady=10, padx=10)

        self.tree.heading("#0", text="Decks", anchor=CENTER)
        self.tree.heading("#1", text="Front", anchor=CENTER)
        self.tree.heading("#2", text="Back", anchor=CENTER)
        self.tree.column("#0", width=15)
        self.tree.column("#1", width=70)

        self._set_style()
        self.populate_tree()

    def enter_deck(self, deck: str):
        deck = deck.title()
        query = "INSERT INTO deck_lookup(deck_name) VALUES (?)"
        parameters = (deck,)
        self.query(query, parameters)
        self.root_window.refresh_dropdown()
        return self.populate_tree()

    def populate_tree(self):
        nodes = self.tree.get_children()
        if nodes != ():
            for node in nodes:
                self.tree.delete(node)

        # Insert the nodes into the tree
        nodes = self.retrieve_nodes()
        for node_id, node in nodes:
            self.tree.insert("", "end", 
                             node.replace(" ", "_"), 
                             text=node, 
                             tags=("deck_lookup", node_id, node))
            # ... Then the items into the nodes
            decks = self.retrieve_items(node)
            for idx, (row_id, front, back) in enumerate(decks, start=1):
                self.tree.insert(node.replace(" ", "_"), 
                                 "end", 
                                 text=idx, 
                                 values=[front, back],
                                 tags=("card", row_id, node))

    def retrieve_nodes(self):
        query = "SELECT id, deck_name FROM deck_lookup"
        return self.query(query)
    
    def retrieve_items(self, deck_name):
        query = """
        SELECT card.id, front, back
        FROM card
        INNER JOIN deck_lookup ON card.deck_id = deck_lookup.id
        WHERE deck_name = (?)
        """.strip()
        parameters = (deck_name,)
        return self.query(query, parameters)

    def delete_selection(self, id, contents):
        query = f"DELETE FROM {contents['tags'][0]} WHERE id = (?)"
        parameters = (contents['tags'][1],)
        self.query(query, parameters,)
        self.tree.delete(id)
        self.root_window.refresh_dropdown()

        if self.root_window.gen.last():
            return self.root_window.next_card()
    
    
    def _set_style(self):
        tree_style = Style()
        tree_style.theme_use("default")
        tree_style.configure("Treeview",
                    background="#2a2d2e",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#343638",
                    bordercolor="#343638",
                    borderwidth=0)
        tree_style.map('Treeview', background=[('selected', '#22559b')])
        tree_style.configure("Treeview.Heading",
                    background="#565b5e",
                    foreground="white",
                    relief="flat")
        tree_style.map("Treeview.Heading", background=[('active', '#3484F0')])

    @property
    def current_selection(self) -> dict:
        id = self.tree.selection()
        contents = self.tree.item(self.tree.selection())
        return {"id": id, "contents": contents}

class ModifyDecks(CTkToplevel, API):
    def __init__(self, master):
        super().__init__(master)
        root_window = master
        self.geometry("680x480")
        self.resizable(False, False)
        self.title("Modify Deck")

        #Frames
        self.top = CTkFrame(self, height=40, width=400)
        self.table = TableFrame(self, 
                                height=150, 
                                width=400, 
                                root_window=root_window)

        # Widgets
        ## Top Section
        self.add_deck_entry = CTkEntry(self.top, placeholder_text="Deck Name",
                                 height=30, width=400)
        self.add_deck_button = CTkButton(self.top, text="Add New Deck",
                                         border_color="black", border_width=2,
                                         command=self._add_deck)
        
        ## Bottom Section
        self.delete_deck_button = CTkButton(self, text="Delete Deck",
                              border_color="black", border_width=2,
                              command=self._delete_deck)
        self.delete_card_button = CTkButton(self, text="Delete Card",
                              border_color="black", border_width=2,
                              command=self._delete_card)
        
        # Positioning
        self.top.pack(side="top", fill='x', pady=10, padx=10)
        self.table.pack(side="top", fill="x", ipady=30, padx=10, pady=10)

        self.add_deck_entry.pack(padx=10, pady=10, side="left")
        self.add_deck_button.pack(padx=10, pady=10, side="right")

        self.delete_deck_button.place(relx=0.2, rely=0.98, anchor="sw")
        self.delete_card_button.place(relx=0.8, rely=0.98, anchor="se")
    
    def _add_deck(self):
        deck_name = self.add_deck_entry.get()
        if len(deck_name) == 0:
            return
        if self.exists(deck_name):
            self._refresh_entry()
            return
        self.table.enter_deck(deck_name)
        self._refresh_entry()

    def _refresh_entry(self):
        self.add_deck_entry.delete("0", "end")
        self.add_deck_entry.focus()

    def _delete_deck(self) -> dict: 
        selection = self.table.current_selection
        if selection["contents"]["values"]:
            return
        self.table.delete_selection(selection["id"], selection["contents"])
        
    def _delete_card(self) -> dict:
        selection = self.table.current_selection
        if not selection["contents"]["values"]:
            return
        self.table.delete_selection(selection["id"], selection["contents"])
