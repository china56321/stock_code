#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import os 
import shutil
import time
#打开zhu_jiang.txt，并删除其中的内容。
f = open("zhu_jiang.txt" , "w")
f.truncate()
f.close

#获取今天日期。
date=time.strftime("%Y%m%d")
date_end=int(date)

#读取mean_5_10_20文件夹里的所有excel文件。
mean_5_10_20_names = os.listdir('./mean_5_10_20/')

i=0
# 循环读取每一个文件。
for mean_5_10_20_name in mean_5_10_20_names :
  #读取单个excel文件。
  df = pd.read_excel('./mean_5_10_20/' + mean_5_10_20_name)

  #如果是科创板股票，则跳过。或若是新股，且上市不超过200天，则跳过。
  if mean_5_10_20_name.split(".")[0][:3]=="688" or len(df['open'])<200:
    continue


  #收盘价
  stock_close=df['close'] 
  #开盘价
  stock_open=df['open']
  #5日均线
  ma5=df['ma5'] 
  #10日均线
  ma10=df['ma10']
  #20日均线
  ma20=df['ma20'] 
  #30日均线
  ma30=df["ma30"]
  #60日均线
  ma60=df["ma60"]
  #120日均线
  ma120=df["ma120"]
  #250日均线
  ma250=df["ma250"]
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
  #换手率
  turnover_rate=df["turnover_rate"]
  #量比
  volume_ratio=df["volume_ratio"]


# *******在此处写你的交易逻辑*****************************************************************************

#1*******************************************************************************************************
  # 今日放量上涨，涨幅大于1
  # if (1.5<=vol[0]/vol[1]) and stock_close[0]>stock_open[0] and pct_chg[0]>1 and mean_30[0]<=mean_10[0]<=mean_5[0]<=stock_close[0]:

  # 昨天放量上涨，今日缩量，可上涨，可下跌
  if vol[1]/vol[2]>=1.5 and pct_chg[1]>=2 and vol[1]/vol[0]>=1.2:

#      # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)
#      #以添加的形式打开zhu_jiang.txt文件
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


#2************************************************************************************************

#   b=1
#   a=0
#   c=[]
#   for trade_date in trade_dates:
#     if trade_date in range(20210428,date_end):
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
#       a+=1
#       b+=1

#       else:
#         continue
#     else:
#       continue

#     print("a is :",a)
#     print("b is :",b)
# print("Over")


