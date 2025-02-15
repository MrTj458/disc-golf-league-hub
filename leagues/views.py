from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

from .models import League, Round, Player
from .forms import RoundForm, PlayerForm


class LeagueListView(ListView):
    model = League
    template_name = "leagues/league_list.html"


class LeagueDetailView(DetailView):
    model = League
    template_name = "leagues/league_detail_leaderboard.html"


class LeagueDetailRounds(DetailView):
    model = League
    template_name = "leagues/league_detail_rounds.html"


class LeagueDetailPlayers(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = League
    template_name = "leagues/league_detail_players.html"

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.user == self.request.user  # type: ignore


class LeagueCreateView(LoginRequiredMixin, CreateView):
    model = League
    template_name = "leagues/league_new.html"
    fields = [
        "name",
        "url",
        "default_payout_buy_in",
        "default_ace_pot_buy_in",
        "default_ctp_buy_in",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LeagueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = League
    template_name = "leagues/league_edit.html"
    fields = [
        "name",
        "url",
        "default_payout_buy_in",
        "default_ace_pot_buy_in",
        "default_ctp_buy_in",
        "ace_pot",
    ]

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.user == self.request.user  # type: ignore


class LeagueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = League
    template_name = "leagues/league_delete.html"
    success_url = reverse_lazy("league_list")

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.user == self.request.user  # type: ignore


class RoundDetailView(DetailView):
    model = Round
    template_name = "leagues/round_detail.html"


class RoundCreateView(
    LoginRequiredMixin, UserPassesTestMixin, SingleObjectMixin, FormView
):
    model = League
    form_class = RoundForm
    template_name = "leagues/round_new.html"

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.user == self.request.user  # type: ignore

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        round = form.save(commit=False)
        round.league = self.object
        round.save()
        self.success_url = reverse("round_detail", kwargs={"pk": round.pk})
        return super().form_valid(form)


class PlayerCreateView(
    LoginRequiredMixin, UserPassesTestMixin, SingleObjectMixin, FormView
):
    model = League
    form_class = PlayerForm
    template_name = "leagues/player_new.html"

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.user == self.request.user  # type: ignore

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        round = form.save(commit=False)
        round.league = self.object
        round.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("league_detail_players", kwargs={"pk": self.object.pk})


class PlayerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Player
    template_name = "leagues/player_edit.html"
    fields = [
        "name",
        "udisc_name",
    ]

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.league.user == self.request.user  # type: ignore


class PlayerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Player
    template_name = "leagues/player_delete.html"
    success_url = reverse_lazy("league_detail_players")

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.league.user == self.request.user  # type: ignore

    def get_success_url(self) -> str:
        player = self.get_object()
        league = player.league  # type: ignore
        return reverse("league_detail_players", kwargs={"pk": league.pk})
