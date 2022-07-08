from boto3 import resource
import config
from boto3.dynamodb.conditions import Key


AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
REGION_NAME = config.REGION_NAME
ENDPOINT_URL = config.ENDPOINT_URL
resource = resource(
   'dynamodb',
   aws_access_key_id     = 'Madhavi',
   aws_secret_access_key = 'Madhavi',
   region_name           = 'us-east-1',
   endpoint_url=ENDPOINT_URL
)

table = resource.Table('DietProject_Table')

def read_recipe(filterexp, filterexpval, projectionexp):
    response = table.scan(
        FilterExpression=Key(filterexp).eq(filterexpval),
        ProjectionExpression=projectionexp
    )

    return response




