from flask import Flask

app=Flask(__name__)

@app.route('/')
def helloworld():
    return "<p>Homepage</p>"

@app.route('/login')
def login():
     return "loginpage"

@app.route("/register")
def register():
     return "register"

@app.route("/index")
def index():
     return "index"

#dynamic routing
#string route(default type)
@app.route('/user/<string:username>')
def show_user(username):
     return f"Hello,{username}"
@app.route('/user_id/<int:user_id>')
def show_user_id(user_id):
     return f"user id is {user_id}"

@app.route('/price/<float:price>')
def show_price(price):
    return f'the price is{price}' 
@app.route('/path/<path:subpath>')
def show_path(subpath):
    return f'the path is{subpath}'      
app.run()