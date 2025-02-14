from django.urls import path

from .views import (
    LeagueListView,
    LeagueDetailView,
    LeagueDetailRounds,
    LeagueCreateView,
    LeagueUpdateView,
    LeagueDeleteView,
)

urlpatterns = [
    path("", LeagueListView.as_view(), name="league_list"),
    path("new/", LeagueCreateView.as_view(), name="league_new"),
    path("<int:pk>/", LeagueDetailView.as_view(), name="league_detail"),
    path("<int:pk>/rounds/", LeagueDetailRounds.as_view(), name="league_detail_rounds"),
    path("<int:pk>/edit/", LeagueUpdateView.as_view(), name="league_edit"),
    path("<int:pk>/delete/", LeagueDeleteView.as_view(), name="league_delete"),
]
