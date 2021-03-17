#!/usr/bin/env python
# coding: utf-8

# In[9]:


import urllib.request
import datetime

xls_path = "https://www.cba.am/Storage/AM/downloads/gorc/YC.xlsx"

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)
    file = open('C:/Users/ASUS/Downloads/YC' + filename + '.xlsx', 'wb')
    file.write(response.read())
    file.close()


# In[10]:


import datetime as date
filename1 = str(datetime.datetime.strftime(datetime.datetime.strptime(str(date.date.today()),'%Y-%m-%d').date(), "%Y%m%d"))


# In[11]:


download_file(xls_path, filename1)

