import requests
from bs4 import BeautifulSoup



URL = "https://iampeymankhalili.github.io/Html4BS/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="content-section")

print(results.prettify())
print(page.text)


