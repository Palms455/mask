import csv

def write_csv(data, file):
	with open(f'{file}.csv', 'a', encoding='utf-8') as file:
		writer = csv.DictWriter(file, fieldnames=['title', 'date', 'url'])
		writer.writerow(data)
	return
	