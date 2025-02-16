from django import forms

from .models import Round, Player


class RoundForm(forms.ModelForm):
    class Meta:
        model = Round
        fields = [
            "name",
            "par",
        ]


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "name",
            "udisc_name",
        ]
