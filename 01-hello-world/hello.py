from flask import Flask
app = Flask(__name__)

# Logging into the root address will call this function
@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

# Navigating to this address, where <name> is a template parameter
# will send the person's name to the callback.
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)

