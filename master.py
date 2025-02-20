
import asyncio
import config as cfg
from utils import get_api_client
from unitycatalog.ai.core.client import UnitycatalogFunctionClient
import pandas as pd


async def main():
    token = cfg.tokens['agent']
    api_client = get_api_client(token)

    uc_client = UnitycatalogFunctionClient(api_client=api_client)
    result = uc_client.execute_function(
        function_name="unity.devconf_demo.predict_diabetes_possibility",
        parameters={
            "glucose_level": 150,
            "blood_pressure": 40,
            "insulin_level": 10 ,
            "bmi": 33.6,
            "diabetes_pedigree_function": 2.228,
            "age": 49,
            "uc_token": token}
        )
    print("Diabetes prediction: ", result.value)

asyncio.run(main())