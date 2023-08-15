[![auto-readme](https://github.com/phzietsman/aws-lambda-layer-common/actions/workflows/auto-readme.yml/badge.svg)](https://github.com/phzietsman/aws-lambda-layer-common/actions/workflows/auto-readme.yml)
[![Python General Layers](https://github.com/phzietsman/aws-lambda-layer-common/actions/workflows/python-general.yml/badge.svg?branch=main)](https://github.com/phzietsman/aws-lambda-layer-common/actions/workflows/python-general.yml)
[![Python Database Layers](https://github.com/phzietsman/aws-lambda-layer-common/actions/workflows/python-database.yml/badge.svg)](https://github.com/phzietsman/aws-lambda-layer-common/actions/workflows/python-database.yml)
[![Python Data Wrangling Layers](https://github.com/phzietsman/aws-lambda-layer-common/actions/workflows/python-datawrangling.yml/badge.svg)](https://github.com/phzietsman/aws-lambda-layer-common/actions/workflows/python-datawrangling.yml)

# Lambda layers
Commonly used libraries packaged as lambda layers.

## Using 3rd party layers
Use caution when including a third party layer in your application. To verify the content of a layer you can download the content and manually inspect it:
```bash
URL=$(aws lambda get-layer-version --layer-name $LAYER_ARN --version-number $LAYER_VERSION --query Content.Location --output text)
curl $URL -o layer.zip
```

# Supported runtimes
## python3
### General 
 arn:aws:lambda:us-east-2:306986787463:layer:common-python-libraries:16  
 arn:aws:lambda:us-east-1:306986787463:layer:common-python-libraries:13  
 arn:aws:lambda:us-west-1:306986787463:layer:common-python-libraries:9  
 arn:aws:lambda:us-west-2:306986787463:layer:common-python-libraries:9  
 arn:aws:lambda:af-south-1:306986787463:layer:common-python-libraries:13  
 arn:aws:lambda:ap-east-1:306986787463:layer:common-python-libraries:11  
 arn:aws:lambda:ap-southeast-3:306986787463:layer:common-python-libraries:12  
 arn:aws:lambda:ap-south-1:306986787463:layer:common-python-libraries:13  
 arn:aws:lambda:ap-northeast-3:306986787463:layer:common-python-libraries:13  
 arn:aws:lambda:ap-northeast-2:306986787463:layer:common-python-libraries:11  
 arn:aws:lambda:ap-southeast-1:306986787463:layer:common-python-libraries:13  
 arn:aws:lambda:ap-southeast-2:306986787463:layer:common-python-libraries:12  
 arn:aws:lambda:ap-northeast-1:306986787463:layer:common-python-libraries:15  
 arn:aws:lambda:ca-central-1:306986787463:layer:common-python-libraries:12  
 arn:aws:lambda:eu-central-1:306986787463:layer:common-python-libraries:14  
 arn:aws:lambda:eu-west-1:306986787463:layer:common-python-libraries:10  
 arn:aws:lambda:eu-west-2:306986787463:layer:common-python-libraries:12  
 arn:aws:lambda:eu-south-1:306986787463:layer:common-python-libraries:11  
 arn:aws:lambda:eu-west-3:306986787463:layer:common-python-libraries:12  
 arn:aws:lambda:eu-north-1:306986787463:layer:common-python-libraries:14  
 arn:aws:lambda:me-south-1:306986787463:layer:common-python-libraries:11  
 arn:aws:lambda:sa-east-1:306986787463:layer:common-python-libraries:14  


### Databases 
 arn:aws:lambda:us-east-2:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:us-east-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:us-west-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:us-west-2:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:af-south-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ap-east-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ap-southeast-3:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ap-south-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ap-northeast-3:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ap-northeast-2:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ap-southeast-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ap-southeast-2:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ap-northeast-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:ca-central-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:eu-central-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:eu-west-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:eu-west-2:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:eu-south-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:eu-west-3:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:eu-north-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:me-south-1:306986787463:layer:common-python-libraries-database:3  
 arn:aws:lambda:sa-east-1:306986787463:layer:common-python-libraries-database:3  


### Data Wrangling 
 arn:aws:lambda:us-east-2:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:us-east-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:us-west-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:us-west-2:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:af-south-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ap-east-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ap-southeast-3:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ap-south-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ap-northeast-3:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ap-northeast-2:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ap-southeast-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ap-southeast-2:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ap-northeast-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:ca-central-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:eu-central-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:eu-west-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:eu-west-2:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:eu-south-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:eu-west-3:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:eu-north-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:me-south-1:306986787463:layer:common-python-libraries-datawrangling:2  
 arn:aws:lambda:sa-east-1:306986787463:layer:common-python-libraries-datawrangling:2  



## node
### General
 arn:aws:lambda:us-east-2:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:us-east-1:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:us-west-1:306986787463:layer:common-node-libraries:4  
 arn:aws:lambda:us-west-2:306986787463:layer:common-node-libraries:5  
 arn:aws:lambda:af-south-1:306986787463:layer:common-node-libraries:8  
 arn:aws:lambda:ap-east-1:306986787463:layer:common-node-libraries:5  
 arn:aws:lambda:ap-southeast-3:306986787463:layer:common-node-libraries:5  
 arn:aws:lambda:ap-south-1:306986787463:layer:common-node-libraries:5  
 arn:aws:lambda:ap-northeast-3:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:ap-northeast-2:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:ap-southeast-1:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:ap-southeast-2:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:ap-northeast-1:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:ca-central-1:306986787463:layer:common-node-libraries:5  
 arn:aws:lambda:eu-central-1:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:eu-west-1:306986787463:layer:common-node-libraries:7  
 arn:aws:lambda:eu-west-2:306986787463:layer:common-node-libraries:5  
 arn:aws:lambda:eu-south-1:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:eu-west-3:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:eu-north-1:306986787463:layer:common-node-libraries:6  
 arn:aws:lambda:me-south-1:306986787463:layer:common-node-libraries:5  
 arn:aws:lambda:sa-east-1:306986787463:layer:common-node-libraries:6  


### Data Wrangling 
 arn:aws:lambda:us-east-2:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:us-east-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:us-west-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:us-west-2:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:af-south-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ap-east-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ap-southeast-3:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ap-south-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ap-northeast-3:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ap-northeast-2:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ap-southeast-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ap-southeast-2:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ap-northeast-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:ca-central-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:eu-central-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:eu-west-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:eu-west-2:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:eu-south-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:eu-west-3:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:eu-north-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:me-south-1:306986787463:layer:common-node-libraries-datawrangling:2  
 arn:aws:lambda:sa-east-1:306986787463:layer:common-node-libraries-datawrangling:2  
