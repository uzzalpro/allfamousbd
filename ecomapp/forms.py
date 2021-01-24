from django import forms


class SearchForms(forms.Form):
    query = forms.CharField(max_length=200)
    cat_id = forms.IntegerField()