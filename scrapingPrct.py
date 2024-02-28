from bs4 import BeautifulSoup
import requests

page_To_Scrape = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(page_To_Scrape.text, "html.parser")

quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

for quote in quotes:
    print(quote.text)
for author in authors:
    print(author.text)


# OR we can do this

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)

