import os
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import mlflow
import config as cfg

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_registry_uri("uc:http://127.0.0.1:8080")
# print(cfg.tokens['agent'])
os.environ["MLFLOW_UC_OSS_TOKEN"] = cfg.tokens['agent'] # Enable while creating function

X, y = datasets.fetch_california_housing(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(os.environ["MLFLOW_UC_OSS_TOKEN"])
with mlflow.start_run():
    # Train a sklearn model on the housing dataset
    clf = RandomForestRegressor(max_depth=7)
    clf.fit(X_train, y_train)
    # Take the first row of the training dataset as the model input example.
    input_example = X_train.iloc[[0]]
    # Log the model and register it as a new version in UC.
    mlflow.sklearn.log_model(
        sk_model=clf,
        artifact_path="model",
        # The signature is automatically inferred from the input example and its predicted output.
        input_example=input_example,
        registered_model_name="unity.devconf_demo.california_housing_datasetx",
    )