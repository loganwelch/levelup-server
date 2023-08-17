from django.db import models


class Game(models.Model):
    """Game model class"""
    title = models.CharField(max_length=60)
    maker = models.CharField(max_length=60)
    number_of_players = models.IntegerField(3)
    skill_level = models.IntegerField(3)
    creator = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="created_games")
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="games")

    
