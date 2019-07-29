from django import forms


class bdd(forms.Form):
    title = forms.CharField(label='Enter your title', max_length=100, required=True)
    text = forms.CharField(label='Enter your text', max_length=300,
                           required=True, widget=forms.Textarea())
