import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 数据准备环节
df = pd.read_csv('temperature.CSV', names=['Day', 'Temp'])
X_raw = df[['Day']]
y = df['Temp']

# 处理新特征
days_in_year = 365
X_sin = np.sin(2 * np.pi * X_raw / days_in_year)
X_cos = np.cos(2 * np.pi * X_raw / days_in_year)
X_trig = np.concatenate([X_sin, X_cos], axis=1)

# 训练模型
model_trig = LinearRegression()
model_trig.fit(X_trig, y)

# 预测第31天
day_to_predict = 31
# 将要预测的日期放入一个数组
predict_x_raw = np.array([[day_to_predict]])

# 对这个新数据点进行完全相同的特征工程
predict_x_sin = np.sin(2 * np.pi * predict_x_raw / days_in_year)
predict_x_cos = np.cos(2 * np.pi * predict_x_raw / days_in_year)
predict_x_trig = np.concatenate([predict_x_sin, predict_x_cos], axis=1)

# 使用训练好的模型进行预测
predicted_temp = model_trig.predict(predict_x_trig)
print(f"使用三角函数模型预测:")
print(f"  - 5月 {day_to_predict}日的最高气温大约为: {predicted_temp[0]:.2f} °C")
print("\n")

# 可视化拟合结果与预测点 
# 生成从1到31的平滑曲线用于绘图
line_x = np.linspace(1, 31, 300).reshape(-1, 1)

# 对这300个点进行同样的特征工程
line_x_sin = np.sin(2 * np.pi * line_x / days_in_year)
line_x_cos = np.cos(2 * np.pi * line_x / days_in_year)
line_x_trig = np.concatenate([line_x_sin, line_x_cos], axis=1)

# 进行预测
line_y_pred = model_trig.predict(line_x_trig)

# 绘图
plt.figure(figsize=(12, 7))
plt.scatter(X_raw, y, color='blue', alpha=0.7, label='true temperature (1-30)')
# 三角函数拟合曲线
plt.plot(line_x, line_y_pred, color='red', linewidth=3, label='Trigonometric Functions')
# 第31天的预测点
plt.scatter(day_to_predict, predicted_temp, color='magenta', marker='*', s=250, zorder=5, label=f'{day_to_predict}th temperature')

plt.title('Trigonometric Functions predict', fontsize=15)
plt.xlabel('date (5.x)', fontsize=12)
plt.ylabel('temperature (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()