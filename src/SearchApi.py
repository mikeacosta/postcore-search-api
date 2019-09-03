import boto3
import json
import requests
from requests_aws4auth import AWS4Auth

region = 'us-west-2'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = '[Elasticsearch endpoint]'
index = 'postcore-index/ad'
url = 'https://' + host + '/' + index + '/_search'

def lambda_handler(event, context):

    query = {
        "size": 25,
        "query": {
            "multi_match": {
               "query": event['queryStringParameters']['q'],
                "fields": ["Title"]
            }
        }
    }

    headers = { "Content-Type": "application/json" }

    r = requests.get(url, auth=awsauth, headers=headers, data=json.dumps(query))

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": '*'
        },
        "isBase64Encoded": False
    }

    response['body'] = r.text
    return response