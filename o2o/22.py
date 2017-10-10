import pandas as pd  # 数据分析
import numpy as np  # 科学计算
from numpy import *
from pandas import Series, DataFrame
import networkx as nx
import matplotlib.pyplot as plt


def createDataSet():
    data_train = pd.read_csv("data.csv")
    yhbh = set([])
    yhbh = yhbh | set(data_train.iloc[:, 2])
    yhbh = list(yhbh)
    sum_len = len(data_train)
    len_yhbh = (len(yhbh))
    index_yhbh = zeros(len_yhbh)
    for i in arange(sum_len):
        index_yhbh[yhbh.index(data_train.iloc[i, 2])] += 1
    flag = 0
    for i in arange(len_yhbh):
        df = data_train[data_train.YHBH == yhbh[i]]
        df_zxzy = list(df.iloc[:, 4])
        float_df_zxzy = [float(item) for item in df_zxzy]
        for j in arange(int(index_yhbh[i])):
            if j < (int(index_yhbh[i]) - 1):
                float_df_zxzy[j] = float(float_df_zxzy[j + 1]) - float(float_df_zxzy[j])
        df['ZXZYGDN'] = float_df_zxzy
        len2 = len(df['ZXZYGDN'])
        cnt = 0
        for x in arange(len2):
            if float_df_zxzy[x] <= 0:
                cnt += 1
        if cnt < len2 - 1:
            df.to_csv('data%d.csv' % flag)
            flag += 1


def createCorr(cor):
    data_list = []
    df = DataFrame(columns=array(arange(348)))
    person = 348
    for i in arange(person):
        list_single = pd.read_csv('data%d.csv' % i)
        list_single = list(list_single.iloc[:22, 5])
        data_list.append(list_single)
    cor_0 = corrcoef(data_list)
    cor_0 = cor_0 * 0.5 + 0.5
    cor_0[cor_0 < cor] = 0
    for val in arange(person):
        cor_0[val][val] = 0
        df.loc[val] = Series(cor_0[val])
    df.to_csv('data_1.csv', header=False, index=False)
    '''print(cor_0)  '''


'''广度优先遍历'''
"""def countCluster(start,cunt,data_df):
    length=len(data_df)
    i=start
    userid=[]
    userid.append(i+1)
    while i<length:
        j=i
        while j<length:
            if data_df.iloc[i,j]>0.0:
                userid.append(j+1)
                break
            j+=1
        if len(userid)<j:
            i=j
        else:
            i+=1 
    if len(userid)>=1:
        cunt+=1
    return cunt,userid
    """
'''访问过的用户集合'''
'''寻找极大连通子图'''


def set_userid_cluster(set_used, data_df):
    length_data = len(data_df)
    set_max = set([item for item in arange(length_data)])
    userid = []
    set_sum = set_max - set_used
    userid_range = [i for i in set_sum]
    print(userid_range)
    len_userid_range = len(userid_range)
    i = 0
    j = 0
    flag = 0
    print(set_used)
    while i < len_userid_range:
        j = i
        while j < len_userid_range:
            if data_df.iloc[userid_range[i], userid_range[j]] > 0.0:
                userid.append(userid_range[j] + 1)
                flag = 1
                break
            else:
                j += 1
        if flag == 1:
            i = j
        else:
            i += 1
        flag = 0
    return userid


def dfs2():
    cluster_userid_list = []
    set_used = set([])
    data_df = pd.read_csv('data_1.csv')
    length = len(data_df)
    userid = set_userid_cluster(set_used, data_df)
    set_used_id = set(userid)
    while len(set_used_id) > 0 and len(set_used_id) < length:
        cluster_userid_list.append(userid)
        userid = set_userid_cluster(set_used_id, data_df)
        set_used_id = set(userid) | set_used_id
    if len(userid) > 0:
        cluster_userid_list.append(userid)


createCorr(0.85)
dfs2()