import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# 读取数据
datafile = 'air_data.csv'
data = pd.read_csv(datafile, encoding='utf-8')

# 删除非数值型特征
data = data.select_dtypes(include=[np.number])

# 使用均值填充NaN值
imputer = SimpleImputer(strategy='mean')
data = imputer.fit_transform(data)

# 定义预处理方法
scalers = {
    'StandardScaler': StandardScaler(),
    'MinMaxScaler': MinMaxScaler(),
    'RobustScaler': RobustScaler(),
    'PCA': PCA(n_components=2)
}

# 定义K-Means参数
k = 5

# 存储聚类结果
results = {}

for name, scaler in scalers.items():
    # 预处理数据
    if name == 'PCA':
        transformed_data = scaler.fit_transform(data)
    else:
        transformed_data = scaler.fit_transform(data)

    # 使用K-Means聚类
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(transformed_data)

    # 保存聚类结果
    results[name] = {
        'labels': kmeans.labels_,
        'centers': kmeans.cluster_centers_
    }

# 使用PCA进行降维
pca = PCA(n_components=2)
pca_data = pca.fit_transform(data)

# 可视化聚类结果
plt.figure(figsize=(15, 10))

for i, (name, result) in enumerate(results.items()):
    plt.subplot(2, 2, i + 1)
    plt.scatter(pca_data[:, 0], pca_data[:, 1], c=result['labels'], cmap='viridis', s=50)
    plt.title(f'{name} Clustering')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')

plt.tight_layout()
plt.show()