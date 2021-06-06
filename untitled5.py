# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 21:30:06 2021

@author: 13138
"""
from AQI_plot import avg_data_year
import requests
import sys
from bs4 import  BeautifulSoup
import os
import csvfile_html = open('Data/Html_Data/{}/{}.html'.format(2015,1), 'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)

#def met_data(month, year):
    
    