## Prepare

1. Download tools:
    1. Spark v3.4 -
    2. x-table jar file -
    3. Java 11
    4. python 3
2. Create python virtual environment
   ` python `
3. Install python packages in venv
    `python -m pip instal -r requirements.txt`

## Setup and start Unity server and UI

1. Clone OSS Unity catalog github repository
    ```git@github.com:unitycatalog/unitycatalog.git
       cd unitycatalog
    ```
2. Follow the guide linked below to configure external identity provider  - https://docs.unitycatalog.io/server/auth/#configure-your-external-identity-provider

3. [Optional] To enable UC server to vend AWS temporary credentials to access S3 buckets (for accessing External tables/volumes),enable set the parameters in etc/conf/server.properties as specified in https://docs.unitycatalog.io/server/configuration/#configuration

3. Start UC server
    `bin/start-uc-server`

4. Follow the guide below to configure authentication in Unity UI - https://docs.unitycatalog.io/server/auth/#configure-and-restart-the-unity-catalog-ui

5. Start UC UI(accessible at http://localhost:3000/)
    ```cd ui
       yarn install
       yarn start
    ```
6. Add user(present in external ID provider) account to the local database
    `bin/uc --auth_token $(cat etc/conf/token.txt) user create --name "<username>" --email <user-email-id>`
7. Grant necessary permissions to the user:

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

7. Login with user account and save access token
    `bin/uc auth login --output jsonPretty`
    Kepe value for <"access_token"> handy for a later use




### Train and Register Model

### Create function in UC

### Call unity function from master script
