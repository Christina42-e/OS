#webscriping
import requests
from bs4 import BeautifulSoup
url = "https://www.bbc.com/news"

#send GET request to the URL
response = requests.get(url)
#print(response.text)
#check if the request was successful
if response.status_code == 200:
    print("Page fetched successfully!\n")
    #parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    #find headlines (Example: Find all <h3> tags with class 'gs-c-promo-heading__title')
    headlines = soup.find_all('h2', class_='sc-8ea7699c-3')
    #print(headlines)
    #display the first 5 headlines
    print("Top 5 Headlines:")
    for i, headline in enumerate(headlines[:5]):
        print(f"{i+1}. {headline.get_text()}")
else:
    prnit(f"failed to retrieve data. Status Code: {response.status_code}")