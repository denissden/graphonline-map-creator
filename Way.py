class Way:
    def __init__(self, _id, nodes, name):
        self.id = _id
        self.nodes = nodes
        for node in nodes:
            node.has_ways.add(_id)
        self.end1 = nodes[0].id
        self.end2 = nodes[-1].id

        self.name = name

    def __str__(self):
        return f"{self.id} : {self.name} {self.nodes}"

    def get_start_end(self):
        self.nodes[0].is_end += 1
        self.nodes[-1].is_end += 1
        return self.nodes[0], self.nodes[-1]

    def merge(self, way):
        start = self.nodes[0].id
        end = self.nodes[-1].id

        second_start = way.nodes[0].id
        second_end = way.nodes[-1].id

        if start == second_start:
            self.nodes = way.nodes[::-1] + self.nodes[1:]
        elif start == second_end:
            self.nodes = way.nodes + self.nodes[1:]
        elif end == second_start:
            self.nodes = self.nodes + way.nodes[1:]
        elif end == second_end:
            self.nodes = self.nodes[:-1] + way.nodes[::-1]
        else:
            print("OOPS")

    # def merge(self, way):
    #     if type(way) == int:
    #         return way
    #
    #     start = self.nodes[0].id
    #     end = self.nodes[-1].id
    #
    #     second_start = way.nodes[0].id
    #     second_end = way.nodes[-1].id
    #
    #     n = None
    #     if start == second_start:
    #         n = way.nodes[:1:-1] + self.nodes
    #     elif start == second_end:
    #         n = way.nodes[:-1] + self.nodes
    #     elif end == second_start:
    #         n = self.nodes + way.nodes[1:]
    #     elif end == second_end:
    #         n = self.nodes + way.nodes[-2::-1]
    #     else:
    #         n = self.nodes
    #     return Way(self.id, n, self.name)

