class CustomError(Exception):
    def __init__(self, message):
        self.message = message

def risky_function():
    raise CustomError("Something went wrong!")

try:
    risky_function()
except CustomError as e:
    print(f"Caught custom exception: {e.message}")