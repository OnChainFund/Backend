from django import forms
from .models import LiquidityManagement


class LiquidityManagementForm(forms.ModelForm):
    class Meta:
        model = LiquidityManagement
        fields = "__all__"
