import requests

URL = "http://luminis-dev.intel.com/installer/publish.htm"
page = requests.get(URL)

print(page.text)