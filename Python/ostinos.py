import requests
from xml.etree import ElementTree
import csv

f = open('ostinos.csv')
csv_f = csv.reader(f)

out = open('osti_recs.csv', 'w')
data = csv.writer(out)
data.writerow(['Title', 'Author', 'Date', 'Subjects', 'Description', 'OstiID', 'DOI', 'Report Number', 'DOE Number', 'URL', ''])

dc = '{http://purl.org/dc/elements/1.1/}'
dcq = '{http://purl.org/dc/terms/}'

for number in csv_f:
	ostiId = number[0]
	
	results = requests.get('http://www.osti.gov/scitech/scitechxml?Identifier=' + ostiId)
	tree = ElementTree.fromstring(results.content)
	
	for node in tree.iter():
		if node.tag == dc + 'title':
			title = node.text
			continue
		if node.tag == dc + 'creator':
			author = node.text
			continue
		if node.tag == dc + 'subject':
			sub = node.text
			continue
		if node.tag == dc + 'description':
			description = node.text
			continue
		if node.tag == dc + 'ostiId':
			ostiId = node.text
			continue
		if node.tag == dc + 'doi':
			doi = node.text
			continue
		if node.tag == dc + 'identifierReport':
			reportNumber = node.text
			continue
		if node.tag == dc + 'date':
			date = node.text
			continue
		if node.tag == dcq + 'identifierDOEcontract':
			doeNumber = node.text
			continue
		if node.tag == dcq + 'identifier-citation':
			ostiUrl = node.text
			continue
	data.writerow([title, author, date, sub, description, ostiId, doi, reportNumber, doeNumber, ostiUrl])

out.close()
	