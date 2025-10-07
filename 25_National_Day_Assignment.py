import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

advertise_data = pd.read_csv("D:\\advertising.csv")
plt.rcParams["font.family"] = ["SimHei"]

x = advertise_data[['TV', 'Radio', 'Newspaper']]
y = advertise_data['Sales']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=36)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)
print(f"测试集R^2分数{r2:.2f}")

effect = pd.DataFrame({'特征':x_test.columns, '系数':model.coef_})
print(effect)