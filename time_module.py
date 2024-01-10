from datetime import datetime


# For getting the current time
def get_time():
    now = datetime.now()
    current_time = now.strftime("The Current Time is %H:%M:%S %p")
    return current_time
    