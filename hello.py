__author__ = 'Don'

from flask import Flask
app = Flask(__name__)   # magic identifier __name__ identifier as the name of the file

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
