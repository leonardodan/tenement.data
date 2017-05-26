#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'http://bj.xiaozhu.com/fangzi/9219942264.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,"lxml")
titles = soup.select('#page_list > ul > li:nth-child(1) > div.result_btm_con.lodgeunitname > div.result_intro > a > span')
print(titles)
