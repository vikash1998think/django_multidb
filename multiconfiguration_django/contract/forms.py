from django import forms


class ContractForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()

    content = forms.CharField(widget=forms.Textarea)
    header = forms.CharField(widget=forms.Textarea)
    footer = forms.CharField(widget=forms.Textarea)
    