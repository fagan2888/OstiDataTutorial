import requests
from lxml import etree
import csv
import pymarc
from pymarc import Record, Field


def getRecs(osti, data):
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
			continue
	data.writerow([title, author, date, sub, description, ostiId, doi, reportNumber, doeNumber, ostiUrl])

def getMarc(osti, marc):
	
	for node in osti:
		
		if node.tag == dc + 'doi':
			doi = node.text or 'blank'
			doiId = Field(tag = '024', indicators = ['7', ' '], subfields = ['a', doi, '2', 'doi'])
			continue
		if node.tag == dc + 'ostiId':
			ostiNum = Field(tag = '086', indicators = [' ', ' '], subfields = ['a', node.text])
			continue
		if node.tag == dc + 'identifierReport':
			repId = Field(tag = '088', indicators = [' ', ' '], subfields = ['a', node.text])
			continue
		if node.tag == dc + 'title':
			title = Field(tag = '245', indicators = ['0', '0'], subfields=['a', node.text])
			continue
		if node.tag == dc + 'date':
			dat = node.text or 'blank'
			date = Field(tag = '260', indicators = [' ', ' '], subfields = ['c', dat])
			continue
		if node.tag == dc + 'format':
			pag = node.text or 'blank'
			pages = Field(tag = '300', indicators = [' ', ' '], subfields = ['a', pag])
			continue
		if node.tag == dc + 'description':
			des = node.text or 'blank'
			description = Field(tag = '520', indicators = [' ', ' '], subfields = ['a', des])
			continue
		if node.tag == dcq + 'identifierDOEcontract':
			doe = node.text or 'blank'
			doeId = Field(tag = '536', indicators = [' ', ' '], subfields = ['b', doe,])
			continue
		if node.tag == dc + 'subject':
			sub = node.text or 'blank'
			subject = Field(tag = '650', indicators = [' ', '0'], subfields = ['a', sub])
			continue
		if node.tag == dc + 'creator':
			auth = node.text or 'blank'
			creator = Field(tag = '700', indicators = ['1', ' '], subfields = ['a', auth])
			continue
		if node.tag == dcq + 'publisherResearch':
			pub = node.text or 'blank'
			publisher = Field(tag = '710', indicators = ['2', ' '], subfields = ['a', pub])
			continue
		if node.tag == dcq + 'identifier-purl':
			url = node.text or 'blank'
			reportUrl = Field(tag = '856', indicators = ['4', '0'], subfields = ['u', url])
			
	marc.add_ordered_field(doiId, ostiNum, repId, title, date, pages, description, doeId, subject, creator, publisher, reportUrl)		
#-------------------------------------------------

f = open('ostinos2.csv')
csv_f = csv.reader(f)

out = open ('osti_recs2.csv', 'w')
data = csv.writer(out)
data.writerow(['Title', 'Author', 'Date', 'Subjects', 'Description', 'OstiID', 'DOI', 'Report Number', 'DOE Number', 'URL', ''])

marcOut = open('ostimarc.mrc', 'a')

dc = '{http://purl.org/dc/elements/1.1/}'
dcq = '{http://purl.org/dc/terms/}'


for number in csv_f:
	ostiId = number[0]
	marc = Record()
	results = requests.get('http://www.osti.gov/scitech/scitechxml?Identifier="' + ostiId + '"')
	tree = etree.fromstring(results.content)
	for node in tree.iter():
		if node.tag == dc + 'identifierReport':
			#if node.text == ostiId:
			o = node.getparent()
			osti = o.getchildren()
			getRecs(osti, data)
			getMarc(osti, marc)

	
	marcOut.write(marc.as_marc())