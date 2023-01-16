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

#Find tags: return some of Html tags
# <header> , <section> <footer> <ul> <a> <img> - step6

# This section finds the paragraphs in the HTML
paragraphs = soup.find_all("p")
print(paragraphs)

# This section finds the header in the HTML
headers = soup.find_all("header")
print(headers)

# This section finds the sections in the HTML
sections = soup.find_all("section")
print(sections)

# This section finds the lists in the HTML
uls = soup.find_all("ul")
print(uls)

# This section finds the links in the HTML
links = soup.find_all("a")
print(a)

# This section finds the images in the HTML
imgs = soup.find_all("img")
print(imgs)


#step6


#Find a complete text using a part of that text - step7

text = soup.find_all(
    "p", string=lambda text: "this book"
)
print(text)

#step7

