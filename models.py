from django.db import models

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.TextField()

class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_team_goals = models.IntegerField(null=True, blank=True)
    away_team_goals = models.IntegerField(null=True, blank=True)

class PremierLeagueStats(models.Model):
    stat_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.TextField(unique=True)

class PlayerGoalsAssists(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    goals_scored = models.IntegerField()
    assists_made = models.IntegerField()
    