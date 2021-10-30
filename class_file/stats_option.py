from tkinter import IntVar
from class_file.stats import Stats


class StatsOption:
    def __init__(self, name, condition, stats):
        self.name = name
        self.condition = condition
        self.stats = stats
        self.status = IntVar()
        self.stack = IntVar()
