from django import forms

class TestForm(forms.Form):
    test_input = forms.CharField(label="Test Text", max_length=100)