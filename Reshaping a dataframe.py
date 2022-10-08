#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Pandas
import pandas as pd

# Read the excel file in the current directory.
movies = pd.read_excel('movies_merge.xlsx')

# Read the csv file in the currect directory.
ott = pd.read_csv('ott_merge.csv')

# View the DataFrame
print(movies.columns)
print(movies.shape)
print(ott.columns)
print(ott.shape)


# In[2]:


# Merge the two DataFrame
mov_ott = pd.merge(movies, ott, how='left', on='ID')

# View the DataFrame
print(mov_ott.columns)
print(mov_ott.shape)


# In[4]:


# View DataFrame
mov_ott


# In[5]:


#1. Determine the film released date and content rating.
movies.pivot(index='Title', columns='Age',
            values='Year')


# In[10]:


#2. Determine the title of movie, the directors, the genres by content rating
movies.pivot(index='Title', columns='Age',
             values=['Directors','Genres'])


# In[11]:


#3. Determine the title of the movies, the released year,and 
# the language by content rating.
movies.pivot(index='Title', columns='Age', 
            values=['Year','Language'])


# In[13]:


#4. Determine the Netflix screened movies based on language, runtime and country.
mov_ott.pivot(index='Title', columns='Netflix',
             values=['Language', 'Runtime', 'Country'])


# In[14]:


#5. Determine the title of the movies, specified language, potential runtime
# and genres by content rating.
mov_ott.pivot(index='Title', columns='Age',
             values=['Language','Runtime','Genres'])


# In[ ]:




