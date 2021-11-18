from tkinter import IntVar
from class_file.stats import Stats


class StatsOption:
    def __init__(self, name, condition, stats):
        self.name = name
        self.condition = condition
        self.stats = stats
        self.stack_combobox = None
        self.status = IntVar()
        self.stack = IntVar()

    def __eq__(self, other):
        return self.name == other.name and self.condition == other.condition
