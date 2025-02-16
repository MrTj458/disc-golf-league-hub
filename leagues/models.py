from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

from .base_models import BaseModel


class League(BaseModel):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    default_payout_buy_in = models.IntegerField()
    default_ace_pot_buy_in = models.IntegerField()
    default_ctp_buy_in = models.IntegerField()
    ace_pot = models.IntegerField(default=0)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("league_detail", kwargs={"pk": self.pk})


def default_round_name():
    return timezone.now().strftime("%m/%d/%Y")


class Round(BaseModel):
    name = models.CharField(max_length=200, default=default_round_name)
    par = models.IntegerField(default=54)
    payout = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)

    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("round_detail", kwargs={"pk": self.pk})


class Player(BaseModel):
    name = models.CharField(max_length=250)
    udisc_name = models.CharField(max_length=250, blank=True)

    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("league_detail_players", kwargs={"pk": self.league.pk})


# class Score(BaseModel):
#     score = models.IntegerField(null=True)
#     place = models.CharField(max_length=25, null=True)
#     payout = models.IntegerField()
#     start_tag = models.IntegerField(null=True)
#     end_tag = models.IntegerField(null=True)
#     buy_in = models.BooleanField(default=False)

#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     round = models.ForeignKey(Round, on_delete=models.CASCADE)


# class CTP(BaseModel):
#     hole = models.IntegerField()
#     buy_in = models.IntegerField()
#     payout = models.IntegerField(default=0)

#     winner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
#     round = models.ForeignKey(Round, on_delete=models.CASCADE)
