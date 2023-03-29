from flask import Flask

app = Flask(__name__)

@app.route("/a")
def hello_world():
    return "<h1>Hello World!!</h1>"

@app.route("/welcome")
def disp():
    return "<h1>Welcome to ABC Corporation</h1>"

@app.route("/")
def disp2():
    return "<h1>Company Name: ABC Corporation</h1> <h1>Location: India</h1> <h1>Contact Detail: 999-999-9999</h1>"   

if __name__=="__main__":
    app.run(host="0.0.0.0")
