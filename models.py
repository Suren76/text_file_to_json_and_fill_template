from pydantic import BaseModel
from config import CATEGORIES_LIST


class AttributeItem(BaseModel):
    id: int
    name: str
    options: list[str]


class DownloadItem(BaseModel):
    name: str
    file: str


class ItemBaseModel(BaseModel):
    name: str
    type: str
    regular_price: str
    description: str
    short_description: str
    # sku: str
    # categories: list[dict[str, str]]
    # tags: list[dict[str, str]]
    # images: list[dict[str, str]]
    # attributes: list[AttributeItem]


class ItemProModel(ItemBaseModel):
    sku: str
    categories: list[dict[str, str]]
    downloadable: bool
    downloads: list[DownloadItem]
    tags: list[dict[str, str]]
    images: list[dict[str, str]]
    attributes: list[AttributeItem]

    type: str = "simple"
    regular_price: str = "2"


class ItemFreeModel(ItemBaseModel):
    external_url: str
    sku: str
    categories: list[dict[str, str]]
    tags: list[dict[str, str]]
    images: list[dict[str, str]]
    attributes: list[AttributeItem]
    button_text: str = "Download"  #  arje?

    type: str = "external"
    regular_price: str = "0"


class CategoryItem:
    _CATEGORIES_LIST = CATEGORIES_LIST

    id: int = None
    name: str = None

    def __init__(self, _name):
        if _name in self._CATEGORIES_LIST:
            self.id = self._CATEGORIES_LIST.get(_name)
        else:
            self.name = _name

    @property
    def dict(self):
        return {"id": self.id} if self.id is not None else {"name": self.name}


def get_item(
        item_type: str,
        name: str,
        description: str,
        short_description: str,
        sku: str,
        categories: list[CategoryItem],
        image_url: str,
        tags: list[dict[str, str]],
        attributes: list[AttributeItem],
        file_url: str
) -> ItemBaseModel:
    _image_block = [{"src": image_url}]
    _file_url: str = file_url

    if item_type == "Free":
        return ItemFreeModel(
            name=name,
            description=description,
            short_description=short_description,
            sku=sku,
            categories=categories,
            images=_image_block,
            tags=tags,
            attributes=attributes,

            external_url=file_url
        )
    elif item_type == "Pro":
        return ItemProModel(
            name=name,
            description=description,
            short_description=short_description,
            categories=categories,

            sku=sku,
            images=_image_block,
            tags=tags,
            attributes=attributes,

            downloads=[DownloadItem(name=sku, file=_file_url)],
            downloadable=True
        )
