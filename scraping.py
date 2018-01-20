# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:11:21 2018

@author: ( Jatin Bansal )
"""


# Amount of Reviews to extract
n=110

#Id of the movie
id="tt2582846"

url='http://www.imdb.com/title/'+id+'/reviews?ref_=tt_ov_rt'


from time import sleep
from selenium import webdriver
driver=webdriver.Chrome('E://chromedriver.exe')
driver.get(url)
button=driver.find_element_by_id('load-more-trigger')
req=(int)((n/25)+1)

for i in range(0,req):
    try:
        button.click()
    except Exception:
        i=i-1
        continue
    sleep(10)

import requests
from scrapy.selector import Selector
import urllib.parse
from urllib.parse import  urljoin

page=Selector(text=driver.page_source)
amt = page.xpath('//*[@class="header"]/span/text()').extract()[0]

title = page.xpath('//*[@class="title"]/text()').extract()
date  = page.xpath('//*[@class="review-date"]/text()').extract()
content  = page.xpath('//*[@class="content"]//*[@class="text"]').extract()
username=page.xpath('//*[@class="display-name-link"]/a/text()').extract()

final=[]
for i in range(0,n):
    temp=[]
    temp.append(i+1)
    temp.append(title[i])
    temp.append(username[i])
    s=content[i]
    s=s[18:-6]
    temp.append(s)
    temp.append(date[i])
    final.append(temp)

import csv
filename=id+'-'+amt+'-'+'file.csv'

myFile = open(filename, 'w',encoding='utf-8')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(final)
     
print("Writing complete")

