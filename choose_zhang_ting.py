#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import os 
import shutil

f = open("zhang_ting.txt" , "w")
f.truncate()
f.close

#读取mean_5_10_20文件夹里的所有excel文件
mean_5_10_20_names = os.listdir('./mean_5_10_20/')

i=0
# 循环读取每一个文件
for mean_5_10_20_name in mean_5_10_20_names :

  df = pd.read_excel('./mean_5_10_20/' + mean_5_10_20_name)

  if mean_5_10_20_name.split(".")[0][:3]=="688":

    continue

  elif len(df['open'])<200:

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

  # *********************************************************************************************************************************************

  # 判断是否为涨停股
  if (9.9<=float(pct_chg[0])<=10.3) or (19.7<=float(pct_chg[0])<=20.3):
     # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)
      with open("zhang_ting.txt",'a') as f:
        stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
        stock=stock.split(".")[0]
        f.write(stock)

        f.write('\n')
        i+=1
        print("The number of stock be choosen===>",i)


