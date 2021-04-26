"""
Scrape Amazon website to get the details price, Author, weight for list of
book names listed in a text file
Input : Book Name
Output : Name as per Amazon, Author, Price and weight
"""

# Import required Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen

#Headers
headers = {
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }    

def Amazon_books_data(asin_Num,each_book):
    try:
    
        #Target URL to scrap
        url = r"https://www.amazon.in/dp/"+asin_Num    
        
        #Send request to download data
        response = requests.request("GET", url,  headers=headers)

        #Parse the downloaded data
        data = BeautifulSoup(response.text, 'html.parser')    

        #Get Book Name
        Name = data.find_all('span',attrs = {'id': 'productTitle'})    

        #Get Author
        Author = data.find_all('a',attrs = {'class':"a-link-normal contributorNameID"})    
        
        # Get the price
        price = data.find_all('span', attrs = {'class':'a-size-base a-color-price a-color-price'})
        
        #Get the weight
        weight = data.find_all('span', attrs = {'class':'a-list-item'})
        for each in weight:
            if ('Item Weight' in each.get_text()):
                return Name[0].text.strip().lstrip(), Author[0].text.strip().lstrip(), price[0].text.strip().lstrip(),each.get_text().split(":")[-1].strip().lstrip()
    except Exception as e:
        return("Book data Not found",e)
    

def get_amazon_link(book_title):
  url = r'https://www.amazon.in/s?k='+book_title
  print(url)
  
  #Send request to download data
  response = requests.request("GET", url,  headers=headers)

  #Parse the downloaded data
  data = BeautifulSoup(response.text, 'html.parser')  

  book_Url = data.find_all('a', attrs = {'class':'a-link-normal a-text-normal'})
  print(book_Url)

  return r'https://www.amazon.in/'+str(book_Url[0].get('href'))

def get_amazon_asin (url):
    url = url
    #Send request to download data
    response = requests.request("GET", url,  headers=headers)

    #Parse the downloaded data
    data = BeautifulSoup(response.text, 'html.parser')

    asin = data.find_all('span', attrs = {'class':'a-list-item'})
    for each in asin:
        if ('ASIN' in each.get_text()):
            return each.get_text().split(":")[-1].strip().lstrip()
        elif 'ISBN-10' in each.get_text():
            return each.get_text().split(":")[-1].strip().lstrip()

if __name__ == "__main__":
    Books = []
    Amazon_Data = {}
    book_list_file = open ('D:\Python_Scripts\web_Scraper\list_Of_Books.txt')
    Lines = book_list_file.readlines()
    for each_book in Lines:
        Books.append(each_book.split('\n')[0])    

    for each_book in Books:
        bookName = each_book.replace(' ','+')
        bookUrl = get_amazon_link(bookName)
        scraped_data = Amazon_books_data(get_amazon_asin(bookUrl),bookName)    
        if scraped_data[0]!=("Book data Not found"):
            Amazon_Data[each_book]={}
            Amazon_Data[each_book]['Title'] = scraped_data[0]
            Amazon_Data[each_book]['Author'] = scraped_data[1]
            Amazon_Data[each_book]['Price'] = scraped_data[2]
            Amazon_Data[each_book]['Weight'] = scraped_data[3]
        elif scraped_data[0]==("Book data Not found"):
            Amazon_Data[each_book] = "Book data Not found"
    output_file = open(r'D:\Python_Scripts\web_Scraper\output_file.txt','w')
    for book in Amazon_Data:
        output_file.write(book+"\n")
        for attribute in Amazon_Data[book]:
            output_file.write(attribute+":"+Amazon_Data[book][attribute]+"\n")
        output_file.write("-----------------------------------------------+")
    output_file.close()
