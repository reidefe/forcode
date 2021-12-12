from django.contrib import admin
from django.db import models # noqa
from .models import Player, Game

class PlayerAdmin(admin.ModelAdmin):    
    list_display = ('id','name','email', 'games_in', 'created', 'updated')
    search_fields = ('name', 'email')

    def games_in(self, obj):
        player = obj.player_games.all().values_list('name', flat=True)
        pl = [p for p in player]
        return pl
admin.site.register(Player, PlayerAdmin)


class GamePlayers(admin.StackedInline):
    model = Game.players.through


class GameAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'game_players', 'created', 'updated')
    model=Game
    inlines = [GamePlayers]
    def game_players(self, obj):        
        player = obj.players.all().values_list('name', flat=True)
        pl = [p for p in player]
        return pl    
admin.site.register(Game, GameAdmin)