from mongoengine import Document, fields

class Contract(Document):

    meta = {
        'collection': 'contract_contents',
        'auto_create_index': True,
    }

    content = fields.StringField()
    header = fields.StringField()
    footer = fields.StringField()
