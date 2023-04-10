from config import celery_app
from .es_documents import ContractIndex

@celery_app.task()
def create_contract_index(name, author, description, content, header, footer, contract_id, id):
    contract_index = ContractIndex(
        meta={"id": id},
        name=name,
        author=author,
        description=description,
        content=content,
        header=header,
        footer=footer,
        contract_id=contract_id
    )
    contract_index.save()
    return contract_index.id
