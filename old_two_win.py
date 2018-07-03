# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import sqlite3

#取得網頁上的表格
tables = pd.read_html("http://www.taiwanlottery.com.tw/lotto/Lotto1224/history.aspx")

# =============================================================================
# n = 1
# for table in tables:
#     print("第 " + str(n) + " 表格")
#     print(table.head())
#     print()
#     n += 1
# =============================================================================

#將表格上的資料 組成sql語句
sql = []
temp = "delete from Two_Win"
sql.append(temp)

for i in range(2,len(tables)):
    table = tables[i]
    volume = table[0][1]
    date = table[1][1]
    
    temp = "insert into Two_Win values("
    temp +="\"" + volume +"\","
    temp +="\"" + date +"\","
    for j in range(1,13):
        temp += str(int(table[j][4])) 
        if(j==12):
            temp += ")"
        else:
            temp +="," 
    sql.append(temp) 

#將資料寫入 sqllite 中
conn = sqlite3.connect('lottery.db') #建立資料庫連線
cursor = conn.cursor() #建立 cursor 物件

for k in range(0,len(sql)):
    cursor.execute(sql[k])  
  
conn.commit()#主動更新
conn.close()#關閉資料庫連線










