# Basic Query

It's fairly simple to to use the OSTI XML service, as it's just a matter of constructing a URL in a browser. After the query returns all relevant metadata, you can then add a file type to that query (end of the URL) and download your data directly to your computer for further manipulation. 

Once you understand how to construct the URL, you may want to try out the Python section of this tutorial, where you can assign parts of the URL to variables and, potentially, incorporate this into your ILS or other automated workflows. 

##Sample search: 

Copy and paste the following link into a browser. You'll see a bunch of XML in your browser: this is the metadata for this particular set of OSTI reports. 

[http://www.osti.gov/scitech/scitechxml?Biblio=oak%20AND%20ridge&Identifier=AECD*&FullTextMatch=1&nrows=3000&page=0]

Breaking down how the URL is constructed: 

`osti.gov/scitech/scitechxml?`

This is the base URL. You'll always need this at the beginning of your query.  

`Biblio=`

This is your first *Criteria Keyword*, or search parameter. Here, you're telling OSTI's XML serivce that you'd like to query all of the available bibliographic record data (title, subjects, and so on). Alternatively, I could search for a specific `Author`, `Subject`, `Identifier`, `ResearchOrg`, range of `PubDates`, and so on. 

`oak%20AND%20ridge&`

Here I'm adding specific keywords to my `Biblio` query. Since you're constructing this in a browser, your keywords can't have spaces; thus, %20 needs to be present in lieu of an empty space. Their query service also supports Boolean searching (e.g. `oak AND ridge` becomes `oak%20AND%20ridge`, but I could just have easily written 'oak%20**OR**%20ridge). 

`Identifier=`

You aren't limited to selecting just one *Criteria Keyword*. You can chain together a query with as many *Criteria Keywords* as you like. In this case, I've added the `Identifier` *Criteria Keyword* to my query so that I can ask for records with a specific unique identifier.  

`AECD*&`

`FullTextMatch=1&`

`nrows=3000&page=0`