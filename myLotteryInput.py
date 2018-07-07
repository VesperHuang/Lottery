# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:26:25 2018

@author: Vepser
"""
import tkinter as tk
import sqlite3

def click1():
    btnSave.config(state="disabled")
    
    sql = "insert into My_Lottery(category,volume,date,no1,no2,no3,no4,no5,no6,no7,no8,no9,no10,no11,no12) "
    sql += "select"
    sql +="\"two_win\","

    if(volume.get() != ""):
        #期號
        sql +="\"" + str(volume.get()) +"\"," 
    
    if(date.get() != ""):
        #開獎日期
        sql +="\"" + str(date.get()) +"\","    
    
    if(number.get() != ""):
        numbers = []
        numbers = str(number.get()).split(',')
        for i in range(0,len(numbers)):
            sql += numbers[i] 
            if(i==len(numbers)-1):
                sql += " "
            else:
                sql +=","          
    ExeSql(sql)
    btnSave.config(state="active")      
 
def ExeSql(vSql):
    conn = sqlite3.connect('lottery.db') #建立資料庫連線
    cursor = conn.cursor() #建立 cursor 物件
    cursor.execute(vSql)  
    conn.commit()#主動更新
    conn.close()#關閉資料庫連線
    
win = tk.Tk()
win.geometry("300x220")
win.title("我的樂透號碼－輸入")

lblVolume = tk.Label(win,text="期 別：",fg="red",font=("新細明體",12),padx=20,pady=10)
lblVolume.grid(row=0,column=0,padx=5,pady=5,sticky="w")

volume = tk.StringVar()
txtVolume = tk.Entry(win,textvariable=volume)
txtVolume.grid(row=0,column=1,padx=5,pady=5,sticky="w")

lblDate = tk.Label(win,text="日 期：",fg="red",font=("新細明體",12),padx=20,pady=10)
lblDate.grid(row=1,column=0,padx=5,pady=5,sticky="w")

date = tk.StringVar()
txtDate = tk.Entry(win,textvariable=date)
txtDate.grid(row=1,column=1,padx=5,pady=5,sticky="w")

lblNumber = tk.Label(win,text="號 碼：",fg="red",font=("新細明體",12),padx=20,pady=10)
lblNumber.grid(row=2,column=0,padx=5,pady=5,sticky="w")

number = tk.StringVar()
txtNumber = tk.Entry(win,textvariable=number)
txtNumber.grid(row=2,column=1,padx=5,pady=5,sticky="w")

textvar = tk.StringVar()
btnSave = tk.Button(win,textvariable=textvar,width=8,height=1,command=click1)
textvar.set("儲 存")
btnSave.grid(row=3,column=0,padx=5,pady=5,columnspan=2)

win.mainloop()