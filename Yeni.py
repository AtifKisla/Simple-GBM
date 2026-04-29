import pandas as pd

df = pd.read_csv("amazon.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
# ======================
# STEP 2: CLEANING
# ======================

df = df.drop(columns=[
    "product_id",
    "product_name",
    "about_product",
    "user_id",
    "user_name",
    "review_id",
    "review_title",
    "review_content",
    "img_link",
    "product_link"
])

print(df.head())
print(df.columns)
print(df.info())

# ======================
# STEP 3: NUMERIC CLEANING
# ======================

df = df.dropna(subset=["rating_count"])

df["discounted_price"] = (
    df["discounted_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["actual_price"] = (
    df["actual_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["discount_percentage"] = (
    df["discount_percentage"]
    .str.replace("%", "", regex=False)
    .astype(float)
)

df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

df["rating_count"] = (
    df["rating_count"]
    .str.replace(",", "", regex=False)
    .astype(int)
)

df = df.dropna()

print(df.head())
print(df.info())
# ======================
# STEP 4: FEATURE ENGINEERING + TARGET
# ======================

import numpy as np

df["price_diff"] = df["actual_price"] - df["discounted_price"]
df["popularity_log"] = np.log1p(df["rating_count"])

df["success_score"] = df["rating"] * df["popularity_log"]

threshold = df["success_score"].median()
df["target"] = (df["success_score"] > threshold).astype(int)

print(df[[
    "discounted_price",
    "actual_price",
    "discount_percentage",
    "rating",
    "rating_count",
    "price_diff",
    "popularity_log",
    "success_score",
    "target"
]].head())

print(df["target"].value_counts())
# ======================
# STEP 5 (UPDATED): LEAK-FREE FEATURES
# ======================

X = df[[
    "discounted_price",
    "actual_price",
    "discount_percentage",
    "price_diff"
]]

y = df["target"]
print("Current X columns:")
print(X.columns)
# ======================
# STEP 6-9: MODELS + EVALUATION
# ======================


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_preds = lr.predict(X_test)

gbm = GradientBoostingClassifier(random_state=42)
gbm.fit(X_train, y_train)
gbm_preds = gbm.predict(X_test)

print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_preds))
print("GBM Accuracy:", accuracy_score(y_test, gbm_preds))

print("\nGBM Classification Report:")
print(classification_report(y_test, gbm_preds))

importance = pd.Series(gbm.feature_importances_, index=X.columns)
print("\nFeature Importance:")
print(importance.sort_values(ascending=False))

# ======================
# STEP 10: XGBOOST
# ======================

from xgboost import XGBClassifier

xgb = XGBClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    random_state=42,
    use_label_encoder=False,
    eval_metric='logloss'
)

xgb.fit(X_train, y_train)

xgb_preds = xgb.predict(X_test)

from sklearn.metrics import accuracy_score

print("XGBoost Accuracy:", accuracy_score(y_test, xgb_preds))
