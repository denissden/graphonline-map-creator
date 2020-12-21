from WayDictionary import *
import string

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



def translit1(string):
    """ This function works just fine """
    capital_letters = {
        u'А': u'A',
        u'Б': u'B',
        u'В': u'V',
        u'Г': u'G',
        u'Д': u'D',
        u'Е': u'E',
        u'Ё': u'E',
        u'Ж': u'Zh',
        u'З': u'Z',
        u'И': u'I',
        u'Й': u'Y',
        u'К': u'K',
        u'Л': u'L',
        u'М': u'M',
        u'Н': u'N',
        u'О': u'O',
        u'П': u'P',
        u'Р': u'R',
        u'С': u'S',
        u'Т': u'T',
        u'У': u'U',
        u'Ф': u'F',
        u'Х': u'H',
        u'Ц': u'Ts',
        u'Ч': u'Ch',
        u'Ш': u'Sh',
        u'Щ': u'Sch',
        u'Ъ': u'',
        u'Ы': u'Y',
        u'Ь': u'',
        u'Э': u'E',
        u'Ю': u'Yu',
        u'Я': u'Ya'
    }

    lower_case_letters = {
        u'а': u'a',
        u'б': u'b',
        u'в': u'v',
        u'г': u'g',
        u'д': u'd',
        u'е': u'e',
        u'ё': u'e',
        u'ж': u'zh',
        u'з': u'z',
        u'и': u'i',
        u'й': u'y',
        u'к': u'k',
        u'л': u'l',
        u'м': u'm',
        u'н': u'n',
        u'о': u'o',
        u'п': u'p',
        u'р': u'r',
        u'с': u's',
        u'т': u't',
        u'у': u'u',
        u'ф': u'f',
        u'х': u'h',
        u'ц': u'ts',
        u'ч': u'ch',
        u'ш': u'sh',
        u'щ': u'sch',
        u'ъ': u'',
        u'ы': u'y',
        u'ь': u'',
        u'э': u'e',
        u'ю': u'yu',
        u'я': u'ya'
    }

    translit_string = ""

    for index, char in enumerate(string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(string) > index+1:
                if string[index+1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char

    return translit_string