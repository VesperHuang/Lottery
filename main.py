# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import common as com

#大樂透資料字典
biglottery = {"volume":"","date":"","no1":0,"no2":0,"no3":0,"no4":0,"no5":0,"no6":0,"special":0}

#資料來源網址
url='http://www.taiwanlottery.com.tw'
html = requests.get(url)

sp = BeautifulSoup(html.text,'html.parser')
data1 = sp.select("#rightdown")
#print(data1)

# 20180701 改取大樂透號碼
#data2 = data1[0].find('div',{'class':'contents_box02'})
collect_box02 = sp.select('.contents_box02')
data2 = collect_box02[2]
#print(data2)

#取得第幾期 及 開獎日期
temp = data2.find_all('span',{'class':'font_black15'})
temp_text = temp[0].text
start = temp_text.find("第")
end = temp_text.find("期")
#期號
biglottery["volume"]=temp_text[start+1:end]
#開獎日期
biglottery["date"] = com.FormatDate(temp_text[0:8])

#取得大樂透號碼
data3 = data2.find_all('div',{'class':'ball_tx'})
#print(data3)

# =============================================================================
# print("開出順序：",end="")
# for n in range(0,6):
#     print(data3[n].text,end="  ")
# =============================================================================

#print("\n大小順序：",end="  ")
for n in range(6,len(data3)):
    biglottery["no" + str(n-5)] = data3[n].text
#    print(data3[n].text,end="  ")

red = data2.find('div',{'class':'ball_red'})
biglottery["special"] = format(red.text)
#print("\n第二區：{}".format(red.text))
#print(biglottery)

#將資料寫入 sqllite 中
sql = ""
sql = "insert into Big_Lottery(volume,date,no1,no2,no3,no4,no5,no6,special) "
sql +="select "
sql +="\"" + biglottery["volume"] +"\","
sql +="\"" + biglottery["date"] +"\","
sql += biglottery["no1"] +","
sql += biglottery["no2"] +","
sql += biglottery["no3"] +","
sql += biglottery["no4"] +","
sql += biglottery["no5"] +","
sql += biglottery["no6"] +","
sql += biglottery["special"] +" "
sql += "where not exists (select volume from Big_Lottery where volume = '"+ biglottery["volume"] +"')"
com.ExeSql(sql)
