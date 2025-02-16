from django.urls import path

from .views import (
    LeagueListView,
    LeagueDetailView,
    LeagueDetailRounds,
    LeagueDetailPlayers,
    LeagueCreateView,
    LeagueUpdateView,
    LeagueDeleteView,
    RoundCreateView,
    RoundDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView,
)

urlpatterns = [
    # Leagues
    path("leagues/", LeagueListView.as_view(), name="league_list"),
    path("leagues/new/", LeagueCreateView.as_view(), name="league_new"),
    path(
        "leagues/<int:pk>/leaderboard/",
        LeagueDetailView.as_view(),
        name="league_detail",
    ),
    path(
        "leagues/<int:pk>/rounds/",
        LeagueDetailRounds.as_view(),
        name="league_detail_rounds",
    ),
    path(
        "leagues/<int:pk>/players/",
        LeagueDetailPlayers.as_view(),
        name="league_detail_players",
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
    # Players
    path("leagues/<int:pk>/new-player/", PlayerCreateView.as_view(), name="player_new"),
    path("players/<int:pk>/edit/", PlayerUpdateView.as_view(), name="player_edit"),
    path("players/<int:pk>/delete/", PlayerDeleteView.as_view(), name="player_delete"),
]
