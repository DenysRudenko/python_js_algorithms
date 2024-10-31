import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

string, max_width = input("Please enter you string: "), int(input("Please enter your width value: "))
result = wrap(string, max_width)
print(result)