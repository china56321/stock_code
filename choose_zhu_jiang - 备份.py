#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import os 
import shutil

#打开zhu_jiang.txt，并删除其中的内容。
f = open("zhu_jiang.txt" , "w")
f.truncate()
f.close

#读取mean_5_10_20文件夹里的所有excel文件。
mean_5_10_20_names = os.listdir('./mean_5_10_20/')

i=0
# 循环读取每一个文件。
for mean_5_10_20_name in mean_5_10_20_names :
  #读取单个excel文件。
  df = pd.read_excel('./mean_5_10_20/' + mean_5_10_20_name)
  #如果是科创板股票则跳过。
  if mean_5_10_20_name.split(".")[0][:3]=="688":
    continue
  #若是新股，且上市不超过200天，则跳过。
  elif len(df['open'])<20:
    continue
  #收盘价
  stock_close=df['close'] 
  #开盘价
  stock_open=df['open']
  #5日均线
  mean_5=df['ma5'] 
  #10日均线
  mean_10=df['ma10']
  #20日均线
  mean_20=df['ma20'] 
  #30日均线
  mean_30=df["ma30"]
  #60日均线
  mean_60=df["ma60"]
  #120日均线
  mean_120=df["ma120"]
  #250日均线
  mean_250=df["ma250"]
  #涨跌幅
  pct_chg=df['pct_chg']
  #最低价
  stock_low=df["low"]
  #最高价
  stock_high=df["high"]
  #昨日收盘价
  pre_close=df["pre_close"]
  #成交量
  vol=df["vol"]
  #交易日
  trade_dates=df["trade_date"]

  # *******在此处写你的交易逻辑*****************************************************************************
#   b=1
#   a=0
#   c=[]
#   for trade_date in trade_dates:
#     if trade_date in range(20210428,20210501):
#       # print("trade_date is :",trade_date)
#       for i in range(a,b):
#         if vol[i]/vol[b-1]>=2.5 and stock_close[i]>=stock_open[i]:
#           c.append(1)
#         else:
#           continue
#       d=sum(c)
#       c.clear()

#       if d==4:
#        #以添加的形式打开zhu_jiang.txt文件
#         with open("zhu_jiang.txt",'a') as f:
#           #截取股票代码，包括后缀
#           stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
#           #分离后缀，仅保留股票代码
#           stock=stock.split(".")[0]
#           #写入zhu_jiang.txt文件
#           f.write(stock)
#           #换行
#           f.write('\n')
#       if b>30:
#         continue
#       else:
#         a+=1
#         b+=1

#       else:
#         continue
#     else:
#       continue

#     print("a is :",a)
#     print("b is :",b)
# print("Over")





#*******************************************************************************************************

#   #前三日涨幅大于5，今日收盘小于开盘
#   # if pct_chg[1]>=5 and stock_open[1]<=stock_close[0]<=stock_close[1] and stock_open[0]>=stock_close[0] :
  
#   #前三日涨幅大于4，最近两天收盘小于开盘
#   if pct_chg[2]>=4 and stock_open[2]<=stock_close[1]<=stock_close[2] and stock_open[0]>=stock_close[0]>=stock_open[2] and stock_open[1]>=stock_close[1] :
  
#   #三降
#   # if stock_open[0]>=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and pct_chg[0]<=(-2) and pct_chg[1]<=(-2) and pct_chg[2]<=(-2):

#   #四降
#   # if stock_open[0]>=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4]:
 
#   #五降
#   # if stock_open[0]>=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4] :
 
#   #六降
#   # if stock_open[0]>=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4] and stock_open[5]>=stock_close[5]:
 
#   #七降
#   # if stock_open[0]>=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4] and stock_open[5]>=stock_close[5]  and stock_open[6]>=stock_close[6]:
 
#   #八降
#   # if stock_open[0]>=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4] and stock_open[5]>=stock_close[5] and stock_open[6]>=stock_close[6] and stock_open[7]>=stock_close[7]:
 

#   #二降一升
#   # if stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2]:  

#   #三降一升
  if stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3]:  

#   #四降一升
#   # if stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4]: 

#   #五降一升
#   # if stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4]  and stock_open[5]>=stock_close[5]: 

#   #六降一升
#   # if stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4]  and stock_open[5]>=stock_close[5]  and stock_open[6]>=stock_close[6]:
  
#   #七降一升
#   # if stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4]  and stock_open[5]>=stock_close[5]  and stock_open[6]>=stock_close[6] and stock_open[7]>=stock_close[7]:
      
#   #八降一升
#   # if stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4]  and stock_open[5]>=stock_close[5]  and stock_open[6]>=stock_close[6] and stock_open[7]>=stock_close[7] and stock_open[8]>=stock_close[8]:
   
#   #三连阳
#   # if stock_open[0]<stock_close[0] and stock_open[1]<stock_close[1] and stock_open[2]<stock_close[2] and 0<=pct_chg[0]<2 and 0<pct_chg[1]<2 and 0<=pct_chg[2]<2:
     
#      # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)
     #以添加的形式打开zhu_jiang.txt文件
      with open("zhu_jiang.txt",'a') as f:
        #截取股票代码，包括后缀
        stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
        #分离后缀，仅保留股票代码
        stock=stock.split(".")[0]
        #写入zhu_jiang.txt文件
        f.write(stock)
        #换行
        f.write('\n')
        i+=1
        print("The number of stock be choosen===>",i)


