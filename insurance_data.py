from bs4 import BeautifulSoup
import requests

response = requests.get("https://open.spotify.com/playlist/6nZJDrkwViKpyEbYfLtVz1")

soup = BeautifulSoup(response.text, "html.parser")

div_elements = soup.find_all("div")

for element in div_elements[21:]:
    print(element.text.strip())  
