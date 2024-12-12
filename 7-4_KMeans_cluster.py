# #-*- coding: utf-8 -*-
# #K-Means聚类算法
#
# import pandas as pd
# from sklearn.cluster import KMeans #导入K均值聚类算法
#
# inputfile = 'zscoreddata.xls' #待聚类的数据文件
# k = 5                       #需要进行的聚类类别数
#
# #读取数据并进行聚类分析
# data = pd.read_excel(inputfile) #读取数据
#
# #调用k-means算法，进行聚类分析
# kmodel = KMeans(n_clusters = k) #n_jobs是并行数，一般等于CPU数较好
# kmodel.fit(data) #训练模型
#
# # 查看聚类中心
# cluster_centers = kmodel.cluster_centers_
# print("聚类中心:")
# print(cluster_centers)
#
# # 查看各样本对应的类别
# labels = kmodel.labels_
# print("各样本对应的类别:")
# print(labels)

import pandas as pd
from sklearn.cluster import KMeans  # 导入K均值聚类算法

inputfile = 'zscoreddata.xls'  # 待聚类的数据文件
k = 5  # 需要进行的聚类类别数

# 读取数据并进行聚类分析
data = pd.read_excel(inputfile)  # 读取数据

# 调用k-means算法，进行聚类分析
kmodel = KMeans(n_clusters=k)  # n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data)  # 训练模型

kmodel.cluster_centers_  # 查看聚类中心
kmodel.labels_  # 查看各样本对应的类别

r1 = pd.Series(kmodel.labels_).value_counts()  # 统计各类的个数
r2 = pd.DataFrame(kmodel.cluster_centers_)  # 获取聚类中心
r = pd.concat([r2, r1], axis=1)  # 合并
r.columns = list(['L', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']) + ['类别数目']  # 加上列名
print(r)

df_data = pd.read_excel('zscoreddata.xls')

r2 = pd.concat([df_data, pd.Series(kmodel.labels_, index=df_data.index)], axis=1)
r2.columns = list(['L', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']) + ['聚类类别']  # 加列名
print(r2)
