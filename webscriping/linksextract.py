#Extract All Links from a Webpage
#Problem: Extract and print all links (<a> tags) from a webpage.

import requests
from bs4 import BeautifulSoup
#url of a news website(Example:BBC  News)
url = "https://cybersecuritynews.com/weekly-cybersecurity-update-jan-last-week/"
# send GET request to the URL
response = requests.get(url)
#print (response.text)
#check if the request was successful
if response.status_code == 200:
    print("Link fetched successfully!\n")
    #Parse the HTML content of the page using using Beautifulsoup
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    #find link (Example: find all <h3> tags with class "gs-c-promo-heading_title")
    links = soup.find_all("a")
    #print(link)
    #Diesplay the first 5 link
    print("All links from url:")
    for i, link in enumerate(links):
        href = link.get("href")
        if href:
            print(f"{i}. {href}")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")