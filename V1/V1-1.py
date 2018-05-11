# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
#商品基本信息表
#商品价格/标识/品类（预测品类为101和30，其它为高相关品类）/
#商品三个参数，-1为空
sku=pd.read_csv('jdata_sku_basic_info.csv')
#用户基本信息表
#用户标识/年龄（-1未知）/性别（0男1女2保密）/等级
basic_info=pd.read_csv('jdata_user_basic_info.csv')
#用户行为表
#用户标识/商品标识/行为日期/行为次数/行为类型（1浏览，2关注）
action=pd.read_csv('jdata_user_action.csv')
#用户订单表
#用户标识/商品标识/下单标识/下单日期/下单区域/下单件数
order=pd.read_csv('jdata_user_comment_score.csv')
#评论分数数据表
#用户标识/评论时间/下单标识(与订单表关联）/评分级别（1好评2中评3差评-1为空）
comment_score=pd.read_csv('jdata_user_comment_score.csv')
#选取用户行为表中的关注
#train=action[(action['a_type']==2)]
#日期装换，越靠近2017-5-1号权重越高
i=0
def adate(line):
    global i
    a = 366
    b = 30
    c = 1
    i=i+1
    date1=line['a_date'].split('-')
    #乘以行为类型
    date2=((int(date1[0])-2016)*a+(int(date1[1]))*b+(int(date1[2]))*c)*line['a_type']
    print('已完成第%d次转换'%i)
    return date2

#将日期转换成数值，数值越大表示可能性越高。
train=action
train['a_date']=train.apply(adate,axis=1)
print('开始丢弃商品标号列和行为类型列！')
train=train.drop(['sku_id'],axis=1)
train=train.drop(['a_type'],axis=1)
train.to_csv('trainv1-1.csv',index=False)
print('已生成新的CSV文件V1-1')