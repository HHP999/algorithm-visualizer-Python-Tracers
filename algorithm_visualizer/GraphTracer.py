from algorithm_visualizer.Tracer import Tracer

class GraphTracer(Tracer):
    def __init__(self, title=None):
        super().__init__(title)

    def set(self, array2d):
        self.command("set", [array2d])

    def directed(self, is_directed=None):
        if is_directed is not None:
            self.command("directed", [is_directed])
        else:
            self.command("directed", [])
        return self

    def weighted(self, is_weighted=None):
        if is_weighted is not None:
            self.command("weighted", [is_weighted])
        else:
            self.command("weighted", [])
        return self

    def layout_circle(self):
        self.command("layoutCircle", [])
        return self

    def layout_tree(self, root=None, sorted=None):
        if root is not None and sorted is not None:
            self.command("layoutTree", [root, sorted])
        elif root is not None:
            self.command("layoutTree", [root])
        else:
            self.command("layoutTree", [])
        return self

    def layout_random(self):
        self.command("layoutRandom", [])
        return self

    def add_node(self, id, weight=None, x=None, y=None, visited_count=None, selected_count=None):
        args = [id]
        if weight is not None:
            args.append(weight)
        if x is not None:
            args.append(x)
        if y is not None:
            args.append(y)
        if visited_count is not None:
            args.append(visited_count)
        if selected_count is not None:
            args.append(selected_count)
        self.command("addNode", args)

    def update_node(self, id, weight=None, x=None, y=None, visited_count=None, selected_count=None):
        args = [id]
        if weight is not None:
            args.append(weight)
        if x is not None:
            args.append(x)
        if y is not None:
            args.append(y)
        if visited_count is not None:
            args.append(visited_count)
        if selected_count is not None:
            args.append(selected_count)
        self.command("updateNode", args)

    def remove_node(self, id):
        self.command("removeNode", [id])

    def add_edge(self, source, target, weight=None, visited_count=None, selected_count=None):
        args = [source, target]
        if weight is not None:
            args.append(weight)
        if visited_count is not None:
            args.append(visited_count)
        if selected_count is not None:
            args.append(selected_count)
        self.command("addEdge", args)

    def update_edge(self, source, target, weight=None, visited_count=None, selected_count=None):
        args = [source, target]
        if weight is not None:
            args.append(weight)
        if visited_count is not None:
            args.append(visited_count)
        if selected_count is not None:
            args.append(selected_count)
        self.command("updateEdge", args)

    def remove_edge(self, source, target):
        self.command("removeEdge", [source, target])

    def visit(self, target, source=None, weight=None):
        args = [target]
        if source is not None:
            args.append(source)
        if weight is not None:
            args.append(weight)
        self.command("visit", args)

    def leave(self, target, source=None, weight=None):
        args = [target]
        if source is not None:
            args.append(source)
        if weight is not None:
            args.append(weight)
        self.command("leave", args)

    def select(self, target, source=None):
        args = [target]
        if source is not None:
            args.append(source)
        self.command("select", args)

    def deselect(self, target, source=None):
        args = [target]
        if source is not None:
            args.append(source)
        self.command("deselect", args)

    def log(self, log_tracer):
        self.command("log", [log_tracer])
