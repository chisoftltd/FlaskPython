from flask import Flask
#
app = Flask(__name__)
#
#
# # @app.route('/')
# # def hello_world():
# #     return ('<h1 style="text-align: center">Hello, World!</h1>'
# #             '<p style="text-align: center">This is a paragraph</p>'
# #             '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTkxYjhlb21lMHliNTZrYXk0ZjJwYWV6ZGkyMTR2Mm9yaHFld3FqMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C8oGI85zRUqWhcwnVR/giphy.gif" style="text-align: center">')
# #
# # @app.route("/bye")
# # def say_bye():
# #     return "Bye"
# #
# # @app.route("/username/<name>/<int:number>")
# # def greet(name, number):
# #     return f"Hello there {name}, you are {number} years old!"
# #
# # if __name__ == "__main__":
# #     #Reload and auto debugger
# #     app.run(debug=True)
#
# ## Advanced Python Decorator Function
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
#
# new_user = User("Benjamin")
# new_user.is_logged_in = True
# create_blog_post(new_user)

inputs = eval(input())

def logging_decorator(fn):
    def wrapper(*args):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned {result}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c

a_function(inputs[0], inputs[1], inputs[2])