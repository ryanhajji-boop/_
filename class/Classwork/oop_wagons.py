class Wagon:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def getName(self):
        return f"Wagon is called {self.name}"
    

    def get_length(self):
        return self.length

class OpenWagon(self):
    pass

class ClosedWagon(self):
    pass

class Siding:
    def push_wagon(self, wagon):
        self._top_of_stack += 1
        self._wagon_array[self._top_of_stack] = wagon

    def pop_wagon(self):
        if self._top_of_stack > -1:
            return_wagon = self.wagon_array[self._top_of_stack]
            self._top_of_stack -= 1