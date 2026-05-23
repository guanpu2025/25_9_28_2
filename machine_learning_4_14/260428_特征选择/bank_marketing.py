import pandas as pd
from sklearn.datasets import fetch_openml

def get_bank_marketing():
    X, y = fetch_openml(
        data_id=1461,
        as_frame=True,
        return_X_y=True
    )

    X.columns = [
        "age",
        "job",
        "marital",
        "education",
        "default",
        "balance",
        "housing",
        "loan",
        "contact",
        "day",
        "month",
        "duration",
        "campaign",
        "pdays",
        "previous",
        "poutcome",
    ]

    y = y.map({"1": "no", "2": "yes"})

    Xy = pd.concat([X, y], axis=1)

    return Xy, X, y


if __name__ == '__main__':
    Xy, X, y = get_bank_marketing()

    print(Xy)
    print(X.shape)
    print(y.value_counts())
    print(X.dtypes)
    print()