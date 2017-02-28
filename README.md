# rest_api_demo_dynamodb

Note: Intentionally using Python 2.7 to be able to deploy on AWS Lambda.

## Setup

Requires: AWS configuration is valid and accessible by user in her home directory
(`~/.aws/config` and `~/.aws/credentials`).

    git clone https://github.com/nikos/rest_api_demo_dynamodb.git
    cd rest_api_demo_dynamodb

    virtualenv-2 venv
    source ./venv/bin/activate

    pip install -r requirements.txt
    ./run.py

    open http://0.0.0.0:5000/


## Testing

Assuming you have installed it via `brew` you can start local DynamoDB with:

    brew services start rjcoelho/boneyard/dynamodb-local

You should now be able to access your local DynamoDB on localhost port 8000.
