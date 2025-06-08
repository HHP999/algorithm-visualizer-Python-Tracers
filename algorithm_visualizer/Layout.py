from algorithm_visualizer.Commander import Commander

class Layout(Commander):
    def __init__(self, children):
        super().__init__([children])

    @staticmethod
    def set_root(child):
        Commander.command_(None, "setRoot", [child])

    def add(self, child, index=None):
        if index is not None:
            self.command("add", [child, index])
        else:
            self.command("add", [child])

    def remove(self, child):
        self.command("remove", [child])

    def remove_all(self):
        self.command("removeAll", [])
