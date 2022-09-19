from django import forms
from .models import LiquidityManagement, Strategy, Weight


class LiquidityManagementForm(forms.ModelForm):
    class Meta:
        model = LiquidityManagement
        fields = "__all__"


class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = "__all__"


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = "__all__"
