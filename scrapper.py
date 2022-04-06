from bs4 import BeautifulSoup
from requests import get
indeed_request = get('https://www.indeed.com/jobs?as_and=python&limit=50')

indeed_soup = BeautifulSoup(indeed_request.text, 'html.parser')

pagination = indeed_soup.find("ul", {"class": "pagination-list"})

li = pagination.find_all('li')
spans = []

for item in li:
    spans.append(item.span)
spans = spans[1:len(spans)-1]

print(spans)
