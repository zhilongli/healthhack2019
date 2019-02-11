from tempfile import NamedTemporaryFile
from time import gmtime, strftime
import shutil
import csv
import decision_tree

nodeDict={1: 'cough_duration', 2: 'cough_type', 3: 'wheezing', 4: 'rash', 5: 'sore_throat', 6: 'aches', 7: 'chills', 8: 'appetite', 9: 'sore_throat', 10: 'chest_pain', 11: 'swelling'}

def write2db(incoming_body, incoming_number, zipcode):
	filename = 'database.csv'
	tempfile = NamedTemporaryFile(mode='w', delete=False)

	fields = ['Id', 'curr_node', 'Time', 'Age', 'Gender', 'Zipcode', 'cough_duration', 
	'cough_type', 'resh', 'aches', 'chills', 
	'sore_throat', 'chest_pain', 'swelling', 'wheezing']

	addCopy = 1
	firstLine = 1

	with open(filename, 'r') as csvfile, tempfile:
		reader = csv.DictReader(csvfile, fieldnames=fields)
		writer = csv.DictWriter(tempfile, fieldnames=fields)

		for row in reader:

			if (firstLine): 
				firstLine = 0

			elif (int(row['Id'])==incoming_number and int(row['curr_node']) != -1):
				addCopy = 0
				nodeNum = int(row['curr_node'])
				field = nodeDict[nodeNum]
				row[field] = incoming_body
				row['curr_node'] = decision_tree.next_qn(nodeNum, incoming_body)
				if type(row['curr_node']) is str:
					row['curr_node']=-1
					
				row['Time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

			row = {'Id': row['Id'], 'curr_node': row['curr_node'], 'Time': row['Time'], 'Age': row['Age'], 'Gender': row['Gender'], 'Zipcode': row['Zipcode'], 'cough_duration': row['cough_duration'], 'cough_type': row['cough_type'], 'resh': row['resh'], 'aches': row['aches'], 'chills': row['chills'], 'sore_throat': row['sore_throat'], 'chest_pain': row['chest_pain'], 'swelling': row['swelling'], 'wheezing': row['wheezing']}
			writer.writerow(row)

		#print(addCopy)

		if addCopy:
			row = {'Id': incoming_number, 'curr_node': 1, 'Time': strftime("%Y-%m-%d %H:%M:%S", gmtime()), 
			'Zipcode': zipcode}
			writer.writerow(row)

	shutil.move(tempfile.name, filename)


def init():
	with open('database.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(['Id', 'Message'])

	f.close()
