from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join( dirname(__file__), '.env' )
load_dotenv( dotenv_path )

# Accessing Variables
aws_id = os.getenv('AWS_ID')
aws_key = os.getenv('AWS_KEY')