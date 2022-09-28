## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()




from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    wrapper_function



@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p> This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/1hM5kW7OU6d7AOUUjv/giphy-downsized-large.gif" width=200>'

@app.route("/bye")
@make_bold
def say_bye():
    return "Bye"

@app.route("/<name>")
def greeting(name):
    return f"Hello there {name}"

if __name__ == "__main__":
    app.run(debug=True)


## Python Decorator Function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before function
        function()
        function()
        #Do something after function
    return wrapper_function

@delay_decorator
def say_hello():
    time.sleep(2)
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello()
say_bye()
say_greeting()

# Advanced Python Decorator Functions

class User:
    def __init__(self, user):
        self.name = user
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s blog. ")

new_user = User("dirk")
new_user.is_logged_in = True
create_blog_post(new_user)
