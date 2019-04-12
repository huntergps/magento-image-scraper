# Import libraries
import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup


def get_product_url_list():
    productlist = []
    # Set URL for sitemap to parse
    sitemap = 'https://www.MYDOMAIN.com/sitemap'
    # Connect to the SITEMAP
    response = requests.get(sitemap)
    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    # Loop through soupsitemap object finding 'li.a' with class 'product'
    for link in soup.find_all('li', class_="product"):
        producturl = (link.a.get('href'))
        if producturl not in productlist:
            productlist.append(producturl)
    return productlist


def get_product_name():  # removes the https://www.MYDOMAIN.com/ part
    productname = []
    for product in get_product_url_list():
    # Change '27' to the character length of the URL from https through to the .com/ (include final slash) 
    # This could calculated of course but I was using this as a one off so no need.
        productname.append(product[27:]) 
    return productname


def create_product_dirs(productname):
    directory = f"./images/{productname}"
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_product_images(urlproductname):
    # Set the URL you want to webscrape from
    url = f"https://www.MYDOMAIN.com/{urlproductname}"
    response = requests.get(url)  # Connect to the URL
    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    count = 0
    # Loop through soup object finding 'a' links with class 'lightbox' -  check what class is assigned to gallery images in your theme
    for link in soup.find_all('a', class_="lightbox"):
        imgurl = (link.get('href'))
        count += 1
        imgname = f"./images/{urlproductname}/{urlproductname}-{count}.jpg"
        urllib.request.urlretrieve(imgurl, imgname)
        # time.sleep(1)  # uncomment this to pause the code for a second if you have issues with your host blocking you due to the scraping


def main():
    for product in get_product_name():
        create_product_dirs(product)
        get_product_images(product)


main()
