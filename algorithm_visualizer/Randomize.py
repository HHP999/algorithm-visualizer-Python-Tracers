import random

class Randomizer:
    def __init__(self):
        self.random = random.Random()

    def get_type(self):
        raise NotImplementedError

    def create(self):
        raise NotImplementedError


class Integer(Randomizer):
    def __init__(self, _min=1, _max=9):
        super().__init__()
        self._min = _min
        self._max = _max

    def get_type(self):
        return int

    def create(self):
        return self.random.randint(self._min, self._max)


class Double(Randomizer):
    def __init__(self, _min=0.0, _max=1.0):
        super().__init__()
        self._min = _min
        self._max = _max

    def get_type(self):
        return float

    def create(self):
        return self.random.uniform(self._min, self._max)


class String(Randomizer):
    def __init__(self, length=16, letters="abcdefghijklmnopqrstuvwxyz"):
        super().__init__()
        self._length = length
        self._letters = letters

    def get_type(self):
        return str

    def create(self):
        return ''.join(self.random.choice(self._letters) for _ in range(self._length))


class Array2D(Randomizer):
    def __init__(self, N=10, M=10, randomizer=None):
        super().__init__()
        self._N = N
        self._M = M
        self._randomizer = randomizer or Integer()
        self._sorted = False

    def sorted(self, sorted=True):
        self._sorted = sorted
        return self

    def get_type(self):
        return None

    def create(self)->list:
        array = [[self._randomizer.create() for _ in range(self._M)] for _ in range(self._N)]
        if self._sorted:
            for row in array:
                row.sort()
        return array


class Array1D(Randomizer):
    def __init__(self, N=10, randomizer=None):
        super().__init__()
        self._N = N
        self._randomizer = randomizer or Integer()
        self._sorted = False

    def sorted(self, sorted=True):
        self._sorted = sorted
        return self

    def get_type(self):
        return object

    def create(self)->list:
        array = [self._randomizer.create() for _ in range(self._N)]
        if self._sorted:
            array.sort()
        return array


class Graph(Randomizer):
    def __init__(self, N=5, ratio=0.3, randomizer=None):
        super().__init__()
        self._N = N
        self._ratio = ratio
        self._randomizer = randomizer or Integer()
        self._directed = True
        self._weighted = False

    def directed(self, directed=True):
        self._directed = directed
        return self

    def weighted(self, weighted=True):
        self._weighted = weighted
        return self

    def get_type(self):
        return None

    def create(self)->list:
        graph = [[0 if i == j else (self.random.random() < self._ratio and
                                    (self._randomizer.create() if self._weighted else 1) or 0)
                  for j in range(self._N)] for i in range(self._N)]
        
        # Ensure undirected edges are mirrored
        if not self._directed:
            for i in range(self._N):
                for j in range(i, self._N):
                    graph[j][i] = graph[i][j]
        return graph
