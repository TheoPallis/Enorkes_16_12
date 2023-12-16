import datetime

def generate_timestamp_filename(filename_prefix):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    return f"{filename_prefix}_{timestamp}"