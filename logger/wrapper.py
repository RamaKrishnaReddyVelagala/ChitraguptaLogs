class Wrapper:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        # Pass through any arguments to the original function.
        self.func(*args, **kwargs)
        print("Something is happening after the function is called.")

@Wrapper
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("ram")
