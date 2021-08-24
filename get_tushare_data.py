#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
此程序用来从tushare网站获取每日股票数据。
"""

import time
import os
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tushare as ts

#设置tushare接口
ts.set_token('53f7543547a1c56ac53a0aa58521ed9e2de575e8cca53cbd85775fc6')
pro = ts.pro_api()

# 若存在mean_5_10_20文件，则删除;不存在，则生成
if os.path.exists("mean_5_10_20"):
    shutil.rmtree("mean_5_10_20")  # delete mean_5_10_20 folder
os.makedirs("mean_5_10_20")  # make new mean_5_10_20 folder

# 获取20210430这一天的数据并保存到stock.xlsx文件中,主要为了利用它的股票代码为下一步下载全部股票数据做准备。
#若今天是非交易日，则将此日期设为最近一天的交易日日期。并将下一行date代码注释，按ctrl + / 键。
# date="20210629"

#若今天是交易日。则将上一行date代码注释，按ctrl + / 键 。
date=time.strftime("%Y%m%d")
data = pro.daily(trade_date=date)
data.to_excel('day_stock.xlsx','encoding=utf-8')

# 读取stock.xlsx文件
df = pd.read_excel('day_stock.xlsx')
# 找到股票代码这一列
stock_codes=df['ts_code']

# 将数据保存到mean_5_10_20文件夹中。下载数据的起始日期：20200127，截止日期：20200828。ma里的参数为5日，10日，20日均线
i=0
for stock_code in stock_codes:

    df = ts.pro_bar(ts_code=stock_code ,start_date='20201001', end_date=date, ma=[3,5, 10,20,30,60,120,250],factors=['tor', 'vr'])
    #保存到mean_5_10_20文件夹，并以相应股票代码命名
    df.to_excel('./mean_5_10_20/'+ stock_code +'.xlsx','encoding=utf-8')
    i+=1
    print("downloading processing===>",i)

