import requests



URL = "https://iampeymankhalili.github.io/Html4BS/"
page = requests.get(URL)

print(page.text)


