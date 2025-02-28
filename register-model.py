import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
import pandas as pd
import mlflow
import config as cfg

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_registry_uri("uc:http://127.0.0.1:8080")

# Set MLFLOW_UC_OSS_TOKEN for mlflow to autheticate to UC server
os.environ["MLFLOW_UC_OSS_TOKEN"] = cfg.tokens['agent']

# Load data from csv
df=pd.read_csv("../healthcare-diabetes.csv")

# Remove indentifiable data
df=df.drop(columns=["Id"])

#separate outcome and features
X=df.iloc[:,:-1]
y=df.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

with mlflow.start_run():
    # Train a sklearn model on the diabetes dataset
    bc = BaggingClassifier(n_estimators=150, random_state=2)
    bc.fit(X_train,y_train)
    # Take the first row of the training dataset as the model input example.
    input_example = X_train.iloc[[0]]
    # Log the model and register it as a new version in UC.
    mlflow.sklearn.log_model(
        sk_model=bc,
        artifact_path="model",
        # The signature is automatically inferred from the input example and its predicted output.
        input_example=input_example,
        registered_model_name="unity.devconf_demo.diabetes_prediction",
    )