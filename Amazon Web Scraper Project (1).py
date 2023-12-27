#!/usr/bin/env python
# coding: utf-8

# In[6]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib


# In[66]:


# Connect to Website and pull in data

URL = 'https://www.amazon.ca/Sony-WH-1000XM5-Cancelling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_3_sspa?crid=36BVDXMSYA36T&keywords=headphones&qid=1701306979&sprefix=headpone%2Caps%2C106&sr=8-3-spons&ufe=app_do%3Aamzn1.fos.71722c10-739d-471b-befb-3e4b9bf7d0d6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(class_="a-price-whole").get_text()


print(title)
print(price)


# In[67]:


# Clean up the data a little bit

price = price.strip()
title = title.strip()

print(title)
print(price)


# In[68]:


# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[76]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\khush\Downloads\AmazonWebScraperDataset.csv')

print(df)


# In[84]:


#appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[89]:


#Combine all of the above code into one function


def check_price():
    URL = 'https://www.amazon.ca/Sony-WH-1000XM5-Cancelling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_3_sspa?crid=36BVDXMSYA36T&keywords=headphones&qid=1701306979&sprefix=headpone%2Caps%2C106&sr=8-3-spons&ufe=app_do%3Aamzn1.fos.71722c10-739d-471b-befb-3e4b9bf7d0d6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(class_="a-price-whole").get_text()
    
    price = price.strip()
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if price<350:
        send_mail()
    


# In[ ]:


# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\alexf\AmazonWebScraperDataset.csv')

print(df)


# In[91]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it 
#out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('khushijainlmh01@gmail.com', 'yourpassword')  # Replace with your password

    subject = "The headphones you want is below $350! Now is your chance to buy!"
    body = ("Khushi, This is the moment we have been waiting for. Don't mess it up! "
            "Link here: https://www.amazon.ca/link-to-product")

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'khushijainlmh01@gmail.com',
        'recipient@example.com',  # Replace with the recipient's email address
        msg
    )
    server.quit()

