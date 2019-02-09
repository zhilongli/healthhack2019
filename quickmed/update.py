from tempfile import NamedTemporaryFile
import shutil
import csv

def write2db(incoming_body, incoming_number):
	filename = 'database.csv'
	tempfile = NamedTemporaryFile(mode='w', delete=False)

	fields = ['Id', 'Message']

	with open(filename, 'r') as csvfile, tempfile:
		reader = csv.DictReader(csvfile, fieldnames=fields)
		writer = csv.DictWriter(tempfile, fieldnames=fields)
		for row in reader:
			row = {'Id': row['Id'], 'Message': row['Message']}
			writer.writerow(row)

		row = {'Id': incoming_number, 'Message': incoming_body}
		writer.writerow(row)

	shutil.move(tempfile.name, filename)



def init():
	with open('database.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(['Id', 'Message'])

	f.close()
