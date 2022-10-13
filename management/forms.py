from django import forms
from .models import PriceManagement, Strategy, Weight


class PriceManagementForm(forms.ModelForm):
    class Meta:
        model = PriceManagement
        fields = "__all__"


class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = "__all__"


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = "__all__"
