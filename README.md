# OstiDataTutorial
This is a tutorial for extracting metadata from OSTI's XML service, cleaning it, incorporating it into catalog records.

##Why have you created this?

OSTI does provide a [MARC record download service](https://www.osti.gov/home/marcrecords.html). However, with this service (at the time of this writing) it's not possible to search for specific MARC records or sets of records. Since ORNL only wanted to pull data specific to ORNL technical reports, another means of acquiring that metadata was necessary. 

##Do I need to know XML to do this? 

Not necessarily. I've provided some sample code for parsing XML with Python, but also will provide an alternative means of gathering and manipulating the data by searching the XML service either using Python or directly, and then downloading and manipulating a csv file. 

##What do I need to know?

This tutorial expects you to have Python 2.7 on your computer, and a very rudimentary understanding of the command line (examples will be provided). 


