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
import math 
import matplotlib.pyplot as plt 

#打开zhu_jiang.txt，并删除其中的内容。
f = open("zhu_jiang1.txt" , "w")
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
  if mean_5_10_20_name.split(".")[0][:3]=="688" or len(df['open'])<200:
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
    
    # 连续三天沿着三日线向上走
    # if stock_close[2]>=ma5[2] and stock_close[1]>=ma3[1] and stock_close[0]>=ma3[0] :

    # 连续三天沿着三日线向上走
    # if stock_close[2]>=stock_open[2]>=ma5[2] and stock_close[1]>=stock_open[1]>=ma3[1] and stock_close[0]>=ma3[0] :
  
    #前三日涨幅大于4，最近两天收盘小于开盘
    # if vol[2]/vol[3]>=2 and pct_chg[2]>=5 and stock_open[2]<=stock_close[1]<=stock_close[2] and stock_close[1]>=stock_close[0]>=stock_open[2]:
    # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)

    #三降一升，且收盘价大于均价
    # if stock_open[0]<=stock_close[0] and stock_open[1]>=stock_close[1] and stock_open[2]>=stock_close[2] and stock_open[3]>=stock_close[3] and pct_chg[0]>=1: 
    
    # 连续三天微量上涨
    # if stock_close[0]>=stock_open[0] and stock_close[1]>=stock_open[1] and stock_close[2]>=stock_open[2] and 0<pct_chg[0]<=3 and 0<pct_chg[1]<=3 and 0<pct_chg[2]<=3 and stock_close[0]>=mean_price :
    
    #两升两降一升
    # if ((stock_close[4]>stock_open[4] and stock_close[3]>stock_open[3] and stock_close[2]<stock_open[2] and stock_close[1]<stock_open[1] and stock_close[0]>=stock_open[0])\
    #     or  (stock_close[5]>stock_open[5] and stock_close[4]>stock_open[4] and stock_close[3]<=stock_open[3] and stock_close[2]<=stock_open[2] and stock_close[1]<=stock_open[1] and stock_close[0]>=stock_open[0]) ) and stock_close[0]<=70 and pct_chg[0]>=1 and stock_close[0]>=mean_price: 
    
    #放量上涨
    # if vol[0]/vol[1]>=1.8 and (stock_close[0]>stock_open[0]) and pct_chg[0]>=3 and turnover_rate[0]>=2 and volume_ratio[0]>=1.5 and stock_close[0]>=mean_price:

    # 连续两天放量上涨
    # if (vol[0]/vol[2]>=2) and (vol[1]/vol[2]>=2) and (stock_close[0]>=stock_open[0]) and (stock_close[1]>stock_open[1]) :


#******股价创30日新高********************************************************************************************
    #---以下主要用来获取三日数据拟合后的角度-------------------------------------
    #存放开盘价数据
    open_data=[]
    #存放收盘价数据
    close_data=[]
    # 将三日数据分别放入open_data，close_data
    for k in range(0,5):
        open_data=list(open_data)
        #将开盘数据放入open_data
        open_data.append(stock_open[k])
        close_data=list(close_data)
        #将开盘数据放入close_data
        close_data.append(stock_close[k])
    #将开盘和收盘数据组合在一起，并转为数组
    data=np.array(list(zip(open_data,close_data)))
    #改造开盘，收盘数据以便进行线性拟合
    open_data,close_data=data[:,0].reshape(-1,1),data[:,1]
    # 引用 sklearn机器学习库，主要为了使用其中的线性回归模块
    from sklearn import linear_model 

    # 调用线性回归函数，实例化一个线性回归的模型
    regr = linear_model.LinearRegression()
    # 在open_data,close_data上训练一个线性回归模型。 如果训练顺利，则regr会存储训练完成之后的结果模型
    regr.fit(open_data, close_data)

    # 画出开盘与收盘数据点
    plt.scatter(open_data, close_data, color='red')

    # 画出拟合好的线条
    plt.plot(open_data, regr.predict(open_data), color='blue')
    # 获取斜率
    coe=regr.coef_ 
    #将斜率转换为弧度
    angle_h=math.atan(coe)
    #将弧度转换为角度
    angle_j=math.degrees(angle_h)
   
    #--以下获取股价创新高股票-----------------------------
    #定义一个字典
    a={ }
    for j in range(1,11):
        # 遍历将收盘价赋给对应的键
        a[j]=stock_close[j]
    # 获得键
    key=list(a.keys())
    # 获取值
    value=list(a.values())
    # 获取最大值对应的键
    date_key=max(a,key=a.get)
    # 若今日股价大于30日内的最高收盘价
    # if stock_close[0]>=float(max(value)) and stock_close[0]>=ma5[0]>=ma10[0]>=ma20[0] and stock_close[1]>=ma5[1]>=ma10[1]>=ma20[1] and stock_close[2]>=ma5[2]>=ma10[2]>=ma20[2] and angle_j>=50 :
    if stock_close[0]>=float(max(value)) and stock_close[0]>=ma5[0] and stock_close[1]>=ma5[1] and stock_close[2]>=ma5[2] and angle_j>=55 :


#*****以下不用改动*************************************************************************************
      #以添加的形式打开zhu_jiang.txt文件
      with open("zhu_jiang1.txt",'a') as f:
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


