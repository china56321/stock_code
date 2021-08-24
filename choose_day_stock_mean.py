#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import numpy as np
# import pandas as pd
# import os 
# import shutil

# from sklearn import linear_model
# import numpy as np
# import matplotlib.pyplot as plt
# mean_5_10_20_names = os.listdir('./mean_5_10_20/')
# j=0
# for mean_5_10_20_name in mean_5_10_20_names :
#     df = pd.read_excel('./mean_5_10_20/' + mean_5_10_20_name)
#     mean_5=df['ma5']  
#     mean_10=df['ma10']
#     mean_20=df['ma20'] 
#     stock_open=df['open']
#     stock_close=df['close']
#     close_data=[]
#     open_data=[]
#     for i in range(0,5):
        
#         # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)
#         if mean_5_10_20_name.split(".")[0][:3]=="688":
#             continue
#         elif len(df['open'])<120:
#             continue
#         else:
#             close_data.append(stock_close[i])
#             open_data.append(stock_open[i])

#             clf=linear_model.LinearRegression()
#             clf.fit (np.array(open_data).reshape(-1,1),np.array(close_data).reshape(-1,1))
#             coe=clf.coef_ 
#             print(coe[0])
#             if (0<=coe<=0.02) and (stock_close[0]>=stock_close[1]) and (stock_close[0]>=stock_open[0]):
#                 with open("choosen_stock.csv",'a') as f:
#                     f.write(mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   ')
#                     f.write('\n')
#                     j+=1
#                     print("The number of stock be choosen===>",j)



#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import os 
import shutil

f = open("choosen_stock.txt" , "w")
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

  elif len(df['open'])<120:

    continue

  stock_close=df['close'] 

  stock_open=df['open']

  mean_5=df['ma5'] 

  mean_10=df['ma10']

  mean_20=df['ma20'] 
  
  pct_chg=df['pct_chg']
  # *********************************************************************************************************************************************
 
  if  pct_chg[1]>=1 and (stock_open[1]<=mean_10[1]<=mean_5[1]<=stock_close[1]) and stock_open[0]>=mean_5[0] and stock_close[0]>=mean_5[0]:  
      # print("name:",'./mean_5_10_20/' + mean_5_10_20_name)
      with open("choosen_stock.txt",'a') as f:
        stock=mean_5_10_20_name.split('.')[0]+'.'+ mean_5_10_20_name.split('.')[1].lower()+'   '
        stock=stock.split(".")[0]
        f.write(stock)

        f.write('\n')
        i+=1
        print("The number of stock be choosen===>",i)


