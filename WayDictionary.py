from Way import Way


class WayDictionary:
    def __init__(self):
        self.dictionary = dict()

    def __getitem__(self, key, level=0):
        item = self.dictionary[key]
        if type(item) == int:
            ret = self.__getitem__(self.dictionary[item], level+1)
            return ret
        print("after", item, type(item))
        return item

    def __setitem__(self, key, value):
        self.dictionary[key] = value

    def __str__(self):
        return str(self.dictionary)

    def way_valid(self, _id):
        if _id in self.dictionary:
            if not self.dictionary[_id] is int:
                return True
        return False


class EndDictionary:
    def __init__(self):
        self.dictionary = dict()

    def __getitem__(self, key):
        return self.dictionary[key]

    def __setitem__(self, key, value):
        if key not in self.dictionary:
            self.dictionary[key] = set()
        self.dictionary[key].add(value)

    def __contains__(self, item):
        return item in self.dictionary

    def __str__(self):
        return str(self.dictionary)
