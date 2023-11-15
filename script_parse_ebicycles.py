BASE_URL: str = "https://ebicycle-db.com/"
URL: str = "https://ebicycle-db.com/category/transport/electric-bicycle/"

from parse_html import extract_parsed_html_content
from bs4 import BeautifulSoup


html_content = extract_parsed_html_content(url=URL)

soup = BeautifulSoup(html_content, features="html.parser")
div_tags = soup.findAll(name='div', attrs={'class': 'container-fluid'})

if div_tags[0]:
    for a_tag in div_tags[0].findAll('a'):
        manufacturer_name, href = a_tag.find('img')['alt'], a_tag['href']
        webpage_url = BASE_URL + href
        print(manufacturer_name, webpage_url)

