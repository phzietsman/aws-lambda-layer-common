import sys
import json
import os

import boto3

LAYER_NAME = sys.argv[1]
DICT_KEY = sys.argv[2]

REGIONS = [
    "us-east-2",
    "us-east-1",
    "us-west-1",
    "us-west-2",
    "af-south-1",
    "ap-east-1",
    "ap-southeast-3",
    "ap-south-1",
    "ap-northeast-3",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-northeast-1",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-south-1",
    "eu-west-3",
    "eu-north-1",
    "me-south-1",
    "sa-east-1"]

arns = []
for region in REGIONS:

    client = boto3.client('lambda', region_name=region)
    latest = client.list_layer_versions(LayerName=LAYER_NAME)['LayerVersions'][0]['LayerVersionArn']
    arns.append(latest)
    print(f'Latest in {region} is {latest}')

content = {}

if os.path.isfile('./versions.json'):
    with open("./versions.json", "r") as f:
        content = json.load(f)

content[DICT_KEY] = arns
with open("./versions.json", "w") as f:
    f.write(json.dumps(content))