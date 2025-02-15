from django.contrib import admin

from .models import League, Round


class LeagueAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ace_pot",
        "user",
    ]


admin.site.register(League, LeagueAdmin)
admin.site.register(Round)
