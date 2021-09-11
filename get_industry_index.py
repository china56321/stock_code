#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
该脚本用于获取行业行情数据
"""

import time
import os
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tushare as ts

# # 若存在industry文件，则删除;不存在，则生成
if os.path.exists("industry"):
    shutil.rmtree("industry")  # delete industry folder
os.makedirs("industry")  # make new industry folder

#设置tushare接口
ts.set_token('53f7543547a1c56ac53a0aa58521ed9e2de575e8cca53cbd85775fc6')
pro = ts.pro_api()
concept = pro.ths_index()
concept.to_excel('./industry.xlsx','encoding=utf-8')

data = pd.read_excel('./industry.xlsx')
stock_codes=data['ts_code']

# 将数据保存到industry文件夹中。下载数据的起始日期：20201010，截止日期：20200805。fields里的参数为行业代码，交易日期，开盘，收盘，最高，最低，涨跌副，昨日收盘，换手率，成交量，平均价，总市值，流通市值
i=0
for stock_code in stock_codes:
    df = df = pro.ths_daily(ts_code=stock_code, start_date='20210101', end_date='20210910', fields='ts_code,trade_date,open,close,high,low,pct_change,pre_close,turnover_rate,vol,avg_price,total_mv,float_mv')
    #保存到industry文件夹，并以相应股票代码命名
    df.to_excel('./industry/'+ stock_code +'.xlsx','encoding=utf-8')
    i+=1
    print("downloading processing===>",i)
    if i%5==0:
        time.sleep(61)

