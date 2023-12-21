SCHEMA_PRO = {
    '$defs': {
        'AttributeItem': {
            'properties': {
                'id': {
                    'title': 'Id',
                    'type': 'integer'
                },
                'name': {
                    'title': 'Name',
                    'type': 'string'
                },
                'options': {
                    'items': {
                        'type': 'string'
                    },
                    'title': 'Options',
                    'type': 'array'
                }
            },
            'required': [
                'id',
                'name',
                'options'
            ],
            'title': 'AttributeItem',
            'type': 'object'
        },
        'DownloadItem': {
            'properties': {
                'name': {
                    'title': 'Name',
                    'type': 'string'
                },
                'file': {
                    'title': 'File',
                    'type': 'string'
                }
            },
            'required': [
                'name',
                'file'
            ],
            'title': 'DownloadItem',
            'type': 'object'
        }
    },
    'properties': {
        'name': {
            'title': 'Name',
            'type': 'string'
        },
        'type': {
            'default': 'simple',
            'title': 'Type',
            'type': 'string'
        },
        'regular_price': {
            'default': '2',
            'title': 'Regular Price',
            'type': 'string'
        },
        'description': {
            'title': 'Description',
            'type': 'string'
        },
        'short_description': {
            'title': 'Short Description',
            'type': 'string'
        },
        'sku': {
            'title': 'Sku',
            'type': 'string'
        },
        'categories': {
            'items': {
                'additionalProperties': {
                    'type': 'string'
                },
                'type': 'object'
            },
            'title': 'Categories',
            'type': 'array'
        },
        'tags': {
            'items': {
                'additionalProperties': {
                    'type': 'string'
                },
                'type': 'object'
            },
            'title': 'Tags',
            'type': 'array'
        },
        'images': {
            'items': {
                'additionalProperties': {
                    'type': 'string'
                },
                'type': 'object'
            },
            'title': 'Images',
            'type': 'array'
        },
        'attributes': {
            'items': {
                '$ref': '#/$defs/AttributeItem'
            },
            'title': 'Attributes',
            'type': 'array'
        },
        'downloadable': {
            'title': 'Downloadable',
            'type': 'boolean'
        },
        'downloads': {
            'items': {
                '$ref': '#/$defs/DownloadItem'
            },
            'title': 'Downloads',
            'type': 'array'
        }
    },
    'required': [
        'name',
        'description',
        'short_description',
        'sku',
        'categories',
        'tags',
        'images',
        'attributes',
        'downloadable',
        'downloads'
    ],
    'title': 'ItemProModel',
    'type': 'object'
}
