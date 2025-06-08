from algorithm_visualizer.Tracer import Tracer

class Array2DTracer(Tracer):
    def __init__(self, title=None):
        if title:
            super().__init__(title)
        else:
            super().__init__()

    def set(self, array2d):
        self.command("set", [array2d])

    def patch(self, x, y, v=None):
        if v is not None:
            self.command("patch", [x, y, v])
        else:
            self.command("patch", [x, y])

    def depatch(self, x, y):
        self.command("depatch", [x, y])

    def select(self, sx, sy, ex=None, ey=None):
        if ex is not None and ey is not None:
            self.command("select", [sx, sy, ex, ey])
        else:
            self.command("select", [sx, sy])

    def selectRow(self, x, sy, ey):
        self.command("selectRow", [x, sy, ey])

    def selectCol(self, y, sx, ex):
        self.command("selectCol", [y, sx, ex])

    def deselect(self, sx, sy, ex=None, ey=None):
        if ex is not None and ey is not None:
            self.command("deselect", [sx, sy, ex, ey])
        else:
            self.command("deselect", [sx, sy])

    def deselectRow(self, x, sy, ey):
        self.command("deselectRow", [x, sy, ey])

    def deselectCol(self, y, sx, ex):
        self.command("deselectCol", [y, sx, ex])
