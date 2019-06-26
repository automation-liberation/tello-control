import os

from dotenv import load_dotenv

load_dotenv()

broker_url = os.environ.get('BROKER_URL')
result_backend = os.environ.get('RESULT_BACKEND')
