import bs4


with open("de-resources-fellows/bs4-codes/index3.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')

tags = soup.select('div.w3-panel > p')

for _tags in tags:
    print(_tags.text)