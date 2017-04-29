# Author's name:            Lukas Mohs
# Creation Date:            04/20/17
# Last Modification Date:   04/20/17
# Brief Description:
# This small application presents some functionality of the requests,
# the nltk and BeautifulSoup libraries: First, a webpage is requested
# and the returned answer stored. Then, the content in form of a plain String
# of HTML is printed. This String is interpreetd by BeautifulSoup and printed
# in a formatted way. The find_all() method of BeautifulSoup is then used to
# get all HTML tags from the page, which are printed afterwards.
# Then, all tags are filtered for anchor tags and their content is added to the
# linkList, which is printed afterwards. Another loop iterates again
# over all tags and uses a regular expression to expract just the link of all
# anchor tags, which are printed to the screen, too.
# Finally, the NLTK word_tokenize() method is used to print all tokens within
# the HTML String.

import nltk
from nltk import word_tokenize
import requests
from bs4 import BeautifulSoup
import re

def main():
    # Scraoe the webpage http://www.bigrigg.net and save it in page
    page = requests.get('https://github.com/lukasmohs')

    # Print the page content
    print(page.content)

    # Create a BeautifulSoup object out of the page content 
    soup = BeautifulSoup(page.content, 'html.parser')

    # Print it in a formatted way
    print(soup.prettify())

    # find all HTML tags within the content and print them
    tagSet = set()
    tags = soup.find_all()
    for tag in tags:
        tagSet.add(tag.name)

    print(tagSet)
    # Find all the anchor HTML tags within all tags 
    # and append it to the seperate linkList.
    linkList = []
    for tag in tags:
        if str(tag).startswith("<a") and str(tag).endswith("</a>"):
            linkList.append(str(tag))

    # Print the linkList
    print(linkList)

    # Iterate over all links again and just display the plain URL
    # by applying a regular expression and finally print the result
    count = 1
    for link in linkList:
        print(str(count) + ": " + re.findall(r'(?<=href=").*?(?=")', str(link))[0])
        count = count +1 

    # Get tokens out of page content
    plain = soup.get_text()
    tokens = word_tokenize(plain)
    print(tokens)

# Call main() method
main()
