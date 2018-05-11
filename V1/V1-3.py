# -*- coding:utf-8 -*-
#处理表格trainv1-2,生产结果
import numpy as np
import pandas as pd
#读取文件
df=pd.read_csv('trainv1-2.csv')
#按照pred_date降序排列
df=df.sort_values(by='pred_date',ascending=False)
#选取前五万行数据
df=df[:50000]
#计算时间差
timebase=df.iat[0,1]-df.iat[49999,1]
timelow=df.iat[49999,1]
print(timebase)
def adate(line):
    date1=line['pred_date']
    date1=(date1-timelow)*31//timebase
    if date1==0:
        return '2017-05-01'
    if date1<10:
        return '2017-05-0'+str(date1)
    else:
        return '2017-05-'+str(date1)
df['pred_date']=df.apply(adate,axis=1)
print(df)
df.to_csv('result.csv',index=False)
print('实验完成！')