import os
from datetime import datetime

try:
    first_name = os.getenv('first_name')
    last_name = os.getenv('last_name')
    print(f"This is my firstname, {first_name}!")
    print(f"This is my lastname, {last_name}!")
    date = datetime.now()
    print(f"The current time is {date.isoformat()}")
except Exception as error:
    print(f"An error occurred: {error}")