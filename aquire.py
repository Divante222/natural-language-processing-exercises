import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

import os
from pprint import pprint 

def get_news_articles():
    headers = {"User-Agent": "Chrome/91.0.4472.124"}
    url_list = []
    begins_with = 'https://inshorts.com/'
    url = 'https://inshorts.com/en/read'
    response = get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')

 
    the_dict = {}
    for i in soup.find_all('ul', class_ = 'category-list')[0].find_all('a'):
        if i.text in [' Business ', ' Sports ',' Technology ', ' Entertainment ']:

            'news-card-title news-right-box'

            response2 = get(begins_with + i['href'][1:], headers = headers)
            soup2 = BeautifulSoup(response2.content, 'html.parser')
            value_list = []
            key_list = []

            for j in soup2.find_all('div', class_ = 'card-stack')[0].find_all('div', class_ = 'news-card-content'):
                value_list.append(j.text.splitlines()[1])
   

            for j in soup2.find_all('div', class_ = 'card-stack')[0].find_all('div', class_ = 'news-card-title news-right-box'):
                
                key_list.append(j.text.splitlines()[2])

            for k in range(len(key_list)):

                the_dict[key_list[k]] = value_list[k]
        
        if i.text ==  ' Business ':   
            the_df1 = pd.DataFrame(key_list, columns = ['title'])
            the_df2 = pd.DataFrame(value_list, columns = ['content'])

            business_df = pd.concat([the_df1, the_df2], axis=1)
            business_df['catagory'] = 'Business'
            

        if i.text ==  ' Sports ':   
            the_df1 = pd.DataFrame(key_list, columns = ['title'])
            the_df2 = pd.DataFrame(value_list, columns = ['content'])

            sports_df = pd.concat([the_df1, the_df2], axis=1)
            sports_df['catagory'] = 'Sports'


        if i.text ==  ' Technology ':   
            the_df1 = pd.DataFrame(key_list, columns = ['title'])
            the_df2 = pd.DataFrame(value_list, columns = ['content'])

            tech_df = pd.concat([the_df1, the_df2], axis=1)
            tech_df['catagory'] = 'Technology'
            


        if i.text ==  ' Entertainment ':   
            the_df1 = pd.DataFrame(key_list, columns = ['title'])
            the_df2 = pd.DataFrame(value_list, columns = ['content'])

            ent_df = pd.concat([the_df1, the_df2], axis=1)
            ent_df['catagory'] = 'Entertainment'
     
    return pd.concat([ent_df, tech_df, sports_df, business_df])


def codeup_blog_posts():

    headers = {"User-Agent": "Chrome/91.0.4472.124"}
    url = 'https://codeup.com/blog/'
    response = get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    article_links = soup.find_all('h2', class_="entry-title")
    value_list = []
    the_dict = {}
    title_list = []
    for i in range(len(article_links)):
        list_to_append = []
        url = article_links[i].find_all('a')[0]['href']
        response = get(url, headers = headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        response = get(url, headers = headers)
        key = soup.find_all('h1')[0].text
        title_list.append(key)
        value = soup.find_all('div', class_ = 'entry-content')[0].find_all('p')
        titles_list = []
        for j in value:

            list_to_append.append(j.text)
            
        
        
        value_list.append(str(list_to_append))    
        the_dict[key] = value_list
        
    the_df = pd.concat([pd.DataFrame(value_list, columns = ['content']),pd.DataFrame(title_list, columns = ['title'])], axis = 1)
    
    return the_df