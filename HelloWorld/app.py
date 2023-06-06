from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route and its handler
@app.route('/')
def hello_world():
    return 'Hello, World!'

# # Run the app if this script is executed directly
if __name__ == '__main__':
    app.run()
