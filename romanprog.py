from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Roman!"
    
@app.route("/<username>")
def display_usr(username):
    return "Hello %s" % username

if __name__ == "__main__":
    app.run()
