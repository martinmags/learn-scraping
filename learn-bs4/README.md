# Configure AWS account
Create an AWS account
Create an S3 bucket
Create a Cloudfront Distribution

# Configure on your system
pip install awscli
Enter credentials (found on your security credentials page)
pip install boto3 (python sdk for aws)


# Information Endpoints
S3_bucketname = 'tft-static-assets'
Cloudfront_Distribution_domainname = 'd31kowojj2sx7j.cloudfront.net'


# NOTES
Uploading to S3 Already accounts for duplicates. 
If it already exists, then it just overwrites it.

# Learned Skills
Scraping from a site with Beautiful Soup
Downloading files with wget
Unzipping files with zipfile
Uploading files to AWS S3 with boto3
