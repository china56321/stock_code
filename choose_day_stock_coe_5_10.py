#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import pandas as pd
import os
import numpy as np   
import matplotlib.pyplot as plt 
import math
import time

f = open("choosen_stock_xie_li.txt" , "w")
f.truncate()
f.close

mean_5_10_20_names = os.listdir('./mean_5_10_20/')
k=0
for mean_5_10_20_name in mean_5_10_20_names :
    open_data_5=[]
    close_data_5=[]

    open_data_10=[]
    close_data_10=[]

    open_data_25=[]
    close_data_25=[]
    # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)  
    df = pd.read_excel('./mean_5_10_20/' + mean_5_10_20_name,sheet_name=0)

    if mean_5_10_20_name.split(".")[0][:3]=="688":
        continue
    elif len(df['open'])<120:
        continue

    stock_open_5=df['open']
    stock_close_5=df['close']

    stock_open_10=df['open']
    stock_close_10=df['close']

    stock_open_25=df['open']
    stock_close_25=df['close']

    mean_5=df['ma5']  
    mean_10=df['ma10']
    mean_20=df['ma20'] 
    pct_chg=df['pct_chg']


#*******1**********************************************************************
    for i in range(0,5):
        open_data_5=list(open_data_5)
        open_data_5.append(stock_open_5[i])
        close_data_5=list(close_data_5)
        close_data_5.append(stock_close_5[i])

    data=np.array(list(zip(open_data_5,close_data_5)))
    open_data_5,close_data_5=data[:,0].reshape(-1,1),data[:,1]
    from sklearn import linear_model # 引用 sklearn库，主要为了使用其中的线性回归模块
    # TODO 1. 实例化一个线性回归的模型
    regr_5 = linear_model.LinearRegression()
    # TODO 2. 在x,y上训练一个线性回归模型。 如果训练顺利，则regr会存储训练完成之后的结果模型
    regr_5.fit(open_data_5, close_data_5)
    coe_5=regr_5.coef_ 
    angle_5=math.atan(coe_5)
    angle_5=math.degrees(angle_5)
   
    # TODO 3. 画出身高与体重之间的关系
    # plt.scatter(open_data_5, close_data_5, color='red')
    # # 画出已训练好的线条
    # plt.plot(open_data_5, regr_5.predict(open_data_5), color='blue')
   
 #*******2**********************************************************************  
    for j in range(5,10):
        open_data_10=list(open_data_10)
        open_data_10.append(stock_open_10[j])
        close_data_10=list(close_data_10)
        close_data_10.append(stock_close_10[j])

    data=np.array(list(zip(open_data_10,close_data_10)))
    open_data_10,close_data_10=data[:,0].reshape(-1,1),data[:,1]

    regr_10 = linear_model.LinearRegression()
    regr_10.fit(open_data_10, close_data_10)
    coe_10=regr_10.coef_ 

    angle_10=math.atan(coe_10)
    angle_10=math.degrees(angle_10)
    # print("****:",angle_10)

    # plt.scatter(open_data_10, close_data_10, color='red')
    # # 画出已训练好的线条
    # plt.plot(open_data_10, regr_5.predict(open_data_10), color='blue')
    # plt.show()

#*******3**********************************************************************
    for i in range(10,25):
        open_data_25=list(open_data_25)
        open_data_25.append(stock_open_5[i])
        close_data_25=list(close_data_25)
        close_data_25.append(stock_close_25[i])

    data=np.array(list(zip(open_data_25,close_data_25)))
    open_data_25,close_data_25=data[:,0].reshape(-1,1),data[:,1]
    from sklearn import linear_model # 引用 sklearn库，主要为了使用其中的线性回归模块
    # TODO 1. 实例化一个线性回归的模型
    regr_25 = linear_model.LinearRegression()
    # TODO 2. 在x,y上训练一个线性回归模型。 如果训练顺利，则regr会存储训练完成之后的结果模型
    regr_25.fit(open_data_25, close_data_25)
    coe_25=regr_25.coef_ 
    angle_25=math.atan(coe_25)
    angle_25=math.degrees(angle_25)

    # TODO 3. 画出身高与体重之间的关系
    # plt.scatter(open_data_25, close_data_25, color='red')
    # # 画出已训练好的线条
    # plt.plot(open_data_25, regr_25.predict(open_data_25), color='blue')
    # plt.show()
    # print(coe_25)

    # 逻辑
    # if (abs(angle_10)<=(-10) and stock_close_10[0]>=stock_open_10[0] and  stock_close_10[1]>=stock_open_10[1]):
    if ((abs(coe_5)>=0.2) and (0.2<=coe_10<=0.6)):
        with open("choosen_stock_xie_li.txt",'a') as f:
            stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
            stock=stock.split('.')[0]
            f.write(stock)
            f.write('\n')
            k+=1
            print("The number of stock be choosen===>",k)

            # plt.scatter(open_data_10, close_data_10, color='red')
            # # 画出已训练好的线条
            # plt.plot(open_data_10, regr_5.predict(open_data_10), color='blue')
            # plt.show()
    else:
        continue

    # # TODO 3. 画出open_data,close_data之间的关系
    # plt.scatter(open_data_5, close_data_5, color='red')
    # # 画出已训练好的线条
    # plt.plot(open_data_5, regr_5.predict(open_data_5), color='blue')

    # plt.scatter(open_data_10, close_data_10, color='red')
    # # 画出已训练好的线条
    # plt.plot(open_data_10, regr_10.predict(open_data_10), color='blue')
    # #绘制坐标图
    # plt.xlabel('open')
    # plt.ylabel('close')
    # plt.show()




