import sqlite3

__connectionString = "lottery.db"
    
def myName(name):
    return "我的名字是" + name

def FormatDate(vDate):
    temp = []
    temp = vDate.split('/')
    
    result = ""
    for i in range(0,len(temp)):
        result += str("{:0>2d}".format(int(temp[i])))
        if( i != len(temp)-1):
            result += "/"
    return result

def ExeSql(vSql):
    conn = sqlite3.connect(__connectionString) #建立資料庫連線
    cursor = conn.cursor() #建立 cursor 物件
    cursor.execute(vSql)
#    print(vSql)
    conn.commit()#主動更新
    conn.close()#關閉資料庫連線
        
def ExeSqls(vSql):    
    conn = sqlite3.connect(__connectionString) #建立資料庫連線
    cursor = conn.cursor() #建立 cursor 物件    
    for k in range(0,len(vSql)):
        cursor.execute(vSql[k])
#        print(vSql[k])
    conn.commit()#主動更新
    conn.close()#關閉資料庫連線    
    
    
def getTableData(vSql):
    conn = sqlite3.connect(__connectionString)
    cursor = conn.execute(vSql)
    result = cursor.fetchall()     
#    print(result)
    conn.close()#關閉資料庫連線
    return result