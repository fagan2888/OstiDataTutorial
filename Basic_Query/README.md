# Basic Query

It's fairly simple to to use the OSTI XML service, as it's just a matter of constructing the URL in a browser. Once you have the data you need, you can add a file type to that query and download your data directly to your computer for further manipulation. 

Once you understand the construction of the URL, you have the option of trying out the Python section of this tutorial, where you can assign parts of the URL to variables. 

Sample search: 

http://www.osti.gov/scitech/scitechxml?Biblio=oak%20AND%20ridge&Identifier=AECD*&FullTextMatch=1&nrows=3000&page=0

Copy and paste the above link into a browser. You'll see a bunch of XML in your browser: this is the metadata for this particular set of OSTI reports. 

Breaking down how the URL is constructed: 

*http://www.osti.gov/scitech/scitechxml?*

This is the base URL. You'll always need this, no matter what your query is.  

*Biblio=*

*oak%20AND%20ridge&*

Identifier=AECD*&

FullTextMatch=1&

nrows=3000&page=0