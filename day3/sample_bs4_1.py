import bs4


with open("de-resources-fellows/bs4-codes/index2.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
tags = soup.find_all('h5')

for _tags in tags:
    print(_tags)

