from django import forms


class ContractForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()

    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 6}))
    header = forms.CharField(widget=forms.Textarea(attrs={"rows": 6}))
    footer = forms.CharField(widget=forms.Textarea(attrs={"rows": 6}))
    