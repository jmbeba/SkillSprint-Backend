from datetime import datetime, timedelta
import random

def generate_start_date():
    start_date = datetime.now()
    random_start_date = start_date + timedelta(days=random.randint(1, 60))

    return random_start_date.strftime("%Y-%m-%d")  # Format the date as a string

def generate_end_date():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=60)  
    random_end_date = end_date + timedelta(days=random.randint(1,90))
    
    return random_end_date.strftime("%Y-%m-%d")
