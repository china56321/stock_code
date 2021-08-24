#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import pandas as pd
import os
import numpy as np   
import matplotlib.pyplot as plt 
import math
f = open("choosen_stock_xie_li.txt" , "w")
f.truncate()
f.close

mean_5_10_20_names = os.listdir('./mean_5_10_20/')
j=0
for mean_5_10_20_name in mean_5_10_20_names :
    open_data=[]
    close_data=[]

    # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)  
    df = pd.read_excel('./mean_5_10_20/' + mean_5_10_20_name,sheet_name=0)

    if mean_5_10_20_name.split(".")[0][:3]=="688":
        continue
    elif len(df['open'])<200:
        continue

    stock_open=df['open']
    stock_close=df['close']
    mean_5=df['ma5']  
    mean_10=df['ma10']
    mean_20=df['ma20'] 

    for i in range(0,60):
        open_data=list(open_data)
        open_data.append(stock_open[i])
        close_data=list(close_data)
        close_data.append(stock_close[i])

    data=np.array(list(zip(open_data,close_data)))

    open_data,close_data=data[:,0].reshape(-1,1),data[:,1]

    from sklearn import linear_model # 引用 sklearn库，主要为了使用其中的线性回归模块

    # TODO 1. 实例化一个线性回归的模型
    regr = linear_model.LinearRegression()
    # TODO 2. 在x,y上训练一个线性回归模型。 如果训练顺利，则regr会存储训练完成之后的结果模型
    regr.fit(open_data, close_data)

    # TODO 3. 画出身高与体重之间的关系
    plt.scatter(open_data, close_data, color='red')

    # 画出已训练好的线条
    plt.plot(open_data, regr.predict(open_data), color='blue')

    coe=regr.coef_ 
    print("gradient:",coe)
    #将斜率转换为弧度
    angle_h=math.atan(coe)
    #将弧度转换为角度
    angle_j=math.degrees(angle_h)

    # print('angle_j:',angle_j)

    # 利用已经训练好的模型去预测身高为163的人的体重
    # print ("Standard weight for person with 163 is %.2f"% regr.predict([[163]]))

    # 逻辑
    if (1<=coe):
        with open("choosen_stock_xie_li.txt",'a') as f:
            stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
            stock=stock.split('.')[0]
            f.write(stock)
            f.write('\n')
            j+=1
            print("The number of stock be choosen===>",j)

    # TODO 3. 画出open_data,close_data之间的关系
    plt.scatter(open_data, close_data, color='red')
    # 画出已训练好的线条
    plt.plot(open_data, regr.predict(open_data), color='blue')
    #绘制坐标图
    plt.xlabel('open')
    plt.ylabel('close')
    # plt.show()




