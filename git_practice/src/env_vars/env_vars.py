# 1- pip install python-dotenv

# 2- import os

# 3- from dotenv import find_dotenv ,  load_dotenv

import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
print(dotenv_path)
load = load_dotenv(dotenv_path)
print(load)

API_KEY = os.getenv("API_KEY")
print(API_KEY)
PASSWORD = os.getenv("PASSWORD")
print(PASSWORD)
