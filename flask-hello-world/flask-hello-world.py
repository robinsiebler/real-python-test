from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query


@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"


@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correct"


# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"


@app.route("/name/<name>")
def index(name):
	return "Hello, {}".format(name.title()), 200


if __name__ == '__main__':
	import argparse
parser = argparse.ArgumentParser(description='Development Server Help')
parser.add_argument("-d", "--debug", action="store_true", dest="debug_mode",
                    help="run in debug mode (for use with PyCharm)", default=False)
parser.add_argument("-p", "--port", dest="port",
                    help="port of server (default:%(default)s)", type=int, default=5000)

cmd_args = parser.parse_args()
app_options = {"port": cmd_args.port}

if cmd_args.debug_mode:
	app_options["debug"] = True
	app_options["use_debugger"] = False
	app_options["use_reloader"] = False

app.run(**app_options)
