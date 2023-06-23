import customtkinter as ctk
from .widgets.topframe import TopFrame
from .widgets.bottomframe import BottomFrame
from .widgets.middleframe import MiddleFrame
from .api import API
from .lib.utils import truncate_lines
from .lib.utils import Generator

class Anki(ctk.CTk, API):
    def __init__(self):
        super().__init__()
        self.geometry("400x800")
        self.resizable(False, False)
        self.title("Ankipythia")

        # Frames in the main window
        self.TF = TopFrame(self, width=400, height=30)
        self.MF = MiddleFrame(self, width=400, height=600)
        self.BF = BottomFrame(self, width=400, height=50)

        self.gen = None
        self.front = None
        self.back = None
        self.last_card = False

        self.init_values()

    # Main methods.
    from ._anki._methods import next_card
    from ._anki._methods import turn_card
    from ._anki._methods import init_values
    from ._anki._methods import refresh_dropdown
    from ._anki._methods import on_dropdown_change
    from ._anki._methods import deck_cards
    from ._anki._methods import current_deck
    from ._anki._methods import no_cards

    # Utils.
    from .lib.utils import truncate_lines
    from itertools import chain