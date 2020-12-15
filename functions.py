from WayDictionary import *


# def merge_ways(nodes, ways):
#     id_dict = create_id_dict(ways)
#     new_ways = []
#     print(id_dict)
#     for way in ways:
#         start = way.nodes[0].id
#         end = way.nodes[-1].id
#
#         node_ways = nodes[start].has_ways
#         node_ways_end = nodes[end].has_ways
#         if len(node_ways) == 2:
#             print("start", type(way))
#             second_way = id_dict[list(node_ways - {way.id})[0]]
#             way.merge(second_way)
#             id_dict[second_way.id] = way
#
#         if len(node_ways_end) == 2:
#             print("end", type(way))
#             second_way = id_dict[list(node_ways_end - {way.id})[0]]
#             way.merge(second_way)
#             id_dict[second_way.id] = way
#
#     ret = create_id_dict(id_dict.dictionary.values())
#
#     return ret


def merge_ways(nodes, ways):
    end_dict = create_end_dict(ways)
    return end_dict


def create_id_dict(ways):
    ret = WayDictionary()
    for w in ways:
        ret[w.id] = w
    return ret


def create_end_dict(ways):
    ret = EndDictionary()
    first = ways[0]
    for w in ways:
        ret[w.end1] = w
        ret[w.end2] = w
    #     if w.end1 in ret:
    #         ret[w.end1] = w
    #     else:
    #         ret[w.end2] = w
    # if first.end1 in ret and len(ret[first.end2]) == 1:
    #     del ret[first.end2]
    #     ret[w.end1] = first
    return ret
