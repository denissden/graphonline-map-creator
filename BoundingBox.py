class BoundingBox:
    x1, y1 = (0, 0)
    x2, y2 = (800, 400)

    def __init__(self, lat1, long1, lat2, long2):
        if lat1 < lat2:
            self.lat1 = lat1
            self.lat2 = lat2
        else:
            self.lat2 = lat1
            self.lat1 = lat2

        if long1 < long2:
            self.long1 = long1
            self.long2 = long2
        else:
            self.long2 = long1
            self.long1 = long2

    def SetSize(self, pos1, pos2=None):
        if pos2 is None:
            self.x2, self.y2 = pos1
        else:
            self.x1, self.y1 = pos1
            self.x2, self.y2 = pos2

    def ConvertToXY(self, node):
        n_lat, n_long = node.lat, node.long
        d_lat = self.lat2 - self.lat1
        d_long = self.long2 - self.long1

        d_y = self.lat2 - n_lat
        d_x = self.long2 - n_long

        d_sizex = self.x2 - self.x1
        d_sizey = self.y2 - self.y1

        y = d_y / d_lat * d_sizey + self.y1
        x = (1 - d_x / d_long) * d_sizex + self.x1

        return x, y

    def __str__(self):
        return f"{self.lat1},{self.long1},{self.lat2},{self.long2}"

