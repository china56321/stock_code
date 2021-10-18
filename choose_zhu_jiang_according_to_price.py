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
f = open("xinggao.txt" , "w")
f.truncate()
f.close

#获取今天日期。
date=time.strftime("%Y%m%d")
date_end=int(date)

#读取mean_5_10_20文件夹里的所有excel文件。
mean_5_10_20_names = os.listdir('./mean_5_10_20/')

i=0
# 循环读取每一个文件。
for mean_5_10_20_name in mean_5_10_20_names:
  # print(mean_5_10_20_name)
  #读取单个excel文件。
  df = pd.read_excel('./mean_5_10_20/' + mean_5_10_20_name)
  # print(mean_5_10_20_name.split(".")[0])
  #如果是科创板股票，或是新股，且上市不超过200天，则跳过。
  if mean_5_10_20_name.split(".")[0][:3]=="688" or len(df['open'])<180:
    continue
  else:
    #收盘价
    stock_close=df['close'] 
    #开盘价
    stock_open=df['open']
    #3日均线
    ma3=df['ma3'] 
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
    #成交额
    amount=df["amount"]
    #均价
    mean_price=amount[0]/vol[0]*10

  # *******在此处写你的交易逻辑*****************************************************************************
    
    # 连续五天沿着五日线向上走
    # if stock_close[4]>=ma3[4] and stock_close[3]>=ma3[3] and  stock_close[2]>=ma3[2] and stock_close[1]>=ma3[1] and stock_close[0]>=ma3[0] and stock_close[0]<=ma30[0]*1.13:

    # 连续三天沿着三日线向上走
    # if stock_close[2]>=stock_open[2]>=ma5[2] and stock_close[1]>=stock_open[1]>=ma3[1] and stock_close[0]>=ma3[0] :
  
    #前三日涨幅大于4，最近两天收盘小于开盘
    # if vol[2]/vol[3]>=2 and pct_chg[2]>=5 and stock_open[2]<=stock_close[1]<=stock_close[2] and stock_close[1]>=stock_close[0]>=stock_open[2]:

    #三降一升
    # if (stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and pct_chg[0]>=2 and stock_close[0]>=mean_price and turnover_rate[0]>=2 ) or (stock_open[0]<=stock_close[0] and stock_open[1]<=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and stock_open[4]>=stock_close[4] and pct_chg[0]>=2 and stock_close[0]>=mean_price and turnover_rate[0]>=2 ): 
    
    # 连续五天微量上涨
    # if stock_close[0]>=stock_open[0] and stock_close[1]>=stock_open[1] and stock_close[2]>=stock_open[2] and stock_close[3]>=stock_open[3] and stock_close[4]>=stock_open[4]  and stock_close[0]>=ma5[0]>=ma10[0]>=ma20[0]>=ma30[0] and stock_close[1]>=ma5[1] and stock_close[2]>=ma5[2] and stock_close[3]>=ma5[3] and stock_close[4]>=ma5[4] and pct_chg[0]>=2:
    
    # 两升两降一升，或两升三降一升
    # if (stock_close[4]>stock_open[4] and stock_close[3]>stock_open[3] and stock_close[2]<stock_open[2] and stock_close[1]<stock_open[1] and stock_close[0]>=stock_open[0] and pct_chg[3]>=2 and pct_chg[4]>=2 and pct_chg[0]>=1)\
    #     or (stock_close[5]>stock_open[5] and stock_close[4]>stock_open[4] and stock_close[3]<=stock_open[3] and stock_close[2]<=stock_open[2] and stock_close[1]<=stock_open[1] and stock_close[0]>=stock_open[0] and pct_chg[5]>=2 and pct_chg[4]>=2 and pct_chg[0]>=1) \
    #     or (stock_close[3]>=stock_open[3] and stock_close[2]>=stock_open[2] and stock_close[1]<=stock_open[1] and stock_close[0]>=stock_open[0] and pct_chg[3]>=2 and pct_chg[1]>=2 and pct_chg[0]>=1) and mean_price<=stock_close[0]<=100 and stock_close[0]<=ma30[0]*1.13  : 
        
    #两升两降,或两升三降
    # if ((stock_close[3]>=stock_open[3] and stock_close[2]>=stock_open[2] and pct_chg[3]>=3 and pct_chg[2]>=3 and stock_close[1]<=stock_open[1] and stock_close[0]<=stock_open[0])\
    #     or  (stock_close[4]>=stock_open[4] and stock_close[3]>=stock_open[3] and pct_chg[4]>=3 and pct_chg[3]>=3 and stock_close[2]<=stock_open[2] and stock_close[1]<=stock_open[1] and stock_close[0]<=stock_open[0]) ) and stock_close[0]<=70 : 
    

    #放量上涨
    if vol[0]/vol[1]>=2 and turnover_rate[0]>=2  and stock_close[0]>stock_open[0] and pct_chg[0]>=5 and stock_close[0]>=mean_price and stock_close[0]<=ma30[0]*1.13 :

    # 连续两天放量上涨
    # if (vol[0]/vol[2]>=2) and turnover_rate[0]>=2  and (vol[1]/vol[2]>=2) and (stock_close[0]>=stock_open[0]) and (stock_close[1]>stock_open[1]) and stock_close[0]<=ma30[0]*1.13:

    # 放巨量上涨，且换手率大于2
    # if vol[0]/vol[1]>=2.5 and pct_chg[0]>=5 and turnover_rate[0]>=2 and stock_close[0]<=ma30[0]*1.12:

