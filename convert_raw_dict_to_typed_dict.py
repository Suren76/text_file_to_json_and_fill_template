#
# {
#     1: ['https://3dsky.org/search?query=70651.52f8f4a88cfe5'],
#     2: ['Buy accesses', '297'],
#     3: [
#         'Platform: 3dsMax 2010 + fbx',
#         'Render: Vray',
#         'Size: 11 MB',
#         'Colors:',
#         'Style: Modern',
#         'Materials: Metal, Wood',
#         'Formfactor:',
#         'Published 10 February 2014',
#         'http://www.elfarus.ru/',
#         'tags: : : cloakroom: accessories'
#     ],
#     4: ['Furniture'],
#     5: ['Other'],
#     6: [
#         'Elfa dressing system',
#         'https://www.dropbox.com/scl/fi/mp8sheev8z7d9yxqj905i/70651.52f8f4a88cfe5.rar?rlkey=9xt7mf0snpehn51mvfwefbv3x&dl=1',
#         'https://www.dropbox.com/scl/fi/0x1dc1m4omze0y0lwb6y4/70651.52f8f4a88cfe5.jpg?rlkey=0f9ee4izc62orj7vjo68h4dn1&dl=1'
#     ]
# }




def convert_raw_dict_to_typed_dict(dictionary: dict) -> dict:
    dict_2 = {"others": [], "to_description": [], "tags": []}
    toggle = False

    for item in dictionary[3]:
        item: str = item.strip()

        if item.__contains__("Published"):
            toggle = not toggle
            continue

        if item.__contains__("tags"):
            dict_2["tags"].append(item)
            toggle = False
            continue

        if toggle: #  tuyl tex
            dict_2["to_description"].append(item)
            continue

        if item.count(":") == 1 and not item.__contains__("/"):
            dict_2[item.split(":")[0]] = item.split(":")[1]

    dictionary[3] = dict_2

    return dictionary
