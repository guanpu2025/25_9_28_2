import numpy as np
import pandas as pd
from tqdm import tqdm

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score


class LVW:
    """
    LVW: Las Vegas Wrapper 特征选择算法。

    输入:
        数据集 D
        特征集 A
        学习算法 L
        停止条件控制参数 T

    输出:
        特征子集 A*
    """

    def __init__(self, T=20, cv=5, random_state=42):
        self.T = T
        self.cv = cv
        self.random_state = random_state

    def _encode_dataframe(self, X):
        X_encoded = X.copy()

        cat_cols = X_encoded.select_dtypes(exclude=["number"]).columns.tolist()

        for col in cat_cols:
            if str(X_encoded[col].dtype) == "category":
                X_encoded[col] = X_encoded[col].cat.codes
            else:
                X_encoded[col] = pd.factorize(X_encoded[col])[0]

        return X_encoded

    def fit(self, X, y):
        X_encoded = self._encode_dataframe(X)
        y = pd.factorize(y)[0]
        A = X_encoded.columns.tolist()
        rng = np.random.default_rng(self.random_state)

        learner = DecisionTreeClassifier(max_depth=4, random_state=self.random_state)
        cv = StratifiedKFold(n_splits=self.cv, shuffle=True, random_state=self.random_state)

        E, d, A_star, t = ...   # TODO: 初始化 E, d, A*, t
        history = []
        pbar = tqdm(desc="LVW search")

        while t < self.T:
            pbar.update(1)

            mask = rng.random(len(A)) < 0.5
            if mask.sum() == 0:
                mask[rng.integers(len(A))] = True

            A_prime = ...   # TODO: 根据 mask 得到候选特征子集 A'
            d_prime = ...   # TODO: 计算候选特征子集的特征数 d'

            E_prime = 1 - cross_val_score(
                learner, X_encoded[A_prime], y,
                cv=cv, scoring="accuracy"
            ).mean()

            if ...: # TODO: 判断是否更新最优特征子集
                E, d, A_star, t = ...   # TODO: 更新 E, d, A*, t
                tqdm.write(f"更新最优子集: error={E:.4f}, feature_num={d}, features={A_star}")
            else:
                t += 1

            pbar.set_postfix({
                "best_error": f"{E:.4f}",
                "best_d": d,
                "no_update": f"{t}/{self.T}"
            })
            history.append({
                "error": E_prime,
                "feature_num": d_prime,
                "features": A_prime,
                "current_best_error": E,
                "current_best_feature_num": d,
                "no_update_count": t
            })

        pbar.close()

        self.best_error = E
        self.best_score = 1 - E
        self.selected_features = A_star
        self.history = pd.DataFrame(history)

        return self

    def get_selected_features(self):
        return self.selected_features

    def get_best_score(self):
        return self.best_score

    def get_best_error(self):
        return self.best_error

    def get_history(self):
        return self.history
    

if __name__ == "__main__":
    from bank_marketing import get_bank_marketing

    Xy, X, y = get_bank_marketing()

    selector = LVW(
        T=20,
        cv=5,
        random_state=42
    )

    selector.fit(X, y)

    print("\nLVW 选择的特征子集 A*：")
    print(selector.get_selected_features())

    print("\n最优交叉验证准确率：")
    print(selector.get_best_score())

    print("\n最优交叉验证错误率：")
    print(selector.get_best_error())