# create zip archives with code and dependencies
python ZipHelper.py

# push zip archives to S3
aws s3 sync 'pkg' s3://postcore-bucket/Postcore.SearchApi

# package cloudformation
aws cloudformation package --s3-bucket postcore-bucket --s3-prefix Postcore.SearchApi --template-file template.yaml --output-template-file gen/template-generated.yaml

# deploy
aws cloudformation deploy --template-file gen/template-generated.yaml --stack-name PostcoreSearchApi --capabilities CAPABILITY_IAM