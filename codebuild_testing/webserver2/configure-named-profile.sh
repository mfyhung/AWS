#!/bin/bash

# fail on any error
set -eu

# configure named profile
/usr/local/bin/aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
/usr/local/bin/aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
/usr/local/bin/aws configure set region $AWS_REGION

# verify that profile is configured
/usr/local/bin/aws configure list
