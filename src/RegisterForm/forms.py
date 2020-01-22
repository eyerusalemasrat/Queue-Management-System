from django.forms import forms


class ExampleForm(forms.Form):
    field1 = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=(('enterprise','enterprise'),('residential','residential'),))