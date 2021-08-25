from django.db import models
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=1024)
    coach = models.CharField(max_length=10)
    gm = models.CharField(max_length=10)
    web_url = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

def scrap(url):
    tfb = requests.get(url).text
    html_content = BeautifulSoup(tfb,'lxml')
    table = html_content.find('table',class_='toccolours')
    content = table.find_all('tr')
    head = content[3]
    body_rows = content[4:]
    headings = []
    for item in head.find_all('th'):
        temp = item.text.replace('年齡 – 生日\n','年齡')
        temp = temp.replace('#','背號')
        headings.append(temp)
    all_rows = []
    for row_num in range(len(body_rows)):
        row = []
        for row_item in body_rows[row_num].find_all('td'):
            row.append(row_item.text)
        temp = row[0]
        row[0] = temp[temp.find('!')+1:].strip()
        temp = row[1]
        row[1] = temp.strip()
        temp = row[2]
        row[2] = temp.strip()
        temp = row[3]
        temp = temp.replace('\xa0(I)','')
        temp = temp.replace('\xa0(C)\n','')
        temp = temp.replace('\xa0(FS)\n','')
        temp = temp.replace('\xa0(CP)','')
        row[3] = temp.strip()
        temp = row[4]
        index = temp.find('公')
        row[4] = temp[(index-4):(index)]
        temp = row[5]
        index = temp.find('公')
        index0 = temp.find('♠')
        row[5] = temp[(index0+1):(index)]
        temp = row[6]
        index = temp.find(' ')
        row[6] = temp[(index+1):(index+3)]
        all_rows.append(row)
    df = pd.DataFrame(data=all_rows,columns=headings)
    del df['']
    return df

def scrap2(url):
    pl = requests.get(url).text
    html_content = BeautifulSoup(pl,'lxml')
    table = html_content.find('table')
    content = table.find_all('tr')
    head = content[0]
    body_rows = content[1:]
    headings = []
    for item in head.find_all('th'):
        headings.append(item.text)
    all_rows = []
    for row_num in range(len(body_rows)):
        row = []
        for row_item in body_rows[row_num].find_all('td'):
            row.append(row_item.text)
        all_rows.append(row)
    names = []
    for row_num in range(len(body_rows)):
        row = []
        for name in body_rows[row_num].find_all('th'):
            names.append(name.text)
    headings[4] = '時間'
    headings[7] = '兩分命中率'
    headings[10] = '三分命中率'
    headings[13] = '罰球命中率'
    df = pd.DataFrame(data=all_rows,columns=headings[1:])
    df['姓名'] = names
    headings[0] = '姓名'
    df = df[headings]
    del df['球隊']
    del df['背號']
    return(df)

