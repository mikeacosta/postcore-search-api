# postcore-search-api

Search component of the microservice-oriented [postcore.net](https://github.com/mikeacosta/postcore-web) application.

## Lambda functions
`SearchWorker.py` - Lambda function invoked by SNS notification.  Message payload is stored in Elasicsearch.

`SearchApi.py` - API Gateway passes request to this Lambda function, which queries Elasticsearch domain and returns search results.

## Technologies
* Amazon Elasticsearch Service
* AWS Lambda
* API Gateway