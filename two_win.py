# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import sqlite3
from bs4 import BeautifulSoup

#雙贏彩資料字典
two_win = {"volume":"","date":"","no1":0,"no2":0,"no3":0,"no4":0,"no5":0,"no6":0,
           "no7":0,"no8":0,"no9":0,"no10":0,"no11":0,"no12":0}

#資料來源網址
url='http://www.taiwanlottery.com.tw'
html = requests.get(url)

sp = BeautifulSoup(html.text,'html.parser')
data1 = sp.select("#rightdown")
#print(data1)

data2 = data1[0].find('div',{'class':'contents_box06'})
#print(data2)

#取得第幾期 及 開獎日期
temp = data2.find_all('span',{'class':'font_black15'})
temp_text = temp[0].text
start = temp_text.find("第")
end = temp_text.find("期")
#期號
two_win["volume"]=temp_text[start+1:end]
#開獎日期
two_win["date"] = temp_text[0:8]

#取得雙贏彩號碼
data3 = data2.find_all('div',{'class':'ball_tx'})
#print(data3)

# =============================================================================
# print("開出順序：",end="")
# for n in range(0,12):
#     print(data3[n].text,end="  ")
# =============================================================================

#print("\n大小順序：",end="  ")
for n in range(12,len(data3)):
    two_win["no" + str(n-11)] = data3[n].text
#    print(data3[n].text,end="  ")


#將資料寫入 sqllite 中
conn = sqlite3.connect('lottery.db') #建立資料庫連線
cursor = conn.cursor() #建立 cursor 物件

#判斷是否數據庫已有該表資料 沒有才新增
sql = "select * from Two_Win where volume ='" + two_win["volume"] + "'"
cursor = conn.execute(sql)

if(cursor.fetchone() == None):
    #資料新增
    sql = "insert into Two_Win values("
    sql +="\"" + two_win["volume"] +"\","
    sql +="\"" + two_win["date"] +"\","
    sql += two_win["no1"] +","
    sql += two_win["no2"] +","
    sql += two_win["no3"] +","
    sql += two_win["no4"] +","
    sql += two_win["no5"] +","
    sql += two_win["no6"] +","
    sql += two_win["no7"] +","
    sql += two_win["no8"] +","
    sql += two_win["no9"] +","
    sql += two_win["no10"] +","
    sql += two_win["no11"] +","    
    sql += two_win["no12"] +")"
    cursor.execute(sql)
    
conn.commit()#主動更新
conn.close()#關閉資料庫連線










