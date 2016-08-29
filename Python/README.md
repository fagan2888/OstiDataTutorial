#Using Python

The scripts provided in this portion of the tutorial were created by a non-developer (me) as a means of quickly working with large datasets and remediating a significant number of MARC records. 

##What are these for?

These short Python scripts are simple examples of how you might use OSTI's XML service to either enhance current bibliographic records or create new records. 

`ostinos.py`, coupled with the short dataset `ostinos.csv`, is an example of how you might quickly work through a list of known OSTI numbers to derive additional or updated information about a group of reports. Some small changes to this code, however, would allow you to query according to institution (say, your laboratory), a list of author surnames, a range of publication dates, and so on. 

`osti_doi.py`, coupled with the much larger dataset `osti_dois.csv`, is an example of using a simple web scraper to grab the dois for a series of known OSTI numbers. 