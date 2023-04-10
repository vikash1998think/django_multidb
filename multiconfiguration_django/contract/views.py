from django.shortcuts import render
from django.db import transaction

from .models import Contract
from .forms import ContractForm
from .documents import Contract as ContractDocument
from .es_documents import ContractIndex
from .tasks import create_contract_index

@transaction.atomic
def create_contract(request):
    form = None
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        description = data.get("description")
        content = data.get("content")
        header = data.get("header")
        footer = data.get("footer")

        contract_content = ContractDocument(content=content, header=header, footer=footer)
        contract_content.save()

        contract = Contract(name=name, description=description, created_by=request.user, data=contract_content.id)
        contract.save()

        create_contract_index.delay(
            id=str(contract_content.id),
            name=name,
            author=int(request.user.pk),
            description=description,
            content=content,
            header=header,
            footer=footer,
            contract_id=int(contract.pk)
        )
    else:
        form = ContractForm()

    return render(request, "contract.html", {"form": form})


def get_contract(request, pk):
    contract = Contract.objects.get(id=pk)
    contract_content = ContractDocument.objects.get(id=contract.data)
    return render(request, "content.html", {"contract": contract, "contract_content": contract_content})

def search_contract(request):
    contracts = ContractIndex.search()
    if request.GET:
        if request.GET.get("author"):
            contracts = contracts.query("match", author=int(request.GET.get("author")))
        if request.GET.get("desc"):
            contracts = contracts.query("match", description=request.GET.get("desc"))
    return render(request, "search.html", {"contracts": contracts.execute()})
