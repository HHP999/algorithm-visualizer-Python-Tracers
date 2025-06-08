from algorithm_visualizer.Commander import Commander

class Tracer(Commander):
    @staticmethod
    def delay(line_number=None):
        if line_number is None:
            Commander.command_(None,"delay", [])
        else:
            Commander.command_(None,"delay", [line_number])

    def __init__(self, title=None):
        if title:
            super().__init__([title])
        else:
            super().__init__([])

    def set(self):
        self.command("set", [])

    def reset(self):
        self.command("reset", [])
