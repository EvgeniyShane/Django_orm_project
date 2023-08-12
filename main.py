from django.db import models
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db.settings")
import django
django.setup()
from pathlib import Path

from db.models import Team, Match, PremierLeagueStats, Player, PlayerGoalsAssists

teams_data = [
    {'team_id': 1, 'team_name': 'Liverpool'},
    {'team_id': 2, 'team_name': 'Manchester City'},
    {'team_id': 3, 'team_name': 'Manchester United'},
    {'team_id': 4, 'team_name': 'Chelsea'},
    {'team_id': 5, 'team_name': 'Tottenham Hotspur'},
    {'team_id': 6, 'team_name': 'Arsenal'},
    {'team_id': 7, 'team_name': 'Newcastle United'},
]

for data in teams_data:
    team = Team(**data)
    team.save()

matches_json_path = Path(__file__).resolve().parent / 'Matches.json'

with open(matches_json_path, 'r') as json_file:
    matches_data = json.load(json_file)

for data in matches_data:
    match = Match(
        match_id=data['match_id'],
        home_team_id=data['home_team_id'],
        away_team_id=data['away_team_id'],
        home_team_goals=data['home_team_goals'],
        away_team_goals=data['away_team_goals']
    )
    match.save()

teams = Team.objects.all()
for team in teams:
    stats = PremierLeagueStats(team=team)
    stats.save()

players_data = [
    {'player_id': 1, 'player_name': 'Salah'},
    {'player_id': 2, 'player_name': 'Firmino'},
    {'player_id': 3, 'player_name': 'Mane'},
    {'player_id': 4, 'player_name': 'Holland'},
    {'player_id': 5, 'player_name': 'Haaland'},
    {'player_id': 6, 'player_name': 'Jesus'},
    {'player_id': 7, 'player_name': 'Gundogan'},
    {'player_id': 8, 'player_name': 'Rashford'},
    {'player_id': 9, 'player_name': 'Sterling'},
    {'player_id': 10, 'player_name': 'Abraham'},
    {'player_id': 11, 'player_name': 'Kane'},
    {'player_id': 12, 'player_name': 'Son'},
    {'player_id': 13, 'player_name': 'Lacazette'},
    {'player_id': 14, 'player_name': 'Martinelli'},
    {'player_id': 15, 'player_name': 'Henderson'},
    {'player_id': 16, 'player_name': 'Wilson'},
    {'player_id': 17, 'player_name': 'Pulisic'},
    {'player_id': 18, 'player_name': 'Fernandes'},
    {'player_id': 19, 'player_name': 'Ronaldo'},
    {'player_id': 20, 'player_name': 'Odegaard'},
    {'player_id': 21, 'player_name': 'Van Dijk'},
    {'player_id': 22, 'player_name': 'Saint-Maximin'},
]

for data in players_data:
    player = Player(**data)
    player.save()


player_goals_assists_json_path = Path(__file__).resolve().parent / 'PlayerGoalsAssists.json'

with open(player_goals_assists_json_path, 'r') as json_file:
    player_goals_assists_data = json.load(json_file)

for data in player_goals_assists_data:
    player = Player.objects.get(pk=data['player_id'])
    match = Match.objects.get(pk=data['match_id'])
    team = Team.objects.get(pk=data['team_id'])
    
    player_goals_assists = PlayerGoalsAssists(
        player=player,
        match=match,
        team=team,
        goals_scored=data['goals_scored'],
        assists_made=data['assists_made']
    )
    player_goals_assists.save()

print("Записи успешно добавлены в таблицы.")