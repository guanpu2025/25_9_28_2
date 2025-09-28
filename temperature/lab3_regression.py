import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 数据加载
df = pd.read_csv('temperature.CSV', names=['Day', 'Temp'])
X_raw = df[['Day']]
y = df['Temp']

# 创造三个特征，并创造输入
days_in_year = 365
X_trend = X_raw.copy()                              # 特征1: 线性趋势项 (就是原始的天数)
X_sin = np.sin(2 * np.pi * X_raw / days_in_year)    # 特征2: 周期项 (正弦)
X_cos = np.cos(2 * np.pi * X_raw / days_in_year)    # 特征3: 周期项 (余弦)
X_hybrid = np.concatenate([X_trend, X_sin, X_cos], axis=1)

# 训练模型
model_hybrid = LinearRegression()
model_hybrid.fit(X_hybrid, y)

# 绘制曲线
line_x_raw = np.linspace(1, 31, 300).reshape(-1, 1)
line_x_trend = line_x_raw
line_x_sin = np.sin(2 * np.pi * line_x_raw / days_in_year)
line_x_cos = np.cos(2 * np.pi * line_x_raw / days_in_year)
line_x_hybrid = np.concatenate([line_x_trend, line_x_sin, line_x_cos], axis=1)

# 进行预测
line_y_pred = model_hybrid.predict(line_x_hybrid)

# 绘图
plt.figure(figsize=(12, 7))
plt.scatter(X_raw, y, color='blue', alpha=0.7, label='true temperature (1-30)')
plt.plot(line_x_raw, line_y_pred, color='purple', linewidth=3, label='mix model')

plt.title('mix model predict', fontsize=15)
plt.xlabel('date (5.x)', fontsize=12)
plt.ylabel('temperature (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.savefig('hybrid_fit.png')