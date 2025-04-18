## Prepare
1. Create python virtual environment and activate it
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install python packages in venv
    `python -m pip instal -r requirements.txt`

## Setup and start Unity server and UI

1. Clone OSS Unity catalog github repository
    ```
    git@github.com:unitycatalog/unitycatalog.git
    cd unitycatalog
    ```
2. Follow the guide linked below to configure external identity provider  - https://docs.unitycatalog.io/server/auth/#configure-your-external-identity-provider

3. [Optional] To enable UC server to vend AWS temporary credentials to access S3 buckets (for accessing External tables/volumes),enable set the parameters in etc/conf/server.properties as specified in https://docs.unitycatalog.io/server/configuration/#configuration

4. Start UC server
    `bin/start-uc-server`

5. Follow the guide below to configure authentication in Unity UI - https://docs.unitycatalog.io/server/auth/#configure-and-restart-the-unity-catalog-ui

6. Start UC UI(accessible at http://localhost:3000/)
    ```cd ui
       yarn install
       yarn start
    ```
7. Add user(present in external ID provider) account to the local database
    `bin/uc --auth_token $(cat etc/conf/token.txt) user create --name "<username>" --email <user-email-id>`
8. Grant necessary permissions to the user:

    Catalog
    ```
    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type catalog  --name unity --principal <user-emil-id> --privilege "USE CATALOG"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type catalog  --name unity --principal <user-emil-id> --privilege "CREATE SCHEMA"
    ```

    Schema
    ```
    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type schema  --name unity.devconf_demo --principal  <user-emil-id> --privilege "USE SCHEMA"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type schema  --name unity.devconf_demo --principal  <user-emil-id> --privilege "CREATE TABLE"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type schema  --name unity.devconf_demo --principal  <user-emil-id> --privilege "CREATE VOLUME"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type schema  --name unity.devconf_demo --principal  <user-emil-id> --privilege "CREATE MODEL"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type schema  --name unity.devconf_demo --principal  <user-emil-id> --privilege "CREATE FUNCTION"
    ```

    Function
    ```
    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type function  --name unity.devconf_demo.predict_diabetes_possibility --principal  <user-emil-id> --privilege "EXECUTE"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type function  --name unity.devconf_demo.predict_diabetes_possibility --principal  <user-emil-id> --privilege "SELECT"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type function  --name unity.devconf_demo.predict_diabetes_possibility --principal  <user-emil-id> --privilege "MODIFY"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type function  --name unity.devconf_demo.predict_diabetes_possibility --principal  <user-emil-id> --privilege "MODIFY"
    ```

    Model
    ```
    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type registered_model  --name unity.devconf_demo.predict_diabetes_possibility --principal  <user-emil-id> --privilege "SELECT"

    bin/uc --auth_token $(cat etc/conf/token.txt) permission create --securable_type registered_model  --name unity.devconf_demo.predict_diabetes_possibility --principal  <user-emil-id> --privilege "MODIFY"
    ```

9. Login with user account and save access token
    `bin/uc auth login --output jsonPretty`
10. Copy and rename `sample-config.py` to `config.py`. Use value for `access_token` recieved in step 9 to replace value for 'agent' key in config.py




### Train and Register Model
```
python register-model.py
```


### Create function in UC

```
python create-function.py
```

### Call unity function from master script
```
python master.py
```
