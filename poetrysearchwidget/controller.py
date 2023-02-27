"""controller will manage making API calls to the PoetryDB and format 
the results for display."""

# import statements
import requests

# set some variables to help our API call
domain = "https://poetrydb.org/"
endpoint = ""

# Make an API call
def make_call(query: str) -> str:
    """take the results (of the search) and use it to make an API call
    then return formatted reults or error if it does not return a 200 code"""

    # create our url
    url = domain + endpoint + query

    # make the call
    response = requests.get(url)
    print()

# get the top results

# format results