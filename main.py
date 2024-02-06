from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p style="text-align: center">This is a paragraph</p>'
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTkxYjhlb21lMHliNTZrYXk0ZjJwYWV6ZGkyMTR2Mm9yaHFld3FqMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/C8oGI85zRUqWhcwnVR/giphy.gif" style="text-align: center">')

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    #Reload and auto debugger
    app.run(debug=True)
