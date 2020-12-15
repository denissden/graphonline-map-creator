class Node:
    def __init__(self, _id, lat, long):
        self.id = _id
        self.long = long
        self.lat = lat
        self.has_ways = set()
        self.x = None
        self.y = None
        self.is_end = 0

    def __str__(self):
        return f"{self.id} : {self.lat} {self.long}, {self.x} {self.y}"

    def SetWorkArea(self, workarea):
        self.x, self.y = workarea.ConvertToXY(self)

    def xy(self):
        return self.x, self.y

    def has_valid_ways(self, way_dictionary):
        c = 0
        # print(self.has_ways)
        for w in self.has_ways:
            if way_dictionary.way_valid(w):
                c += 1
        return c

    def is_road_end(self, way_dictionary):
        for w in self.has_ways:
            try:
                way = way_dictionary[w]
                if self.id == way.nodes[0].id or self.id == way.nodes[-1].id:
                    return True
            except:
                pass
        return False
