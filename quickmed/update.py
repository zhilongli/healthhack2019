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

			elif (int(row['Id'])==int(incoming_number) and int(row['curr_node']) != -1):
				#print('here')
				addCopy = 0
				nodeNum = int(row['curr_node'])
				field = nodeDict[nodeNum]
				row[field] = incoming_body

				#print(type(incoming_body))

				if (incoming_body.lower().strip() == 'yes' or incoming_body.lower().strip() == 'true') and nodeNum !=1:
					print(incoming_body.lower().strip())
					print("true detected")

					response = True
				elif (incoming_body.lower().strip() == 'no' or incoming_body.lower().strip() == 'false') and nodeNum !=1:
					print(incoming_body.lower().strip())
					print("false detected")

					response = False

				elif nodeNum!=1:
					response = "invalid"
					return "Sorry, we don't understand your response! Please provide a response that's either \'yes\' or \'no\'"

				else:
					#print("invalid case detected")

					try:
						response = int(incoming_body)
					except:
						response = "invalid"
						# if nodeNum==1:
						return "Sorry, we don't understand your response! Please provide a response that is a whole number"
                        # else:
						# 	return "Sorry, we don't understand your response! Please provide a response that is a whole number:)"


				print(response)

				ret_value = decision_tree.next_qn(nodeNum, response)
				#print('next_qn\'s ret_value is' + str(ret_value) )
				if response!="invalid":
					row['curr_node'] = ret_value
				# if row['curr_node'] == "Invalid response received":
				# 	row['curr_node']=row['curr_node']
				if type(row['curr_node']) is str:
					row['curr_node'] = -1

				row['Time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

			row = {'Id': row['Id'], 'curr_node': row['curr_node'], 'Time': row['Time'], 'Age': row['Age'], 'Gender': row['Gender'], 'Zipcode': row['Zipcode'], 'cough_duration': row['cough_duration'], 'cough_type': row['cough_type'], 'resh': row['resh'], 'aches': row['aches'], 'chills': row['chills'], 'sore_throat': row['sore_throat'], 'chest_pain': row['chest_pain'], 'swelling': row['swelling'], 'wheezing': row['wheezing']}
			writer.writerow(row)

		#print(addCopy)

		if addCopy:
			row = {'Id': incoming_number, 'curr_node': 1, 'Time': strftime("%Y-%m-%d %H:%M:%S", gmtime()),
			'Zipcode': zipcode}
			writer.writerow(row)
			ret_value = 1

	shutil.move(tempfile.name, filename)
	return ret_value


def init():
	with open('database.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(['Id', 'Message'])

	f.close()
