from algorithm_visualizer.Tracer import Tracer

class LogTracer(Tracer):
    def __init__(self, title=None):
        super().__init__(title)

    def set(self, log):
        self.command("set", [log])

    def print(self, message):
        self.command("print", [message])

    def println(self, message):
        self.command("println", [message])

    def printf(self, format, *args):
        trace_args = [format] + list(args)  # Combine format string with args
        self.command("printf", trace_args)
