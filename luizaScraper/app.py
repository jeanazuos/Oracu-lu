from flask import Flask
app = Flas(__name__)

@app.route('/')
def hello_world():
    return 'hello, World!'

