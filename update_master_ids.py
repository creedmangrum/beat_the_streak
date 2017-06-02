import csv
import requests
import ipdb
import StringIO

output_filename = 'master.csv'
output_file = open(output_filename, 'wb')
output_writer = csv.writer(output_file)

updated_master_request = requests.get('http://crunchtimebaseball.com/master.csv')
updated_master_csv = updated_master_request.text.encode('utf-8')
master_array = updated_master_csv.split('\r\n')
reader = csv.reader(master_array, delimiter=',')
for i, row in enumerate(reader):
	output_writer.writerow(row)
