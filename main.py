import requests
from Node import Node
from Way import Way
from BoundingBox import BoundingBox
import matplotlib.pyplot as plt
from functions import merge_ways
from pprint import pprint



# query = """
# [out:json];
# area["ISO3166-1"="DE"][admin_level=2];
# (node["amenity"="biergarten"](area);
#  way["amenity"="biergarten"](area);
#  rel["amenity"="biergarten"](area);
# );
# out center;
# """

# VERY LIGHT
lat1 = 55.751117
long1 = 37.617357

lat2 = 55.754545
long2 = 37.623251

# LIGHT
lat1 = 55.749117
long1 = 37.611357

lat2 = 55.755245
long2 = 37.625251

# JUST WHY
# lat1 = 55.709117
# long1 = 37.601357
#
# lat2 = 55.805245
# long2 = 37.705251

# BRO YOU ARE INSANE
# lat1 = 55.609117
# long1 = 37.501357
#
# lat2 = 55.905245
# long2 = 37.805251

bbox = BoundingBox(lat1, long1, lat2, long2)
query = f"""
[out:json]
[bbox:{bbox}];
way[highway~"^(service|primary|secondary)$"];
(._;>;);
out center; 
"""

print(query)

response = requests.get("https://overpass-api.de/api/interpreter", params={"data": query})
json = response.json()
elements = json["elements"]

nodes = dict()
ways = []
for key in elements:
    if key["type"] == "node":
        _id = key["id"]
        _long = key["lon"]
        _lat = key["lat"]
        n = Node(_id, _lat, _long)
        n.SetWorkArea(bbox)
        nodes[int(_id)] = n
    elif key["type"] == "way":
        _id = int(key["id"])
        _nodes = [nodes[i] for i in key["nodes"]]
        try:
            _name = key["tags"]["name"]
        except:
            _name = "NONE"
        ways.append(Way(_id, _nodes, _name))

print(*nodes.values(), sep='\n')
#print(*ways, sep='\n')

way_dict = merge_ways(nodes, ways)
pprint(way_dict.dictionary)


plt.xlabel("x")
plt.ylabel("y")
# plt.figure(num=None, figsize=(60, 40), dpi=70)
plt.gca().invert_yaxis()


has1 = []
has2 = []
has3 = []
hasmore = []
for k in way_dict.dictionary.keys():
    node = nodes[k]
    c = len(node.has_ways)
    if c == 1:
        has1.append(node.xy())
    elif c == 2:
        has3.append(node.xy())
    elif c == 3:
        has2.append(node.xy())
    else:
        hasmore.append(node.xy())

plt.plot(*zip(*[k for k in has1]), "o")
plt.plot(*zip(*[k for k in has2]), "o")
plt.plot(*zip(*[k for k in has3]), "o")
plt.plot(*zip(*[k for k in hasmore]), "o")
# plot = [nodes[k].xy() for k in way_dict.dictionary.keys()]
# plt.plot(*zip(*plot), "o")
# plt.plot([n.x for _, n in nodes.items() if n.is_end],
#          [n.y for _, n in nodes.items() if n.is_end], "o")
# plt.plot([n.x for _, n in nodes.items() if n.has_valid_ways(way_dict) > 1],
#          [n.y for _, n in nodes.items() if n.has_valid_ways(way_dict) > 1], "o")
# plt.plot([n.x for _, n in nodes.items() if len(n.has_ways) > 2],
#          [n.y for _, n in nodes.items() if len(n.has_ways) > 2], "o")

# for way in way_dict.dictionary.values():
for way in ways:
    _x = []
    _y = []
    for node in way.nodes:
        _x.append(node.x)
        _y.append(node.y)
    plt.plot(_x, _y, )

plt.show()


