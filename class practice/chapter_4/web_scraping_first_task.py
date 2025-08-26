''''
What implications does this structure have for scraping the content? 
You probably don't know much about web scraping yet, so don't think 
too much about the technical implications. But what impact could that have conceptually?

Do you think you can scrape everything in one go?

What programming logic that you've learned might come in handy for this process?

Get out your notebook and write down some thoughts and ideas on how you could approach scraping this page structure.

'''

# 1) I guess because everything is built on separate containers,
#    there should be a kind of -for- that iterates over each container
# 2) No, defenitly not.
# 3) I guess iteration should be a very handy tool with some string search,
#    and also functions like request, json, and tools to save data in a file.text/json
# 4) Thinking of the 3 big steps for a web scrapping:
#       - Inspect: I would use request module.
#       - Scrap: I would save the data into a json file.
#       - Parse: I would analyze that file as I analyze lists or dictionaries.