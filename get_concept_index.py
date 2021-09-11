#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
该脚本用于获取概念板块行情数据
"""

import time
import os
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tushare as ts

# # 若存在concept文件，则删除;不存在，则生成
if os.path.exists("concept"):
    shutil.rmtree("concept")  # delete concept folder
os.makedirs("concept")  # make new concept folder

#设置tushare接口
ts.set_token('53f7543547a1c56ac53a0aa58521ed9e2de575e8cca53cbd85775fc6')
pro = ts.pro_api()
concept = pro.concept()
concept.to_excel('./concept_index.xlsx','encoding=utf-8')

data = pd.read_excel('./concept_index.xlsx')
stock_codes=data['code']

# 将数据保存到concept文件夹中。
i=0
for stock_code in stock_codes:

    df = pro.concept_detail(id=stock_code, fields='ts_code,name')
    #保存到industry_index文件夹，并以相应股票代码命名
    df.to_excel('./concept/'+ stock_code +'.xlsx','encoding=utf-8')
    i+=1
    print("downloading processing===>",i)


