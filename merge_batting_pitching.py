from __future__ import print_function

import mlbgame
import datetime
import csv
import ipdb

today = datetime.datetime.utcnow()
month = today.month
day = today.day
year = today.year

batting_directory = 'steamer_ros/' + str(month) + str(day-1) + str(year) + '/'
pitching_directory = 'steamer_ros/' + str(month) + str(day) + str(year) + '/'
batting_filename = batting_directory + 'steamer_ros_batting_updated_hits_' + str(month) + str(day-1) + str(year) + '.csv'
probables_filename = pitching_directory + 'steamer_ros_pitching_probables_' + str(month) + str(day) + str(year) + '.csv'
output_filename = batting_directory + 'steamer_ros_merged_' + str(month) + str(day) + str(year) + '.csv'
output_file = open(output_filename, 'wb')
output_writer = csv.writer(output_file)

probable_pitcher_stats = {}

with open(probables_filename) as probables_csv:
	reader = csv.reader(probables_csv)
	for i, row in enumerate(reader):
		if i == 0:
			probable_pitcher_stats['headers'] = row
		else:
			probable_pitcher_stats[row[1]] = row

with open(batting_filename) as batting_csv:
	reader = csv.reader(batting_csv)
	for i, row in enumerate(reader):
		if i == 0:
			headers = row + probable_pitcher_stats['headers']
			output_writer.writerow(headers)
		else:
			pitcher_id = '_'.join(row[-3].split(' '))
			team = row[-2]
			if probable_pitcher_stats.get(team):
				next_row = row + probable_pitcher_stats[team]
				output_writer.writerow(next_row)




