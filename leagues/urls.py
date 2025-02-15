from django.urls import path

from .views import (
    LeagueListView,
    LeagueDetailView,
    LeagueDetailRounds,
    LeagueCreateView,
    LeagueUpdateView,
    LeagueDeleteView,
    RoundCreateView,
    RoundDetailView,
)

urlpatterns = [
    # Leagues
    path("leagues/", LeagueListView.as_view(), name="league_list"),
    path("leagues/new/", LeagueCreateView.as_view(), name="league_new"),
    path("leagues/<int:pk>/", LeagueDetailView.as_view(), name="league_detail"),
    path(
        "leagues/<int:pk>/rounds/",
        LeagueDetailRounds.as_view(),
        name="league_detail_rounds",
    ),
    path("leagues/<int:pk>/edit/", LeagueUpdateView.as_view(), name="league_edit"),
    path("leagues/<int:pk>/delete/", LeagueDeleteView.as_view(), name="league_delete"),
    # Rounds
    path("leagues/<int:pk>/new-round/", RoundCreateView.as_view(), name="round_new"),
    path(
        "rounds/<int:pk>",
        RoundDetailView.as_view(),
        name="round_detail",
    ),
]
