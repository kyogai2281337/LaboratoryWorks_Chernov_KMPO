def syntax_error_func(): # excepted behaviour
    raise SyntaxError

def somefunc_syntax_error():
    а = 0 # russian letter
    return а

def unexcepted_map_usage():
    ma = {"k": "v"}
    print(ma[0])

# unexcepted_map_usage() # KeyError
"""
    print(ma[0])
          ~~^^^
KeyError: 0

Right usage:

ma = {"k": "v"}
print(ma["k"])
"""

# print("Hello World" # SyntaxError
"""
print("Hello World" # SyntaxError
    ^
SyntaxError: '(' was never closed
Right usage:

print("Hello World")
"""
