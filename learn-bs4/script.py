import urllib.request, urllib.parse, urllib.error, wget
import os.path, os, boto3, zipfile, shutil
from bs4 import BeautifulSoup
from botocore.config import Config
from settings import aws_id, aws_key

def uploadDirectory(path, bucketname):
  for root, dirs, files in os.walk(path):
    for file in files:
      s3.upload_file(os.path.join(root, file), bucketname, '{}/{}'.format(path, file))
  return


""" Initialize """
s3 = boto3.client('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_key)

""" Web Scrape resource download links """
url = 'https://developer.riotgames.com/docs/tft#static-data'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
substring = "/tft/"
bucketname = 'tft-static-assets'

for tag in tags:
  download_url = tag.get('href')
  if download_url:
    if substring in download_url:
      filename = download_url.split("/tft/")[1]
      dirname = filename.split(".")[0]
      if os.path.exists(filename) is False:
        # Download Files
        wget.download(tag.get('href'))
        print()
        """ Unzip Files """
        try:
          print("Unzipping files...............")
          with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(dirname)
        except IOError as e:
          print(e)
        
        """ Upload to S3 Bucket """
        try:
          print("Uploading to S3 Bucket........")
          uploadDirectory(dirname, bucketname)
        except:
          print("An Exception occurred")
        
      """ Clean up """
      try:
        print("Deleting {} and {}....".format(filename, dirname))
        os.remove(filename)
        shutil.rmtree(dirname)
      except:
        print("Error deleting")


        
        



