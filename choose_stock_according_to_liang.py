#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
此程序用来选股

"""
import numpy as np
import pandas as pd
import os 
import shutil
import time
#打开zhu_jiang.txt，并删除其中的内容。
f = open("fangliang.txt" , "w")
f.truncate()
f.close

#获取今天日期。
date=time.strftime("%Y%m%d")
date_end=int(date)

#读取mean_5_10_20文件夹里的所有excel文件。
mean_5_10_20_names = os.listdir('./mean_5_10_20/')

k=0
# 循环读取每一个文件。
for mean_5_10_20_name in mean_5_10_20_names :
  #读取单个excel文件。
  df = pd.read_excel('./mean_5_10_20/' + mean_5_10_20_name)
  #如果是科创板股票，则跳过。
  if mean_5_10_20_name.split(".")[0][:3]=="688":
    continue
  #如果是新股，且上市不超过20天，则跳过。
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


# 1.*******在此处写你的交易逻辑*****************************************************************************
#连续四天量增价增
#   b=1
#   a=0
#   # 起始日期
#   date_start=date_end-20
#   #若日期在相应时间段内，则进行下一步选股。
#   for trade_date in trade_dates:
#     #在此处设定时间段范围。
#     if trade_date in range(date_start,date_end):
#       for i in range(a,b):
#         #若连续四天放量且是前五天的2.5倍，且价格上涨。
#         if vol[i]/vol[i+4]>=2.5 and vol[i+1]/vol[i+4]>=2.5 and vol[i+2]/vol[i+4]>=2.5 and vol[i+3]/vol[i+4]>=2.5 \
#           and stock_close[i]>=stock_open[i] and stock_close[i+1]>=stock_open[i+1] and stock_close[i+2]>=stock_open[i+2] \
#           and stock_close[i+3]>=stock_open[i+3]:

#           #以添加的形式打开zhu_jiang.txt文件
#           with open("fangliang.txt",'a') as f:
#             #截取股票代码，包括后缀
#             stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
#             #分离后缀，仅保留股票代码
#             stock=stock.split(".")[0]
#             #写入zhu_jiang.txt文件
#             f.write(stock)
#             #换行
#             f.write('\n')
#             k+=1
#             print("The number of stock be choosen===>",k)
#             #若大于30天，则截止。
#             if a>30:
#               continue
#             #若小于30天，则每次自动往后退一天
#             a+=1
#             b+=1
#         else:
#           #若大于30天，则截止
#           if a>30:
#             continue
#           #若小于30天，则每次自动往后退一天 
#           a+=1
#           b+=1
#           continue
#     else:
#       continue

# print("Over")



# 2.*******在此处写你的交易逻辑*****************************************************************************
#连续两天量增价增
#起始日期
  date_start=date_end-5
  b=1
  a=0
  #若日期在相应时间段内，则进行下一步选股。
  for trade_date in trade_dates:
    #在此处设定时间段范围。
    if trade_date in range(date_start,date_end):
      for i in range(a,b):
        #若连续两天量增价增且是前三天的2倍以上。
        if vol[i]/vol[i+2]>=2.5 and vol[i+1]/vol[i+2]>=2.5 and stock_close[i]>=stock_open[i] and stock_close[i+1]>=stock_open[i+1]:

          #以添加的形式打开zhu_jiang.txt文件
          with open("fangliang.txt",'a') as f:
            #截取股票代码，包括后缀
            stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
            #分离后缀，仅保留股票代码
            stock=stock.split(".")[0]
            #写入zhu_jiang.txt文件
            f.write(stock)
            #换行
            f.write('\n')
            k+=1
            print("The number of stock be choosen===>",k)
            #若大于30天，则截止。
            if a>30:
              continue
            #若小于30天，则每次自动往后退一天
            a+=1
            b+=1
        else:
          #若大于30天，则截止
          if a>30:
            continue
          #若小于30天，则每次自动往后退一天 
          a+=1
          b+=1
          continue
    else:
      continue

print("Over")

# 3.*******在此处写你的交易逻辑*****************************************************************************
#前三天放量上涨，第二天缩量下跌，今日放量上涨
#起始日期
#   date_start=date_end-8
#   b=1
#   a=0
#   #若日期在相应时间段内，则进行下一步选股。
#   for trade_date in trade_dates:
#     #在此处设定时间段范围。
#     if trade_date in range(date_start,date_end):
#       for i in range(a,b):
#         #前三天放量上涨，第二天缩量下跌，今日放量上涨
#         if vol[i]/vol[i+1]>=2 and stock_close[i]>=stock_open[i] and pct_chg[i]>=2 and vol[i+2]/vol[i+1]>=1.2 and abs(pct_chg[i+1])<=5 \
#           and vol[i+2]/vol[i+3]>=2 and stock_close[i+2]>=stock_open[i+2] and pct_chg[i+2]>=2:

#           #以添加的形式打开zhu_jiang.txt文件
#           with open("fangliang.txt",'a') as f:
#             #截取股票代码，包括后缀
#             stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
#             #分离后缀，仅保留股票代码
#             stock=stock.split(".")[0]
#             #写入zhu_jiang.txt文件
#             f.write(stock)
#             #换行
#             f.write('\n')
#             k+=1
#             print("The number of stock be choosen===>",k)
#             #若大于30天，则截止。
#             if a>30:
#               continue
#             #若小于30天，则每次自动往后退一天
#             a+=1
#             b+=1
#         else:
#           #若大于30天，则截止
#           if a>30:
#             continue
#           #若小于30天，则每次自动往后退一天 
#           a+=1
#           b+=1
#           continue
#     else:
#       continue

# print("Over")

# 4.*******在此处写你的交易逻辑*****************************************************************************
#第二天放量上涨，今日缩量，

#   b=1
#   a=0
#   # 起始日期
#   date_start=date_end-8
#   #若日期在相应时间段内，则进行下一步选股。
#   for trade_date in trade_dates:
#     #在此处设定时间段范围。
#     if trade_date in range(date_start,date_end):
#       for i in range(a,b):
#         #前三天放量上涨，第二天缩量下跌，今日放量上涨
#         if vol[i+1]/vol[i+2]>=2.5 and stock_close[i+1]>=stock_open[i+1] and pct_chg[i+1]>=3  \
#           and vol[i+1]/vol[i]>=1.3 :

#           #以添加的形式打开zhu_jiang.txt文件
#           with open("fangliang.txt",'a') as f:
#             #截取股票代码，包括后缀
#             stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
#             #分离后缀，仅保留股票代码
#             stock=stock.split(".")[0]
#             #写入zhu_jiang.txt文件
#             f.write(stock)
#             #换行
#             f.write('\n')
#             k+=1
#             print("The number of stock be choosen===>",k)
#             #若大于30天，则截止。
#             if a>30:
#               continue
#             #若小于30天，则每次自动往后退一天
#             a+=1
#             b+=1
#         else:
#           #若大于30天，则截止
#           if a>30:
#             continue
#           #若小于30天，则每次自动往后退一天 
#           a+=1
#           b+=1
#           continue
#     else:
#       continue

# print("Over")


#***********以下可删除************************************************************************************

#   #前三日涨幅大于5，今日收盘小于开盘
#   # if pct_chg[1]>=5 and stock_open[1]<=stock_close[0]<=stock_close[1] and stock_open[0]>=stock_close[0] :
  
#   #前三日涨幅大于4，最近两天收盘小于开盘
#   if pct_chg[2]>=4 and stock_open[2]<=stock_close[1]<=stock_close[2] and stock_open[0]>=stock_close[0]>=stock_open[2] and stock_open[1]>=stock_close[1] :   
#      # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)
     #以添加的形式打开zhu_jiang.txt文件
      # with open("fangliang.txt",'a') as f:
      #   #截取股票代码，包括后缀
      #   stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
      #   #分离后缀，仅保留股票代码
      #   stock=stock.split(".")[0]
      #   #写入zhu_jiang.txt文件
      #   f.write(stock)
      #   #换行
      #   f.write('\n')
      #   i+=1
      #   print("The number of stock be choosen===>",i)




