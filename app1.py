from flask import Flask

app = Flask(__name__)

@app.route('/')
def display():
    return "Came back after 2 days"


app.run(port = 5000)
