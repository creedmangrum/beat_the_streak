from __future__ import print_function

import mlbgame
import datetime
import csv
import ipdb

today = datetime.datetime.utcnow()
month = today.month
day = today.day
year = today.year

directory = 'steamer_ros/' + str(month) + str(day) + str(year) + '/'
filename = directory + 'steamer_ros_pitching_' + str(month) + str(day) + str(year) + '.csv'
output_filename = directory + 'steamer_row_pitching_probables_' + str(month) + str(day) + str(year) + '.csv'
output_file = open(output_filename, 'wb')
output_writer = csv.writer(output_file)

todays_games = mlbgame.day(year, month, day)
game_probables = [[game.p_pitcher_away, game.p_pitcher_home] for game in todays_games]
probables = [pitcher for game in game_probables for pitcher in game] 

with open(filename) as csvfile:
	reader = csv.reader(csvfile)
	for i, row in enumerate(reader):
		if i == 0:
			output_writer.writerow(row)
		else:
			if len(row[0].split(' ')) > 1:
				first_init_last = row[0].split(' ')[0][0] + '. ' + row[0].split(' ')[1]
				if first_init_last in probables:
					output_writer.writerow(row)
					print(first_init_last + ', K/9: ' + str(row[15]))
