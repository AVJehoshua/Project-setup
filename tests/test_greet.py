from lib.greet import *

def test_say_hello_to_given_name():
    result = greet("AVJehoshua")
    assert result == "Hello, AVJehoshua!"