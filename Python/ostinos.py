import requests
from lxml import etree
import csv
import pymarc
from pymarc import Record, Field


def getRecs(osti, data): # Passed osti and data into function instead of calling globally.
	for node in osti:
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
	data.writerow([title, author, date, sub, description, ostiId, doi, reportNumber, doeNumber, ostiUrl])

def getMarc(osti, marc):  # Passed osti and marc into function instead of calling globally.
	
	for node in osti:
		if node.tag == dc + 'ostiId':
			ostiNum = Field(tag = '086', indicators = [' ', ' '], subfields = ['a', node.text])
			continue
		if node.tag == dc + 'identifierReport':
			repId = Field(tag = '088', indicators = [' ', ' '], subfields = ['a', node.text])
			continue
		if node.tag == dc + 'title':
			title = Field(tag = '245', indicators = ['0', '0'], subfields=['a', node.text])
			continue
		if node.tag == dc + 'creator':
			creator = Field(tag = '700', indicators = ['1', ' '], subfields = ['a', node.text,])

	marc.add_field(ostiNum, repId, title, creator)


#-------------------------------------------------

f = open('ostinos.csv')
csv_f = csv.reader(f)

out = open ('osti_recs.csv', 'w')
data = csv.writer(out)
data.writerow(['Title', 'Author', 'Date', 'Subjects', 'Description', 'OstiID', 'DOI', 'Report Number', 'DOE Number', 'URL', ''])

marcOut = open('ostimarc.mrc', 'w')
#marc = Record()

dc = '{http://purl.org/dc/elements/1.1/}'
dcq = '{http://purl.org/dc/terms/}'


for number in csv_f:
	ostiId = number[0]
	marc = Record() # Create a new record for each loop.
	results = requests.get('http://www.osti.gov/scitech/scitechxml?Identifier=' + ostiId)
	tree = etree.fromstring(results.content)
	for node in tree.iter():
		if node.tag == dc + 'ostiId':
			if node.text == ostiId:
				o = node.getparent()
				osti = o.getchildren()
				getRecs(osti, data)
				getMarc(osti, marc)

	marcOut.write(marc.as_marc()) # Write each new record.
