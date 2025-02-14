from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import League


class LeagueListView(ListView):
    model = League
    template_name = "leagues/league_list.html"


class LeagueDetailView(DetailView):
    model = League
    template_name = "leagues/league_detail_leaderboard.html"


class LeagueDetailRounds(DetailView):
    model = League
    template_name = "leagues/league_detail_rounds.html"


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
