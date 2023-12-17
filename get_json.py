from typing import TypeAlias, NewType

import schemas
from convert_raw_dict_to_typed_dict import convert_raw_dict_to_typed_dict
from parse_textfile_to_raw_dict import parse_textfile_to_raw_dict
from models import AttributeItem, CategoryItem, get_item
from utils import get_index_of_string_in_list

Json: TypeAlias = str


class GetJsonFromFileException(Exception): pass
class InvalidPathException(GetJsonFromFileException): pass
class InvalidFileFormatException(GetJsonFromFileException): pass


def get_json_from_file(
        filename,
        path_to_file
) -> Json:

    try:
        raw_dictionary = parse_textfile_to_raw_dict(path_to_file=path_to_file, filename=filename)
    except FileNotFoundError as e:
        raise InvalidPathException(f"File/Directory didn't exists or path is invalid")
    except IOError as e:
        raise InvalidFileFormatException(f"Please check is file filled by correct format! \n metadata:{e}")
    except Exception as e:
        raise GetJsonFromFileException(f"Something went wrong. Please check your data and try again! \n metadata:{e}")

    try:
        dictionary = convert_raw_dict_to_typed_dict(raw_dictionary)
    except Exception as e:
        raise GetJsonFromFileException(f"Something went wrong. Please check your data and try again! \n metadata:{e}")

    _account_type: str = "Pro" if dictionary[2][0] == "Buy accesses" else "Free"
    _name: str = dictionary[6][0]
    _description: str = " ".join(dictionary[3]["to_description"])
    _short_description: str = "".join([
            f"{key}:\t{value}\n"
            for key, value in dictionary[3].items()
            if type(value) is str and len(value)
        ])[:-1]
    _categories: list[CategoryItem] = [CategoryItem(dictionary[5][0]).dict]
    _image_url: str = dictionary[6][get_index_of_string_in_list("jpg", dictionary[6]) ] if get_index_of_string_in_list("jpg", dictionary[6]) is not None else ""
    _file_url: str = dictionary[6][get_index_of_string_in_list("rar", dictionary[6]) ] if get_index_of_string_in_list("rar", dictionary[6]) is not None else ""
    _tags: list[dict[str, str]] = ([
        {"name": str(tag.strip())}
        for tag in dictionary[3]["tags"][0].split(":")
        if len(tag.strip()) != 0 and tag not in ["tags"]
    ] if len(dictionary[3]["tags"]) > 0 else [{"name": ""}])
    _attributes: list[AttributeItem] = [
        AttributeItem(id=1, name="Price", options=[_account_type]),
        AttributeItem(id=2, name="Render", options=[dictionary[3].get("Render").strip()]),
        AttributeItem(id=3, name="Style", options=[dictionary[3].get("Style").strip()])
    ]

    item = get_item(
        item_type=_account_type,
        name=_name,
        description=_description,
        short_description=_short_description,  # ?
        sku=filename[:-4], #  hrcnil ok a?
        categories=_categories,
        image_url=_image_url,
        file_url=_file_url,
        tags=_tags,
        attributes=_attributes
    )
    return item.model_dump_json()


