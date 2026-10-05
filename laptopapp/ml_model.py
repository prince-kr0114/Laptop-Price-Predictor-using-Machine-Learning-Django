from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import pandas as pd
import os
from django.conf import settings


BASE_DIR = settings.BASE_DIR
CSV_PATH = os.path.join(BASE_DIR, "laptop_price_1lakhs.csv")

df = pd.read_csv(CSV_PATH)

X = df[["RAM", "Brand", "Processor", "Storage"]]
y = df["Price"]

col = ["Brand", "Processor"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

process = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), col)
    ],
    remainder="passthrough"
)

model = Pipeline([
    ("preprocessing", process),
    ("regressor", DecisionTreeRegressor(random_state=42))
])

model.fit(X_train, y_train)

predict = model.predict(X_test)

r2 = r2_score(y_test, predict)

print("R2 Score:", round(r2, 4))


def predict_laptop_price(ram, brand, processor, storage):

    new_data = pd.DataFrame({
        "RAM": [ram],
        "Brand": [brand],
        "Processor": [processor],
        "Storage": [storage]
    })

    result = model.predict(new_data)

    return result[0]