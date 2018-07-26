from bokeh.io import show, output_file
from bokeh.plotting import figure

import common as com

__startVolume = "107000075"
__endVolume = "107000076"

sql = "select * from Two_Win where volume between \'" + __startVolume + "\' and \'" + __endVolume + "\'"
rows = com.getTableData(sql)

#建立 1 到 24 字典 做為儲存統計用
dic = {}
for i in range(1,25):
    dic.setdefault("no"+ str(i),0)

#統計 1 到 24 出現次數 並存回字點中 
if(rows != None):
    for row in rows:
#        print("{}".format(row[0]))
        for j in range(2,14):
            dic["no" + str(row[j])] += 1            
#print(dic)
# =============================================================================
# #顯示柱狀圖(matplotlib.pyplot)        
# listx1 = dic.keys() 
# listy1 = dic.values()
# plt.bar(listx1, listy1)
# #plt.legend() #顯示圖例
# plt.xlim(1, 24)
# plt.ylim(1, 10)
# plt.title("Number Count")
# plt.xlabel("Number")
# plt.ylabel("Hit Number Count")
# plt.show() #顯示圖表
# =============================================================================


#沒找到好方法 按 字典裡的 key 值 來排序
# setp1 去"no" 如果沒去 直sorted 排序無法如預期的從小排到大 
dic_sort = {}
for  i in range(1,25):
    dic_sort[i] = dic["no"+ str(i)]
    
# setp2 將去完 "no" 用sorted 排序 排序完後傳回的 型別為 list
dic_sort = sorted(dic_sort.items(), key=lambda d: d[0])

# setp3 將 list 裡的 tuple(key,value) 再分別存入 list_x,list_y 中 供 bokeh.plottin 所使用
list_x = []
list_y = []

for t in dic_sort:
    list_x.append(str(t[0])) # figure 的  x_range ＝ list 內元素 必需為字串
    list_y.append(t[1])
    

#顯示柱狀圖(bokeh) 
output_file("bars.html")
#listx = list(dic.keys())
#listy = list(dic.values())
listx = list_x
listy = list_y

p = figure(x_range=listx, plot_height=250, title="Number Counts",
           toolbar_location=None, tools="")
p.vbar(x=listx, top=listy, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0
show(p)

