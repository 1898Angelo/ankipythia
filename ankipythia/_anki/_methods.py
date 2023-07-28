from ..lib.utils import truncate_lines
from ..lib.utils import Generator

def next_card(self):
    if self.gen.last():
        self.last_card = True
        return self.no_cards()

    self.front, self.back = next(self.gen)
    self.front = truncate_lines(self.front)
    self.MF.set_front_value(self.front)
    self.last_card = False
    self.MF.delete_text()   

def turn_card(self):
    current_value = self.MF.back.get("0.0", "end").strip()
    if len(current_value) == 0:
        return self.MF.set_back_value(self.back)
    
def init_values(self):
    self.refresh_dropdown()
    self.gen = self.deck_cards()

    if self.gen.last():
        self.last_card = True
        return self.no_cards()

    self.front, self.back = next(self.gen)
    self.MF.set_front_value(self.front)

def refresh_dropdown(self):
    query = "SELECT name FROM deck"
    decks = [item for tup in self.query(query) for item in tup]

    if not decks:
        decks = ["Empty Deck"]

    self.TF.dropdown.configure(values=decks)
    self.TF.set_dropdown_value(decks[0])

def on_dropdown_change(self):
    self.gen = self.deck_cards()
    self.next_card()

def deck_cards(self):
    query = """
    SELECT front, back
    FROM card
    INNER JOIN deck ON card.deck_id = deck.id
    WHERE deck.name = (?)
    """.strip()
    parameters = (self.current_deck,)
    return Generator(self.query(query, parameters))

def no_cards(self):
    self.MF.set_front_value("Add new cards!")
    self.MF.delete_text()
    self.back = ""

@property
def current_deck(self):
    return self.TF.current_deck