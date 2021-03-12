from django.db import models

from django102.models.player import Player


class Game(models.Model):
    DIFFICULTY_LEVELS_CHOICES = (
        (0, 'Easy'),
        (1, 'Medium'),
        (2, 'Hard'),
    )
    name = models.CharField(max_length=30, blank=False, default='')
    level_of_difficulty = models.IntegerField(blank=False, choices=DIFFICULTY_LEVELS_CHOICES)
    players = models.ManyToManyField(Player)
