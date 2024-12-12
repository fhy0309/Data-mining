import numpy as np
import matplotlib.pyplot as plt

# 示例数据
data = {
    'L': [1.169137, -0.306752, 0.485423, -0.702272, -0.065196],
    'LAST_TO_END': [-0.380609, 1.700039, -0.799763, -0.419696, 0.001108],
    'FLIGHT_COUNT': [-0.082699, -0.575251, 2.482909, -0.154421, -0.270434],
    'SEG_KM_SUM': [-0.089877, -0.536363, 2.423625, -0.151675, -0.288397],
    'avg_discount': [-0.166561, -0.199573, 0.322459, -0.301706, 1.897520]
}

categories = list(data.keys())
num_categories = len(categories)

# 将数据转换为numpy数组
values = np.array(list(data.values()))

# 计算角度
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]  # 闭合图形

# 创建绘图
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 绘制每个聚类的雷达图
for i in range(values.shape[0]):
    values_i = values[i].tolist()
    values_i += values_i[:1]  # 闭合图形
    ax.plot(angles, values_i, linewidth=2, linestyle='solid', label=f'Cluster {i+1}')
    ax.fill(angles, values_i, alpha=0.25)

# 设置标签
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories)

# 添加图例
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# 显示图形
plt.show()

