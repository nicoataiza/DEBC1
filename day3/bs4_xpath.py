import bs4
from lxml import etree


with open("de-resources-fellows/bs4-codes/index3.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
dom = etree.HTML(str(soup))

tags = dom.xpath('//div[@class="w3-panel"]//p')


for _tags in tags:
    print(_tags)