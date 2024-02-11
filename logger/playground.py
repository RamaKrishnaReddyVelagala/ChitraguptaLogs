def decorator_func(function, kwargs):
    print("entered kwargs")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

some_dic = {"firstname": "ram",
            "lastname": "velagala"}

@decorator_func
def append_dic(some_dic):
    some_dic.update({"age": "30",
            "gender": "male"})
    return some_dic

# decorator_func(some_dic)

append_dic(some_dic)


# def my_decorator(func):
#     print("before wrapper.")
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     print("after wrapper.")
#     return wrapper

# def say_whee():
#     print("Whee!")
# say_whee = my_decorator(say_whee)
# say_whee()
