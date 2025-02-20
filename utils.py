from unitycatalog.ai.core.client import UnitycatalogFunctionClient
from unitycatalog.client import ApiClient, Configuration


def get_user_token():
    with open("/Users/avsingh/Documents/talks/devconfIn/unitycatalog/etc/conf/user-token.txt") as token_file:
        return token_file.read()

def get_api_client(token):
    auth_header = f"Bearer {token}"
    config = Configuration(host="http://localhost:8080/api/2.1/unity-catalog")
    return ApiClient(configuration=config, header_name="Authorization", header_value=auth_header)