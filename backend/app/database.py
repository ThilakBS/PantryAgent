import os
from dotenv import load_dotenv #Import .env values

load_dotenv() #load .env values

d_base = os.environ["DATABASE_URL"]
