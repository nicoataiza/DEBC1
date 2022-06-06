import bs4
import requests
from lxml import etree
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# putting back off so that we don't get 443'd

def load_api(url):
    """
    Uses requests to return page data
    """
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    page = session.get("GET", url)


url = "https://covid-19-statistics.p.rapidapi.com/regions"

headers = {
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com",
	"X-RapidAPI-Key": "ed4eea562emsh3867e25a5889325p110477jsn9c7650c0ecdb"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
if page.status_code == 200:
    soup = bs4.BeautifulSoup(page.content, 'lxml')
    print(soup.prettify())