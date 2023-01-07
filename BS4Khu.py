import requests
from bs4 import BeautifulSoup

# add URL and Get data from Website - step1
URL = "https://iampeymankhalili.github.io/Html4BS/"
page = requests.get(URL)
print(page.text)
# step1

# make a object from BeautifulSoup - step2
soup = BeautifulSoup(page.content, "html.parser")
# step2

# Find data with a specific ID - step3
result_id = soup.find(id="content-section")
print(result_id.prettify())
# step3

# Find data with a specific Class name - step4
result_classes = soup.find_all("div", class_="col-12 col-md-auto")
for result_class in result_classes:
    print(result_class, end="\n"*2)
# step4

#Find text of each class - step5
for result_class in result_classes:
    temp = result_class.find("a")
    print(temp.text)
#step5

#For example: return all paragraphs - step6
paragraphs = soup.find_all("p")

print(paragraphs)

#step7

#img - step7
img = soup.find_all("img")
print(img)

