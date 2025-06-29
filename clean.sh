#!/bin/bash
echo "Cleaning Python and CDK build artifacts..."
find . -type d -name '__pycache__' -exec rm -r {} +
find . -name '*.pyc' -delete
rm -rf cdk.out
echo "Done!"

