# Flask settings
FLASK_SERVER_HOST = '0.0.0.0'
FLASK_SERVER_PORT = 5000
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# JSON Web Token (JWT) config
JWT_AUTH_USERNAME_KEY = 'email'
JWT_AUTH_URL_RULE = '/login'
JWT_EXPIRATION_DELTA = 7 * 24 * 60 * 60
SECRET_KEY = 'Super duper secret'

# Flask-DynamoDB settings
DYNAMOBD_REGION = 'eu-central-1'
# DYNAMOBD_URL = "http://localhost:8000"
DYNAMOBD_URL = None