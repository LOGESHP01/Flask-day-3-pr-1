#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<h1>hello_world</h1>"

@app.route('/hello1')
def hello_world1():
    return "<h1>hai</h1>"
@app.route('/hello1/hello2')
def hello_world2():
    return "<h1>byee<h1>"
if __name__=='__main__':
    app.run(debug=True)