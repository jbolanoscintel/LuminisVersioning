import sys
import requests
from bs4 import BeautifulSoup
from re import search

REGULAR_EXPRESSION = "[0-9]\.[1-9][0-9]*\.[0-3]\.[1-9][0-9]*"
URL = sys.argv[1]
CHANGE_TYPE = sys.argv[2]

def get_version(soup):
    result = ""
    for element in soup.select("td"):
        if search(REGULAR_EXPRESSION, element.text):
            result = element.text

    if result == "":
        raise ValueError('Current application Version not found')

    return result

def increment_version(value, change_type):
    splitted = value.split(".")
    if change_type.lower() == "minor":
        new_value = int(splitted[len(splitted) - 1]) + 1
        splitted[len(splitted) - 1] = str(new_value)
        return ".".join(splitted)
    elif change_type.lower() == "major":
        new_value = int(splitted[len(splitted) - 3]) + 1
        splitted[len(splitted) - 3] = str(new_value)
        splitted[len(splitted) - 1] = "1"
        return ".".join(splitted)

#VALIDATE IF THERE IS A MAXIMUM NUMBER
#MEETING WITH CARO AND ISA TO CHECK IF ALL NOTIFICATION ACTIONS ARE IN US

def luminis_auto_versioning(url, change_type):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    actual_version = get_version(soup)

    print('Previous version: ' + actual_version)

    new_version = increment_version(actual_version, change_type)

    return new_version

print('New version: ' + luminis_auto_versioning(URL, CHANGE_TYPE))

