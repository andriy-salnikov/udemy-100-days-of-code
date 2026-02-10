def my_function():
    print("Hello from a function")
    result = 2 * 3
    return result

output = my_function()
print(output)

def format_name(f_name, l_name):
    """Take a first and last name and format it         
    to return the title case version of the name."""
    # this is a docstring
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
