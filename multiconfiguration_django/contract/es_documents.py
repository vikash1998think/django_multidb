from elasticsearch_dsl import Document, Keyword, Text

class ContractIndex(Document):
    name = Keyword()
    author = Keyword()
    contract_id = Keyword()
    description = Text(analyzer='snowball')
    content = Text(analyzer='snowball')
    header = Text(analyzer='snowball')
    footer = Text(analyzer='snowball')

    class Index:
        name = 'sample_index'
