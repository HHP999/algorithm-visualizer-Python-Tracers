from algorithm_visualizer.Array2DTracer import Array2DTracer


class Array1DTracer(Array2DTracer):
    def __init__(self, title=None):
        if title:
            super().__init__(title)
        else:
            super().__init__()

    def set(self, array1d):
        self.command("set", [array1d])

    def patch(self, x, v=None):
        if v is not None:
            self.command("patch", [x, v])
        else:
            self.command("patch", [x])

    def depatch(self, x):
        self.command("depatch", [x])

    def select(self, sx, ex=None):
        if ex is not None:
            self.command("select", [sx, ex])
        else:
            self.command("select", [sx])

    def deselect(self, sx, ex=None):
        if ex is not None:
            self.command("deselect", [sx, ex])
        else:
            self.command("deselect", [sx])

    def chart(self, chart_tracer):
        self.command("chart", [chart_tracer])
