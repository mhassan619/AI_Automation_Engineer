import datetime
def log_action(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {func.__name__} executed.")
        return result
    return wrapper