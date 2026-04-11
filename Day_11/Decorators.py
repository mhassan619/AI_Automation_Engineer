## lets discuss about decorators
# Simple Decorator 
def my_decorator(func):
    def wrapper():
        print(f"First, Run this.")
        func()
        print(f"Then run this!")
    return wrapper
def say_hello():
    print("Hello Hassan")
    
# Manually Wrapping
say_hello = my_decorator(say_hello)
say_hello()
## Shortcut - Professional Syntax
def my_decorator(func):
    def wrapper():
        print(f"First Run this!")
        func()
        print(f"Then run this!")
    return wrapper
@my_decorator   # this works same as above we do manual decrotor
def say_hello():
    print("Hello Hassan")
say_hello()

## Lets discuss about practical decorators
import time
# 1. Timer decorator - tells the function time
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"⏱⏰  {func.__name__} takes {end-start:.4f} seconds")
        return result
    return wrapper
# 2. Logger decorator - function calls track karo
def logger(func):
    def wrapper(*args,**kwargs):
        print(f"📝 {func.__name__} is called - args: {args}")
        result = func(*args,**kwargs)
        print(f"✅ {func.__name__} completed - result: {result}")
        return result
    return wrapper
# 3. Validation decrator
def validate_marks(func):
    def wrapper(self,subject,marks):
        if not 0 <= marks <= 100:
            print(f"❌ Invalid marks: {marks}")
            return 
        return func(self, subject,marks)
    return wrapper
@timer
@logger
def calculator_average(marks):
    return sum(marks) / len(marks)
result = calculator_average([85,92,101,91])