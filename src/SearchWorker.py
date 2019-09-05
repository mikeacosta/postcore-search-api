import boto3
import json
import os
from elasticsearch import Elasticsearch, RequestsHttpConnection

def connectES(esEndPoint):
    print ('Connecting to ES Endpoint {0}'.format(esEndPoint))
    try:
        esClient = Elasticsearch(
            hosts=[{'host': esEndPoint, 'port': 443}],
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection)
        return esClient
    except Exception as E:
        print("Unable to connect to {0}".format(esEndPoint))
        print(E)
        exit(3) 

endpoint = os.environ['endpoint']
esClient = connectES(endpoint)

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    print('SNS rec''d {0}'.format(message))
    ad = json.loads(message)
    adId = ad['Id']
    res = esClient.index(index='postcore-index', doc_type='ad', id=adId, body=ad) 
    print('Result: {0} {1}'.format(adId, res['result']))