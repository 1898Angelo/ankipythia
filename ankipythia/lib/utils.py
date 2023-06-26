FONT = (None, None, "bold")

def truncate_lines(text):
    text = text.split(" ")
    return "\n".join([" ".join(text[i: i+6]) for i in range(0, len(text), 6)])

class Generator:
    """
    Creates a generator out an iterable with the ability to
    check if the current item in the generator is the last.
    """
    def __init__(self, generator):
        self.generator = iter(generator)
        self.cache = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.cache:
            return self.cache.pop()
        else:
            return next(self.generator)
        
    def __add__(self, gen):
        """Operator overload to join the current generator and another iterable together."""
        from itertools import chain
        return Generator(chain(self.generator, gen))

    def last(self):
        """Returns True if the current item in the generator is the last."""
        if self.cache:
            return False
        try:
            self.cache = [next(self.generator)]
        except StopIteration:
            return True
        return False