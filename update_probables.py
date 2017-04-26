import mlbgame
import datetime
import csv
import ipdb

today = datetime.datetime.utcnow()
month = today.month
day = today.day
year = today.year


filename = 'steamer_ros/' + str(month) + str(day) + str(year) + '/' + 'steamer_ros_pitching_' + str(month) + str(day) + str(year) + '.csv'

todays_games = mlbgame.day(year, month, day)
game_probables = [[game.p_pitcher_away, game.p_pitcher_home] for game in todays_games]
probables = [pitcher for game in game_probables for pitcher in game] 

with open(filename) as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		if len(row[0].split(' ')) > 1:
			first_init_last = row[0].split(' ')[0][0] + '. ' + row[0].split(' ')[1]
			if first_init_last in probables:
				print(first_init_last + ', K/9: ' + str(row[15]))
