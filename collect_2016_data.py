import mlbgame
import ipdb
import csv

date_stats = {}

for month in range(4, 11):
	for day in range(1, 32):
		if month == 4 and day >= 3 or month > 4:
			games = mlbgame.combine_games(mlbgame.games(2016, month, day))
			day_stats = {}
			for game in games:
				try:
					stats = mlbgame.player_stats(game.game_id)
				except ValueError as e:
					print(game.game_id)
					continue

				for player in stats['home_batting']:
					name = player.name_display_first_last
					if player.ab + player.bb + player.sf + player.sac + player.hbp > 2:
						day_stats['_'.join(player.name_display_first_last.split(' '))] = {
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
						day_stats['_'.join(player.name_display_first_last.split(' '))] = {
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
			if day_stats:
				date_stats['{}/{}/{}'.format(month, day, 2016)] = day_stats
	ipdb.set_trace()
