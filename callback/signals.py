from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from .models import Game


def players_num(sender, **kwargs):
    if kwargs['instance'].players.count() > 6:
        raise ValidationError("Game can not contain more than five players simultaneously")


m2m_changed.connect(players_num, sender=Game.players.through)