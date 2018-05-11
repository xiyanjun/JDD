# -*- coding:utf-8 -*-
#处理表trainv1-1
import numpy as np
import pandas as pd
train=pd.read_csv('trainv1-1.csv')
df=pd.DataFrame(train)
df['a_date']=df['a_date']*df['a_num']
df=df.drop('a_num',axis=1)
print(df)

#转换成数组
mat=df.as_matrix()
total_row=len(mat)
print(total_row)

i=1
sum=mat[0][1]
res=[]
while i<total_row:
    if mat[i][0]==mat[i-1][0]:
        sum+=mat[i][1]
    else:
        res.append([mat[i-1][0],sum])
        print('已完成第%d个计算' % (res[-1][0]))
        sum=mat[i][1]
    i=i+1
res.append([mat[i-1][0],sum])
print('已完成第%d个计算'%(res[-1][0]))
mat=res
print(mat)
print('单一化处理完成！')
#数组转化成DF

head=['user_id','pred_date']
train2=pd.DataFrame(mat,columns=head)
print('数组转化成DF完成！')
train2.to_csv('trainv1-2.csv',index=False)
print('CSV存储完成！')
print('实验完成！')

test=pd.read_csv('trainv1-2.csv')
print(test)