#******股价创新高********************************************************************************************
    # 定义一个存放近10天内的字典
    # stock_dict_close={ }
    # for j in range(1,11):
    #   # 遍历将收盘价赋给对应的键
    #   stock_dict_close[j]=stock_close[j]
    # # 获得键
    # stock_key=list(stock_dict_close.keys())
    # # 获取值
    # stock_value=list(stock_dict_close.values())
    # # 获取最大值对应的键
    # max_key=max(stock_dict_close,key=stock_dict_close.get)
    # # 获取最小值对应的键
    # min_key=min(stock_dict_close,key=stock_dict_close.get)

    # # 若今日股价大于10日内的最高收盘价
    # if (pct_chg[0]>=3 and turnover_rate[0]>=2 and stock_close[0]>=float(max(stock_value))  and stock_close[0]>=ma5[0] and stock_close[0]>=mean_price and stock_close[0]<=ma30[0]*1.13):
   

#******股价创新高********************************************************************************************
    # # 定义一个存放近5天内的字典
    # stock_dict_close={ }
    # #定义一个字典，用于存放成交量
    # vol_dict={ }
    # for j in range(1,6):
    #   # 遍历将收盘价赋给对应的键
    #     stock_dict_close[j]=stock_close[j]
    #     #将成交量存放到对应键的字典里
    #     vol_dict[j]=vol[j]
    # # 获得键
    # stock_key=list(stock_dict_close.keys())
    # # 获取值
    # stock_value=list(stock_dict_close.values())
    # # 获取最大值对应的键
    # max_key=max(stock_dict_close,key=stock_dict_close.get)
    # # 获取最小值对应的键
    # min_key=min(stock_dict_close,key=stock_dict_close.get)
    # #获取5日内最小成交量
    # min_vol=min(list(vol_dict.values()))

    # # 今日最高价成交量是5日内最低收盘价日成交量的1.8倍以上，且最高价日涨幅大于3
    # if pct_chg[0]>=3 and turnover_rate[0]>=2 and stock_close[0]>=max(stock_value) and vol[0]/min_vol>=2 and stock_close[0]>=stock_open[0] and stock_close[0]>=ma5[0] and stock_close[0]>=mean_price and stock_close[0]<=ma30[0]*1.13:


#******股价创新30新高,且涨幅大于8，成交量是前一日3倍以上********************************************************************************************
    # 定义一个存放近30天内的字典
    # stock_dict_close={ }
    # for j in range(1,30):
    #   # 遍历将收盘价赋给对应的键
    #   stock_dict_close[j]=stock_close[j]
    # # 获得键
    # stock_key=list(stock_dict_close.keys())
    # # 获取值
    # stock_value=list(stock_dict_close.values())
    # # 获取最大值对应的键
    # max_key=max(stock_dict_close,key=stock_dict_close.get)
    # # 获取最小值对应的键
    # min_key=min(stock_dict_close,key=stock_dict_close.get)

    # # 若今日股价大于10日内的最高收盘价
    # if (pct_chg[0]>=5 and vol[0]/vol[1]>=2 and turnover_rate[0]>=2 and stock_high[0]>=float(max(stock_value))) and stock_close[0]/ma30[0]<=1.13:
   
#******股价创100日新高,且涨幅大于3，成交量是前一日2倍以上********************************************************************************************
    # 定义一个存放近100天内的字典
    # stock_dict_close={ }
    # for j in range(1,100):
    #   # 遍历将收盘价赋给对应的键
    #   stock_dict_close[j]=stock_close[j]
    # # 获得键
    # stock_key=list(stock_dict_close.keys())
    # # 获取值
    # stock_value=list(stock_dict_close.values())
    # # 获取最大值对应的键
    # max_key=max(stock_dict_close,key=stock_dict_close.get)
    # # 获取最小值对应的键
    # min_key=min(stock_dict_close,key=stock_dict_close.get)

    # # 若今日股价大于10日内的最高收盘价
    # if (pct_chg[0]>=5 and vol[0]/vol[1]>=2 and turnover_rate[0]>=2 and stock_high[0]>=float(max(stock_value))) and stock_close[0]/ma30[0]<=1.13:
   

#*****以下不动*************************************************************************************
      #以添加的形式打开zhu_jiang.txt文件
      with open("xinggao.txt",'a') as f:
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


#****10内有一次涨停*********************************************************************************************************
    # 定义一个存放近10天列表
    # pct_chg_10=[ ]
    # # 将10天内的收盘价存入stock_close_10列表
    # for j in range(0,10):
    #     pct_chg_10.append(pct_chg[j])

    # #遍历stock_close_10列表
    # for k in pct_chg_10:
    # #  判断10天内的收盘价是否涨停
    #     if (9.88<=k<=10.3 or 19.7<=k<=20.3 ) and stock_close[0]<=ma30[0]*1.15 :
    #         with open("xinggao.txt",'a') as f:
    #             #截取股票代码，包括后缀
    #             stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
    #             #分离后缀，仅保留股票代码
    #             stock=stock.split(".")[0]
    #             #写入zhu_jiang.txt文件
    #             f.write(stock)
    #             #换行
    #             f.write('\n')
    #             i+=1
    #             print("The number of stock be choosen===>",i)







