#!/usr/bin/env python
# coding: utf-8

# # Website Scraping  

# In[2]:


from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
print(soup)


# In[3]:


soup.find_all('table')[1]


# In[4]:


soup.find('table', class_ = 'wikitable sortable')


# In[5]:


table = soup.find_all('table')[1]
print(table)


# In[6]:


world_titles = table.find_all('th')
world_titles


# In[7]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[8]:


import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

df


# In[9]:


# store data in a dataframe

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df


# In[15]:


# Export data to excel (.csv) file

df.to_csv(r'C:\Users\Acer\Desktop\Excel\scrapped data.csv',index=False)





# In[ ]:




