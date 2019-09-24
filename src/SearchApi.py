import boto3
import json
import os
import requests
from requests_aws4auth import AWS4Auth

region = 'us-west-2'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
url = os.environ['url']

def lambda_handler(event, context):

    titlesOnly = False

    try:
        searchTerm = event['queryStringParameters']['q']
    except:
        searchTerm = ''

    try:
        if event['queryStringParameters']['t'] == '1':
            fields = ["Title"]
            titlesOnly = True
            if len(searchTerm) >= 2:
                searchTerm = '*' + searchTerm + '*' 
            else:
                searchTerm = ''
        else:
            fields = ["Title","Description"]
    except:
        fields = ["Title","Description"]

    query = {
        "size": 25,
        "query": {
            "query_string": {
               "query": searchTerm,
                "fields": fields
            }
        }
    }

    headers = { "Content-Type": "application/json" }

    r = requests.get(url, auth=awsauth, headers=headers, data=json.dumps(query))

    obj = json.loads(r.text)
    hits = obj['hits']['hits']
    searchResults = []

    for item in hits:
        if titlesOnly == True:
            result = json.dumps(item['_source'])
            title = json.loads(result)
            searchResults.append(title.get('Title'))
        else:
            searchResults.append(item['_source'])

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": '*'
        },
        "isBase64Encoded": False,
        "body": json.dumps(searchResults)
    }        

    print("search term: " + searchTerm)
    print(json.dumps(response))
    return response