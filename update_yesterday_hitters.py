from __future__ import print_function

import mlbgame
import datetime
import csv
import ipdb

today = datetime.datetime.utcnow()
month = today.month
day = today.day - 1
year = today.year

directory = 'steamer_ros/' + str(month) + str(day) + str(year) + '/'
filename = directory + 'steamer_ros_batting_' + str(month) + str(day) + str(year) + '.csv'
output_filename = directory + 'steamer_ros_batting_updated_hits_' + str(month) + str(day) + str(year) + '.csv'
output_file = open(output_filename, 'wb')
output_writer = csv.writer(output_file)

yesterdays_player_stats = {}

yesterdays_games = mlbgame.day(year, month, day)
for game in yesterdays_games:
	try:
		stats = mlbgame.player_stats(game.game_id)
	except ValueError as e:
		print(game.game_id)
		continue

	for player in stats['home_batting']:
		name = player.name_display_first_last
		if player.ab + player.bb + player.sf + player.sac + player.hbp > 2:
			yesterdays_player_stats['_'.join(player.name_display_first_last.split(' '))] = {
				'game_hits': player.h,
				'game_ab': player.ab,
				'game_bb': player.bb,
				'game_sf': player.sf,
				'game_sac': player.sac,
				'game_hbp': player.hbp,
				'opposing_pitcher': stats['away_pitching'][0].name_display_first_last,
				'opposing_team': game.away_team,
				'stadium': game.home_team
				#batting order at some point
			}

	for player in stats['away_batting']:
		name = player.name_display_first_last
		if player.ab + player.bb + player.sf + player.sac + player.hbp > 2:
			yesterdays_player_stats['_'.join(player.name_display_first_last.split(' '))] = {
				'game_hits': player.h,
				'game_ab': player.ab,
				'game_bb': player.bb,
				'game_sf': player.sf,
				'game_sac': player.sac,
				'game_hbp': player.hbp,
				'opposing_pitcher': stats['home_pitching'][0].name_display_first_last,
				'opposing_team': game.home_team,
				'stadium': game.home_team
				#batting order at some point
			}

with open(filename) as csvfile:
	reader = csv.reader(csvfile)
	for i, row in enumerate(reader):
		if i == 0:
			new_row = row + ['game_hits', 'game_ab', 'game_pa', 'opposing_pitcher', 'opposing_team', 'stadium']
			output_writer.writerow(new_row)
		else:
			player_name = row[0]
			player_team = row[1]
			
			player_id = '_'.join(player_name.split(' '))
			player_game_stats = yesterdays_player_stats.get(player_id, {})
			player_game_hits = player_game_stats.get('game_hits', 0)
			player_game_ab = player_game_stats.get('game_ab', 0)
			player_game_pa = player_game_stats.get('game_ab', 0) + player_game_stats.get('game_bb', 0) + player_game_stats.get('game_sf', 0) + player_game_stats.get('game_sac', 0) + player_game_stats.get('game_hbp', 0)
			if player_game_pa > 2:
				new_row = row + [player_game_hits, player_game_ab, player_game_pa, player_game_stats.get('opposing_pitcher', ' '), player_game_stats.get('opposing_team', ' '), player_game_stats.get('stadium', ' ')]
				output_writer.writerow(new_row) 

