# Error Handing in Python

- ValueError
- NameError
- KeyError
- IndexError
- FileNotFoundError

try:
    #     Something that might cause an exception
    pass
except FileNotFoundError:
    # Do this if there was an exception
    # You can have multiple excepts
    pass
except KeyError as error_message:
    print(f"The key {error_message} not found")
    pass
else:
    # Do this if there were no exceptions
    pass
finally:
    pass
    # Do this no matter what happens
    # For cleaning up

# You can also raise an exception
age = 30
if age < 5:
    raise ValueError("Age is below Limit!")
