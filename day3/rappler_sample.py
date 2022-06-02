import bs4
import requests
from lxml import etree
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

URL = "http://www.rappler.com/topic/covid-19/"
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

page = session.get(URL)



if page.status_code == 200:
    soup = bs4.BeautifulSoup(page.content, 'lxml')
    print(soup.prettify())