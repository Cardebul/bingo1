from django import forms

from .models import DataModel, DataModelThree, MainMod


class DataForm(forms.ModelForm):
    class Meta:
        model = DataModel
        exclude = ('user', 'bingo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.convert_fields_to_textarea()

    def convert_fields_to_textarea(self):
        for field_name in self.fields.keys():
            self.fields[field_name].widget = forms.Textarea(
                attrs={'maxlength': '18', 'id': 'fieldforinfo'}
                )


class DataFormThree(forms.ModelForm):
    class Meta:
        model = DataModelThree
        exclude = ('user', 'bingo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.convert_fields_to_textarea()

    def convert_fields_to_textarea(self):
        for field_name in self.fields.keys():
            self.fields[field_name].widget = forms.Textarea(
                attrs={'maxlength': '18', 'id': 'fieldforinfo'}
                )


class TestForm(forms.ModelForm):
    GRID_CHOICES = (
        (False, '3x3'),
        (True, '5x5'),
    )
    mod = forms.ChoiceField(choices=GRID_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = MainMod
        fields = ('mod',)