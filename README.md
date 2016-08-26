# OstiDataTutorial
This is a tutorial for extracting metadata from OSTI's XML service, cleaning it, incorporating it into catalog records.

##Why have you created this?

OSTI does provide a [MARC record download service](https://www.osti.gov/home/marcrecords.html). However, this service isn't very granular--for example, it doesn't give you the option of only downloading technical report publications, or only records with links to full text documents. Since ORNL needed this granular searching capability, another means of acquiring that metadata was necessary. 

##Do I need to know XML to do this? 

Not necessarily. I've provided some sample code for parsing XML with Python, but also will provide an alternative means of gathering and manipulating the data by searching the XML service either using Python or directly, and then downloading and manipulating a csv file. 

##What do I need to know?

A portion of this tutorial expects you to have Python 2.7 on your computer, and a very rudimentary understanding of the command line (examples will be provided). However, the tutorial will begin with a basic explanation of the XML service, how to query it directly, and how to download a csv file (i.e. spreadsheet).


