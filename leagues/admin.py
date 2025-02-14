from django.contrib import admin

from .models import League


class LeagueAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ace_pot",
        "user",
    ]


admin.site.register(League, LeagueAdmin)
