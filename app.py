from flask import Flask
import os 

username = os.getenv('USER_NAME')
app = Flask(__name__)

#route.decorator()
@app.route("/")
def home_page():
    return "Welcome to the Searce.. !"

@app.route("/Health")
def status():
    return "I am up"

@app.route("/user_name")
def display_name():
    return "{}!".format(username)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
