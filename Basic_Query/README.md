# Basic Query

It's fairly simple to to use the OSTI XML service, as it's just a matter of constructing a URL in a browser. After the query returns all relevant metadata, you can then add a file type to that query (end of the URL) and download your data directly to your computer for further manipulation. 

Once you understand how to construct the URL, you may want to try out the Python section of this tutorial, where you can assign parts of the URL to variables and, potentially, incorporate this into your ILS or other automated workflows. 

##Sample search: 

Copy and paste the following link into a new browser tab or window. You'll see a bunch of XML appear in your browser: this is the metadata for this particular set of OSTI reports, which you can use for creating new MARC records or updating current ones (more on that later). 

<http://www.osti.gov/scitech/scitechxml?Biblio=oak%20AND%20ridge&Identifier=AECD*&FullTextMatch=1&nrows=3000&page=0>

##What does that mean?

Breaking down how the URL is constructed: 

`osti.gov/scitech/scitechxml?`

This is the base URL. You'll always need this at the beginning of your query.  

`Biblio=`

This is your first *Criteria Keyword* (OSTI's term), or search parameter. Whenever I use *Criteria Keyword*, I'm talking about the controlled metadata fields that you're querying, **not** actual keywords (more on those momentarily). 
Here, you're telling OSTI's XML serivce that you'd like to query all of the available bibliographic record data (title, subjects, and so on). Alternatively, I could search for a specific `Author`, `Subject`, `Identifier`, `ResearchOrg`, range of `PubDates`, and so on. It's really up to you in terms of how general or specific you want to get. 

`oak%20AND%20ridge`

Now, I'm adding specific (actual) keywords to my `Biblio` query. Since you're constructing this in a browser, your keywords can't have spaces; thus, %20 needs to be present in lieu of an empty space. Their query service also supports Boolean searching (e.g. `oak AND ridge` becomes `oak%20AND%20ridge`, but I could just have easily written `oak%20**OR**%20ridge` as well as `oak%20**NOT**%20ridge`). 

`&`

This is an important little character. This is how you chain together all of your different search parameters. Every time you add a new *Criteria Keyword* or other parameter, this character needs to be present just prior to it. 

`Identifier=`

You aren't limited to selecting just one *Criteria Keyword*. You can chain together a query with as many *Criteria Keywords* as you like. In this case, I've added the `Identifier` *Criteria Keyword* to my query so that I can ask for records with a specific unique identifier.  

`AECD*`

I'm interested in all unique identifiers that start with AECD (e.g. AECD-123, AECD\123, AECD-CR-123, etc.). OSTI's XML service supports wildcards, hence the `*` after my query. 

`&FullTextMatch=1`

First, make note of the `&` at the beginning of this parameter. 

Here I've indicated that I'm only interested in full text items. 1 = yes, 0 = no. 

`&nrows=3000&page=0`

It's possible to place limits on the number of results returned. The maximum is 3000 per page (with an unlimited number of pages). 