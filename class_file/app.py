import tkinter as tk

bg_color = '#111133'


class AppMain(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>', self.clickwin)
        self.bind('<B1-Motion>', self.dragwin)
        self.bind('<Button-3>', self.clickwin)
        self.bind('<B3-Motion>', self.dragwin_right)
        self.configure(bg=bg_color)
        self.attributes('-topmost', True)

    def dragwin(self, event):
        if self._offsety > 25:
            return
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x, y=y))

    def dragwin_right(self, event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x, y=y))

    def clickwin(self, event):
        self._offsetx = event.x + event.widget.winfo_rootx() - self.winfo_rootx()
        self._offsety = event.y + event.widget.winfo_rooty() - self.winfo_rooty()


class AppTopLevel(tk.Toplevel):
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-3>', self.clickwin)
        self.bind('<B3-Motion>', self.dragwin_right)
        self.bind('<Button-1>', self.clickwin)
        self.bind('<B1-Motion>', self.dragwin)
        self.configure(bg=bg_color)
        self.attributes('-topmost', True)

    def dragwin(self, event):
        if self._offsety > 25:
            return
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x, y=y))

    def dragwin_right(self, event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x, y=y))

    def clickwin(self, event):
        self._offsetx = event.x + event.widget.winfo_rootx() - self.winfo_rootx()
        self._offsety = event.y + event.widget.winfo_rooty() - self.winfo_rooty()