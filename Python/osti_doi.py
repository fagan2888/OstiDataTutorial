import requests
import bs4
import csv
import pdb


#Open csv file to read from
f = open('osti_dois.csv')
csv_f = csv.reader(f)

#Open csv file to write to
output_file = open('ostidoi.csv', 'w') 
data = csv.writer(output_file)

for record in csv_f:
	ostiNumber = record[0]


	ostiSource = requests.get('http://www.osti.gov/scitech/biblio/' + ostiNumber)
	ostiSource.raise_for_status()
	ostiSourceSoup = bs4.BeautifulSoup(ostiSource.text, "lxml")
	ostiDOIObj = ostiSourceSoup.find(title="Document DOI URL")
	if ostiDOIObj is None: 
		continue
	ostiDOI = ostiDOIObj.contents[0]
	ostiDOI = str(ostiDOI)

	data.writerow([ostiNumber, ostiDOI])
		
output_file.close()
