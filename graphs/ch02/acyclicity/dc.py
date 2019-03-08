from dataclasses import dataclass, field


@dataclass
class Vertex:
    id: int
    pre: int
    post: int
    neighbors: set = field(repr=False)

    def __post_init__(self):
        if not self.neighbors:
            self.neighbors = set()

    def __hash__(self):
        return hash(self.id)


v0 = Vertex(0, None, None, None)
v1 = Vertex(1, None, None, None)
v2 = Vertex(2, None, None, None)
v3 = Vertex(3, None, None, None)
v4 = Vertex(4, None, None, None)


vertices = set((v0, v1, v2, v3, v4))
v0.neighbors = {v1}
v1.neighbors = {v2, v4}
v2.neighbors = {v0}
v3.neighbors = {v0, v2}
v4.neighbors = {}


print(vertices)
