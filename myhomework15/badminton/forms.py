from django import forms
from badminton.models import Minton

class MintonForm(forms.ModelForm):
    class Meta:
        model = Minton
        fields = "__all__"
