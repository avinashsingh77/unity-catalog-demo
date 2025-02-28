from utils import get_api_client
from unitycatalog.ai.core.client import UnitycatalogFunctionClient
import config as cfg
import asyncio


def predict_diabetes_possibility(
    glucose_level: int,
    blood_pressure: int,
    insulin_level: int,
    bmi: float,
    diabetes_pedigree_function: float,
    age: int,
    uc_token: str
    ) -> int:
    """
    Returns an boolean depending on possibility of diabetes for a human being
    with relevant health information details passed

    Args:
        glucose_level: Plasma glucose concentration over 2 hours in an oral glucose tolerance test.
        blood_pressure: Diastolic blood pressure (mm Hg).
        insulin_level: 2-Hour serum insulin (mu U/ml).
        bmi: Body mass index (weight in kg / height in m^2).
        diabetes_pedigree_function: Diabetes pedigree function, a genetic score of diabetes.
        age: Age in years.
        uc_token: Access token to authenticate to Unity server
    Returns:
        outcome: Binary classification indicating the presence (1) or absence (0) of diabetes.
    """

    import numpy as np
    import mlflow
    import os
    import pandas as pd

    os.environ['MLFLOW_UC_OSS_TOKEN'] = uc_token
    mlflow.set_registry_uri('uc:http://127.0.0.1:8080')
    db_model = mlflow.pyfunc.load_model(f'models:/unity.devconf_demo.diabetes_prediction/4')

    X_test_input = pd.DataFrame(data={
        "Pregnancies": [6],
        "Glucose": [148],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [29],
        "Insulin": [insulin_level],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [diabetes_pedigree_function],
        "Age": [age]
    })

    y_pred=db_model.predict(X_test_input)
    return np.array_str(y_pred)

async def main():
    token = cfg.tokens['agent']
    api_client = get_api_client(token)

    uc_client = UnitycatalogFunctionClient(api_client=api_client)
    CATALOG = "unity"
    SCHEMA = "devconf_demo"

    # Asynchronously create the function
    my_function = await uc_client.create_python_function_async(
        func=predict_diabetes_possibility,
        catalog=CATALOG,
        schema=SCHEMA,
        replace=True
    )

asyncio.run(main())